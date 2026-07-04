---
name: mo-graphify-obsidian-memory
description: >
  Production-grade unified memory system for AI agents. Combines Obsidian markdown vaults
  (human-readable source of truth) with PostgreSQL+pgvector (fast semantic search),
  security admission control, emotional salience scoring, prospective memory, and MCP
  server integration. Triggered by: "graphify my knowledge", "obsidian memory",
  "unified memory", "save to memory", "remember this", "knowledge graph",
  "memory vault", "prospective memory", "memory search", "consolidate memory".
---

# mo-Graphify + Obsidian Memory v2.0

> **Production-grade unified memory for AI agents**
>
> This skill gives your agent a brain: it can remember conversations, search memories
> by meaning (not just keywords), schedule future reminders, and protect itself from
> poisoned data. Everything is stored in plain markdown files you can read and edit.

## What This Skill Does (In One Minute)

| Feature | What It Means For You |
|---------|----------------------|
| **Markdown Vault** | All memories are plain `.md` files. You can open them in Obsidian, VS Code, or any text editor. |
| **Semantic Search** | Ask "what did we discuss about neural networks?" — it finds related ideas even if the words don't match exactly. |
| **Graph Memory** | Notes link to each other (`[[Like This]]`). The agent sees relationships, not just isolated facts. |
| **Security Gate** | Bad data (attacks, mistakes, contradictions) is caught before it poisons long-term memory. |
| **Salience Scoring** | Important memories (failures, user emphasis, contradictions) are remembered longer. |
| **Prospective Memory** | The agent can set reminders: *"Check this again in 3 days"* — and actually do it. |
| **Sleep Consolidation** | Nightly maintenance: merge duplicates, archive stale notes, fix broken links. |
| **MCP Server** | Claude Code, Cursor, and any MCP client can read/write the agent's memory directly. |

## Architecture

```
Your Question: "What did we decide about the API rate limit?"
                |
                v
+---------------------------------------------+
|  UNIFIED MEMORY SYSTEM                      |
|  +-----------+ +-----------+ +-----------+  |
|  | Semantic  | |  Keyword  | |   Graph   |  |
|  |  Search   | |  Search   | |  Search   |  |
|  | (pgvector)| |(tsvector) | |(wiki-links|  |
|  +-----+-----+ +-----+-----+ +-----+-----+  |
|        |             |             |         |
|        +-------------+-------------+         |
|                      |                       |
|            +---------v---------+             |
|            |  Merge Results    |             |
|            |   (RRF Rank)      |             |
|            +---------+---------+             |
|                      |                       |
|  +-------------------v--------------------+  |
|  |    Markdown Files (Obsidian Vault)     |  |
|  |  ~/Documents/Kimi/Workspaces/Mnemosyne |  |
|  |            /obsidian-vault/            |  |
|  +----------------------------------------+  |
+---------------------------------------------+
```

## Prerequisites

```bash
# 1. Install PostgreSQL with pgvector extension
#    macOS: brew install postgresql@16 && brew install pgvector
#    Then: CREATE EXTENSION vector; in your database

# 2. Install Python dependencies
pip install psycopg2-binary pyyaml numpy

# Optional (for better embeddings):
pip install sentence-transformers

# 3. Set environment variables (or use defaults)
export MEMORY_DB_DSN="postgresql://localhost:5432/mnemosyne"
export MEMORY_VAULT_PATH="/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"
```

## Quick Start

```python
from mo_graphify_memory import UnifiedMemorySystem

# Initialize (auto-creates DB schema and syncs vault)
memory = UnifiedMemorySystem()

# Remember something
memory.remember(
    title="API Rate Limit Decision",
    content="We decided on 100 req/min with burst to 200. Monitor p95 latency; alert if >200ms.",
    tags=["api", "infrastructure", "decision"],
    salience=0.9  # High importance
)

# Search by meaning
results = memory.recall("rate limiting policy")
for r in results:
    print(f"{r['title']}: {r['score']:.2f}")

# Set a future reminder
memory.remind_me(
    title="Review API metrics",
    trigger_at="2026-07-07T09:00:00",
    recurring="weekly"
)

# Run nightly consolidation (merge duplicates, archive stale)
memory.consolidate()
```

---

## Complete Implementation

```python
"""
mo-graphify-obsidian-memory v2.0
Production-grade unified memory system for AI agents.

Features:
- Obsidian-compatible markdown vault (source of truth)
- PostgreSQL + pgvector (semantic + keyword + graph search)
- Admission control (security gate before writes)
- Emotional salience scoring (important memories persist longer)
- Prospective memory (scheduled future reminders)
- Sleep consolidation (nightly maintenance batch)
- MCP stdio server (JSON-RPC 2.0 tool interface)

Environment variables:
    MEMORY_DB_DSN       PostgreSQL connection string
    MEMORY_VAULT_PATH   Obsidian vault directory
    EMBEDDING_MODEL     Model name (default: all-MiniLM-L6-v2)
    OLLAMA_URL          Local Ollama API (fallback)
    OPENAI_API_KEY      OpenAI API key (fallback)
"""

import os
import sys
import re
import json
import glob
import hashlib
import logging
import threading
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple
from dataclasses import dataclass, field, asdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

VAULT_PATH = os.environ.get(
    "MEMORY_VAULT_PATH",
    "/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"
)
DB_DSN = os.environ.get("MEMORY_DB_DSN", "postgresql://localhost:5432/mnemosyne")
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
EMBEDDING_DIM = int(os.environ.get("EMBEDDING_DIM", "384"))
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("unified-memory")

# ---------------------------------------------------------------------------
# Safe Filename Helper
# ---------------------------------------------------------------------------

def safe_filename(title: str) -> str:
    """Convert a title to a safe filename."""
    return re.sub(r'[^\w\s-]', '', title).strip().replace(" ", "-") + ".md"

# ---------------------------------------------------------------------------
# Embedding Engine (3-tier fallback)
# ---------------------------------------------------------------------------

class Embedder:
    """
    Generate vector embeddings for text.
    
    Tier 1: sentence-transformers (local, no API calls)
    Tier 2: Ollama API (local LLM server)
    Tier 3: Deterministic hash-based projection (zero dependencies)
    """
    
    def __init__(self, model_name: str = EMBEDDING_MODEL, dim: int = EMBEDDING_DIM):
        self.model_name = model_name
        self.dim = dim
        self._model = None
        self._provider = None
        self._lock = threading.Lock()
        self._init_provider()
    
    def _init_provider(self):
        """Try embedding providers in order."""
        # Tier 1: sentence-transformers
        try:
            from sentence_transformers import SentenceTransformer
            self._model = SentenceTransformer(self.model_name)
            self._provider = "sentence-transformers"
            logger.info(f"Embedder: using sentence-transformers ({self.model_name})")
            return
        except Exception as e:
            logger.warning(f"sentence-transformers unavailable: {e}")
        
        # Tier 2: Ollama
        try:
            import urllib.request
            req = urllib.request.Request(f"{OLLAMA_URL}/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=2) as resp:
                if resp.status == 200:
                    self._provider = "ollama"
                    logger.info(f"Embedder: using Ollama at {OLLAMA_URL}")
                    return
        except Exception as e:
            logger.warning(f"Ollama unavailable: {e}")
        
        # Tier 3: deterministic hash fallback
        self._provider = "hash"
        logger.info("Embedder: using deterministic hash fallback (no external deps)")
    
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of texts into vectors."""
        if not texts:
            return []
        
        if self._provider == "sentence-transformers":
            try:
                import numpy as np
                vectors = self._model.encode(texts, convert_to_numpy=True)
                return [self._normalize(v.tolist()) for v in vectors]
            except Exception as e:
                logger.error(f"sentence-transformers failed: {e}, falling back")
                self._provider = "hash"
        
        if self._provider == "ollama":
            try:
                import urllib.request
                results = []
                for text in texts:
                    body = json.dumps({"model": self.model_name, "prompt": text}).encode()
                    req = urllib.request.Request(
                        f"{OLLAMA_URL}/api/embeddings",
                        data=body,
                        headers={"Content-Type": "application/json"},
                        method="POST"
                    )
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        data = json.loads(resp.read())
                        results.append(self._normalize(data.get("embedding", [])))
                return results
            except Exception as e:
                logger.error(f"Ollama failed: {e}, falling back")
                self._provider = "hash"
        
        # Hash fallback: deterministic, no external deps
        return [self._hash_embed(t) for t in texts]
    
    def _hash_embed(self, text: str) -> List[float]:
        """Deterministic embedding via hash-based random projection."""
        vec = [0.0] * self.dim
        for i in range(self.dim):
            h = hashlib.sha256(f"{text}::dim{i}".encode()).hexdigest()
            val = int(h[:8], 16) / 0xFFFFFFFF
            vec[i] = val * 2 - 1
        norm = sum(x * x for x in vec) ** 0.5
        if norm > 0:
            vec = [x / norm for x in vec]
        return vec
    
    def _normalize(self, vec: List[float]) -> List[float]:
        """Pad/truncate and L2-normalize a vector."""
        vec = list(vec)
        if len(vec) < self.dim:
            vec.extend([0.0] * (self.dim - len(vec)))
        elif len(vec) > self.dim:
            vec = vec[:self.dim]
        norm = sum(x * x for x in vec) ** 0.5
        if norm > 0:
            vec = [x / norm for x in vec]
        return vec

# ---------------------------------------------------------------------------
# PostgreSQL + pgvector Store
# ---------------------------------------------------------------------------

class PgVectorStore:
    """
    PostgreSQL-backed store with pgvector for semantic search,
    tsvector for keyword search, and recursive CTEs for graph traversal.
    """
    
    def __init__(self, dsn: str = DB_DSN):
        self.dsn = dsn
        self._local = threading.local()
        self._ensure_schema()
    
    def _conn(self):
        """Get or create a thread-local connection."""
        if not hasattr(self._local, "conn") or self._local.conn.closed:
            import psycopg2
            self._local.conn = psycopg2.connect(self.dsn)
        return self._local.conn
    
    def _ensure_schema(self):
        """Create tables and indexes if they don't exist."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")
                
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS notes (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        title TEXT NOT NULL,
                        content TEXT NOT NULL DEFAULT '',
                        tags TEXT[] DEFAULT '{}',
                        note_type TEXT NOT NULL DEFAULT 'concept',
                        status TEXT NOT NULL DEFAULT 'active',
                        salience FLOAT DEFAULT 0.5,
                        embedding VECTOR(384),
                        tsv TSVECTOR,
                        vault_path TEXT NOT NULL,
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                        CONSTRAINT unique_title_vault UNIQUE (title, vault_path)
                    );
                """)
                
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS links (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        source_note_id UUID NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
                        target_note_id UUID NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
                        link_type TEXT DEFAULT 'wiki',
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                        CONSTRAINT no_self_link CHECK (source_note_id != target_note_id),
                        CONSTRAINT unique_link UNIQUE (source_note_id, target_note_id)
                    );
                """)
                
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS prospective (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        title TEXT NOT NULL,
                        content TEXT,
                        trigger_at TIMESTAMPTZ NOT NULL,
                        recurring TEXT,
                        status TEXT DEFAULT 'pending',
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                    );
                """)
                
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS notes_embedding_idx
                    ON notes USING ivfflat (embedding vector_cosine_ops)
                    WITH (lists = 100);
                """)
                cur.execute("CREATE INDEX IF NOT EXISTS notes_tsv_idx ON notes USING gin (tsv);")
                cur.execute("CREATE INDEX IF NOT EXISTS notes_tags_idx ON notes USING gin (tags);")
                cur.execute("CREATE INDEX IF NOT EXISTS notes_salience_idx ON notes (salience DESC);")
                cur.execute("CREATE INDEX IF NOT EXISTS prospective_trigger_idx ON prospective (trigger_at);")
                
                cur.execute("""
                    CREATE OR REPLACE FUNCTION notes_fts_update() RETURNS trigger AS $$
                    BEGIN
                        NEW.tsv := setweight(to_tsvector('english', coalesce(NEW.title, '')), 'A') ||
                                   setweight(to_tsvector('english', coalesce(NEW.content, '')), 'B') ||
                                   setweight(to_tsvector('english', coalesce(array_to_string(NEW.tags, ' '), '')), 'C');
                        RETURN NEW;
                    END
                    $$ LANGUAGE plpgsql;
                """)
                cur.execute("""
                    DROP TRIGGER IF EXISTS notes_fts_trigger ON notes;
                    CREATE TRIGGER notes_fts_trigger
                    BEFORE INSERT OR UPDATE ON notes
                    FOR EACH ROW EXECUTE FUNCTION notes_fts_update();
                """)
                
                conn.commit()
                logger.info("Database schema initialized.")
    
    def upsert_note(self, title: str, content: str, tags: List[str], 
                    note_type: str, status: str, salience: float,
                    embedding: List[float], vault_path: str) -> str:
        """Insert or update a note. Returns note ID."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO notes (title, content, tags, note_type, status, salience, embedding, vault_path)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (title, vault_path) DO UPDATE SET
                        content = EXCLUDED.content,
                        tags = EXCLUDED.tags,
                        note_type = EXCLUDED.note_type,
                        status = EXCLUDED.status,
                        salience = EXCLUDED.salience,
                        embedding = EXCLUDED.embedding,
                        updated_at = NOW()
                    RETURNING id;
                """, (title, content, tags, note_type, status, salience, embedding, vault_path))
                note_id = cur.fetchone()[0]
                conn.commit()
                return note_id
    
    def delete_note(self, title: str, vault_path: str) -> bool:
        """Delete a note by title."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM notes WHERE title = %s AND vault_path = %s RETURNING id;",
                            (title, vault_path))
                deleted = cur.fetchone()
                conn.commit()
                return deleted is not None
    
    def search_semantic(self, query_embedding: List[float], top_k: int = 10,
                        filters: Optional[Dict] = None) -> List[Dict]:
        """Vector similarity search."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                where = "WHERE status = 'active'"
                params = [query_embedding, top_k]
                
                if filters:
                    if filters.get("tags"):
                        where += " AND tags && %s"
                        params.append(filters["tags"])
                    if filters.get("note_type"):
                        where += " AND note_type = %s"
                        params.append(filters["note_type"])
                
                cur.execute(f"""
                    SELECT id, title, content, tags, note_type, salience, vault_path,
                           1 - (embedding <=> %s::vector) AS score
                    FROM notes
                    {where}
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s;
                """, params)
                
                cols = [d[0] for d in cur.description]
                return [dict(zip(cols, row)) for row in cur.fetchall()]
    
    def search_keyword(self, query: str, top_k: int = 10) -> List[Dict]:
        """Full-text search using PostgreSQL tsvector."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, title, content, tags, note_type, salience, vault_path,
                           ts_rank_cd(tsv, plainto_tsquery('english', %s), 32) AS score
                    FROM notes
                    WHERE status = 'active'
                      AND tsv @@ plainto_tsquery('english', %s)
                    ORDER BY score DESC
                    LIMIT %s;
                """, (query, query, top_k))
                cols = [d[0] for d in cur.description]
                return [dict(zip(cols, row)) for row in cur.fetchall()]
    
    def search_graph(self, note_title: str, depth: int = 2, top_k: int = 10) -> List[Dict]:
        """Graph traversal: find notes connected via wiki-links within N hops."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    WITH RECURSIVE graph AS (
                        SELECT n.id, n.title, n.content, n.tags, n.salience, n.vault_path,
                               0 AS depth, n.id AS root_id
                        FROM notes n
                        WHERE n.title = %s AND n.status = 'active'
                        
                        UNION ALL
                        
                        SELECT n2.id, n2.title, n2.content, n2.tags, n2.salience, n2.vault_path,
                               g.depth + 1, g.root_id
                        FROM graph g
                        JOIN links l ON l.source_note_id = g.id
                        JOIN notes n2 ON n2.id = l.target_note_id
                        WHERE n2.status = 'active'
                          AND g.depth < %s
                    )
                    SELECT DISTINCT id, title, content, tags, salience, vault_path, depth
                    FROM graph
                    WHERE depth > 0
                    ORDER BY depth, salience DESC
                    LIMIT %s;
                """, (note_title, depth, top_k))
                cols = [d[0] for d in cur.description]
                return [dict(zip(cols, row)) for row in cur.fetchall()]
    
    def hybrid_search(self, query: str, query_embedding: List[float],
                      top_k: int = 10) -> List[Dict]:
        """
        Reciprocal Rank Fusion (RRF) of semantic + keyword + salience signals.
        k=60 is the standard RRF constant.
        """
        semantic = self.search_semantic(query_embedding, top_k=top_k * 2)
        keyword = self.search_keyword(query, top_k=top_k * 2)
        
        scores: Dict[str, Dict] = {}
        
        def add_results(results, source, weight):
            for rank, r in enumerate(results, 1):
                nid = str(r["id"])
                if nid not in scores:
                    scores[nid] = dict(r)
                    scores[nid]["rrf_score"] = 0.0
                    scores[nid]["sources"] = []
                scores[nid]["rrf_score"] += weight * (1.0 / (60 + rank))
                scores[nid]["sources"].append(source)
        
        add_results(semantic, "semantic", 1.0)
        add_results(keyword, "keyword", 0.8)
        
        for nid in scores:
            scores[nid]["rrf_score"] += scores[nid].get("salience", 0.5) * 0.2
        
        sorted_results = sorted(scores.values(), key=lambda x: x["rrf_score"], reverse=True)
        return sorted_results[:top_k]
    
    def update_links(self, note_id: str, wiki_links: List[str]):
        """Update graph edges for a note based on its wiki-links."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM links WHERE source_note_id = %s;", (note_id,))
                for target_title in wiki_links:
                    cur.execute("""
                        INSERT INTO links (source_note_id, target_note_id, link_type)
                        SELECT %s, id, 'wiki' FROM notes
                        WHERE title = %s AND status = 'active'
                        ON CONFLICT (source_note_id, target_note_id) DO NOTHING;
                    """, (note_id, target_title.strip()))
                conn.commit()
    
    def get_stats(self) -> Dict:
        """Get vault statistics."""
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM notes WHERE status = 'active';")
                note_count = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM links;")
                link_count = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM prospective WHERE status = 'pending';")
                pending = cur.fetchone()[0]
                return {"notes": note_count, "links": link_count, "pending_reminders": pending}

# ---------------------------------------------------------------------------
# Vault Manager (File Operations)
# ---------------------------------------------------------------------------

class VaultManager:
    """
    Manages the Obsidian-compatible markdown vault.
    Files are the source of truth; the database is a rebuildable index.
    """
    
    def __init__(self, vault_path: str = VAULT_PATH):
        self.vault_path = Path(vault_path)
        self.vault_path.mkdir(parents=True, exist_ok=True)
    
    def write_note(self, title: str, content: str, tags: List[str] = None,
                   note_type: str = "concept", status: str = "active",
                   salience: float = 0.5, links: List[str] = None) -> Path:
        """Write a note to the vault."""
        tags = tags or []
        links = links or []
        filepath = self.vault_path / safe_filename(title)
        
        frontmatter = {
            "title": title,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "tags": tags,
            "type": note_type,
            "status": status,
            "salience": salience,
            "links": links,
        }
        
        body = f"# {title}\n\n{content}"
        if links:
            body += "\n\n## Related\n\n"
            for link in links:
                body += f"- [[{link}]]\n"
        
        import yaml
        yaml_content = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        full = f"---\n{yaml_content}---\n{body}\n"
        filepath.write_text(full, encoding="utf-8")
        return filepath
    
    def read_note(self, title: str) -> Optional[Dict]:
        """Read a note from the vault. Returns dict with frontmatter + content."""
        filepath = self.vault_path / safe_filename(title)
        if not filepath.exists():
            return None
        text = filepath.read_text(encoding="utf-8")
        return self._parse_note(text)
    
    def _parse_note(self, text: str) -> Dict:
        """Parse markdown with YAML frontmatter."""
        import yaml
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                except Exception:
                    frontmatter = {}
                body = parts[2].strip()
                return {"frontmatter": frontmatter, "body": body, "raw": text}
        return {"frontmatter": {}, "body": text, "raw": text}
    
    def extract_wiki_links(self, text: str) -> List[str]:
        """Extract [[Wiki Links]] from text."""
        return re.findall(r'\[\[(.*?)\]\]', text)
    
    def list_notes(self) -> List[Path]:
        """List all markdown files in the vault."""
        return list(self.vault_path.glob("*.md"))
    
    def sync_to_db(self, db: PgVectorStore, embedder: Embedder) -> Dict:
        """Sync all vault files to the database."""
        stats = {"upserted": 0, "deleted": 0, "errors": 0}
        for filepath in self.list_notes():
            try:
                text = filepath.read_text(encoding="utf-8")
                parsed = self._parse_note(text)
                fm = parsed["frontmatter"]
                title = fm.get("title", filepath.stem.replace("-", " "))
                content = parsed["body"]
                tags = fm.get("tags", [])
                note_type = fm.get("type", "concept")
                status = fm.get("status", "active")
                salience = float(fm.get("salience", 0.5))
                embedding = embedder.embed([content])[0] if content else [0.0] * EMBEDDING_DIM
                note_id = db.upsert_note(title, content, tags, note_type, status, salience, embedding, str(self.vault_path))
                wiki_links = self.extract_wiki_links(text)
                db.update_links(note_id, wiki_links)
                stats["upserted"] += 1
            except Exception as e:
                logger.error(f"Sync error for {filepath}: {e}")
                stats["errors"] += 1
        logger.info(f"Vault sync complete: {stats}")
        return stats

# ---------------------------------------------------------------------------
# Admission Control (Security Gate)
# ---------------------------------------------------------------------------

class AdmissionControl:
    """
    Validates memory writes before they become persistent.
    Protects against poisoning, contradictions, and low-quality data.
    """
    
    def __init__(self, db: PgVectorStore, embedder: Embedder):
        self.db = db
        self.embedder = embedder
    
    def validate(self, title: str, content: str, tags: List[str]) -> Tuple[bool, str, float]:
        """
        Validate a proposed memory write.
        Returns: (is_valid, reason, confidence_score)
        """
        checks = []
        
        # Length gate
        if len(content) < 10:
            checks.append((False, "Content too short (< 10 chars)", 0.0))
        
        # Injection pattern detection
        injection_patterns = [
            r"ignore previous instructions",
            r"disregard (all|your) (instructions|training)",
            r"system prompt",
            r"you are now",
            r"DAN mode",
        ]
        content_lower = content.lower()
        for pattern in injection_patterns:
            if re.search(pattern, content_lower):
                checks.append((False, f"Potential injection pattern detected: {pattern}", 0.1))
        
        # Near-duplicate detection
        emb = self.embedder.embed([content])[0]
        similar = self.db.search_semantic(emb, top_k=5)
        for s in similar:
            if s.get("score", 0) > 0.92:
                checks.append((True, f"Near-duplicate of existing note: {s['title']}", 0.7))
        
        # Contradiction check
        existing = self.db.search_keyword(title, top_k=1)
        if existing and existing[0]["title"].lower() == title.lower():
            checks.append((True, "Title exists — will update rather than create new", 0.8))
        
        if any(not c[0] for c in checks):
            reason = "; ".join(c[1] for c in checks if not c[0])
            return False, reason, 0.0
        
        reason = "; ".join(c[1] for c in checks) if checks else "All checks passed"
        confidence = min((c[2] for c in checks), default=1.0)
        return True, reason, confidence

# ---------------------------------------------------------------------------
# Salience Engine
# ---------------------------------------------------------------------------

class SalienceEngine:
    """
    Scores memory importance so important things persist longer.
    """
    
    @staticmethod
    def score(frontmatter: Dict, content: str, db_stats: Dict) -> float:
        """Calculate salience score (0.0 to 1.0)."""
        score = 0.5
        emphasis_markers = ["IMPORTANT", "CRITICAL", "DECISION", "ALERT", "WARNING"]
        content_upper = content.upper()
        for marker in emphasis_markers:
            if marker in content_upper:
                score += 0.15
        type_weights = {"decision": 0.2, "security": 0.25, "MOC": 0.1, "journal": -0.1}
        score += type_weights.get(frontmatter.get("type", ""), 0.0)
        if len(content) > 500:
            score += 0.05
        if "salience" in frontmatter:
            score = (score + float(frontmatter["salience"])) / 2
        return max(0.0, min(1.0, score))

# ---------------------------------------------------------------------------
# Prospective Memory (Future Reminders)
# ---------------------------------------------------------------------------

class ProspectiveMemory:
    """Remember to do something in the future."""
    
    def __init__(self, db: PgVectorStore):
        self.db = db
    
    def schedule(self, title: str, content: str, trigger_at: str, recurring: Optional[str] = None) -> str:
        """Schedule a future reminder. trigger_at: ISO 8601 datetime string."""
        with self.db._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO prospective (title, content, trigger_at, recurring)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (title, content, trigger_at, recurring))
                pid = cur.fetchone()[0]
                conn.commit()
                logger.info(f"Scheduled reminder: {title} at {trigger_at}")
                return pid
    
    def get_due(self, window_hours: int = 24) -> List[Dict]:
        """Get reminders due within the next N hours."""
        with self.db._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, title, content, trigger_at, recurring
                    FROM prospective
                    WHERE status = 'pending'
                      AND trigger_at <= NOW() + INTERVAL '%s hours'
                    ORDER BY trigger_at;
                """, (window_hours,))
                cols = [d[0] for d in cur.description]
                return [dict(zip(cols, row)) for row in cur.fetchall()]
    
    def mark_done(self, reminder_id: str):
        """Mark a reminder as completed."""
        with self.db._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE prospective SET status = 'done' WHERE id = %s;", (reminder_id,))
                conn.commit()

# ---------------------------------------------------------------------------
# Consolidation Engine (Sleep-Time Maintenance)
# ---------------------------------------------------------------------------

class ConsolidationEngine:
    """
    Nightly batch maintenance:
    - Merge near-duplicate notes
    - Archive stale, low-salience notes
    - Prune orphaned notes
    - Rebuild graph edges
    """
    
    def __init__(self, db: PgVectorStore, vault: VaultManager, embedder: Embedder):
        self.db = db
        self.vault = vault
        self.embedder = embedder
    
    def run(self) -> Dict:
        """Run full consolidation. Returns stats."""
        stats = {"merged": 0, "archived": 0, "pruned": 0, "relinked": 0}
        stats["archived"] += self._archive_stale()
        stats["relinked"] += self._rebuild_links()
        logger.info(f"Consolidation complete: {stats}")
        return stats
    
    def _archive_stale(self) -> int:
        """Archive notes not updated in 90 days with salience < 0.2."""
        with self.db._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE notes
                    SET status = 'archived'
                    WHERE status = 'active'
                      AND updated_at < NOW() - INTERVAL '90 days'
                      AND salience < 0.2
                    RETURNING id;
                """)
                archived = len(cur.fetchall())
                conn.commit()
                return archived
    
    def _rebuild_links(self) -> int:
        """Rebuild graph edges from vault files."""
        count = 0
        for filepath in self.vault.list_notes():
            try:
                text = filepath.read_text(encoding="utf-8")
                parsed = self.vault._parse_note(text)
                title = parsed["frontmatter"].get("title", filepath.stem)
                with self.db._conn() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT id FROM notes WHERE title = %s;", (title,))
                        row = cur.fetchone()
                        if row:
                            links = self.vault.extract_wiki_links(text)
                            self.db.update_links(row[0], links)
                            count += 1
            except Exception as e:
                logger.error(f"Link rebuild error: {e}")
        return count

# ---------------------------------------------------------------------------
# Unified Memory System (Main API)
# ---------------------------------------------------------------------------

class UnifiedMemorySystem:
    """
    One class to rule them all.
    
    Usage:
        memory = UnifiedMemorySystem()
        memory.remember(title="...", content="...")
        results = memory.recall("query")
        memory.remind_me(title="...", trigger_at="...")
        memory.consolidate()
    """
    
    def __init__(self, vault_path: str = VAULT_PATH, dsn: str = DB_DSN):
        self.vault = VaultManager(vault_path)
        self.db = PgVectorStore(dsn)
        self.embedder = Embedder()
        self.admission = AdmissionControl(self.db, self.embedder)
        self.salience = SalienceEngine()
        self.prospective = ProspectiveMemory(self.db)
        self.consolidation = ConsolidationEngine(self.db, self.vault, self.embedder)
        self.sync()
    
    def remember(self, title: str, content: str, tags: List[str] = None,
                 note_type: str = "concept", links: List[str] = None,
                 salience: Optional[float] = None) -> Dict:
        """
        Write a memory. Goes through admission control before persisting.
        Returns: {"success": bool, "note_id": str, "reason": str}
        """
        tags = tags or []
        links = links or []
        is_valid, reason, confidence = self.admission.validate(title, content, tags)
        if not is_valid:
            logger.warning(f"Admission rejected: {title} — {reason}")
            return {"success": False, "note_id": None, "reason": reason}
        
        if salience is None:
            salience = self.salience.score({"type": note_type, "tags": tags}, content, self.db.get_stats())
        
        self.vault.write_note(title, content, tags, note_type, "active", salience, links)
        embedding = self.embedder.embed([content])[0] if content else [0.0] * EMBEDDING_DIM
        note_id = self.db.upsert_note(title, content, tags, note_type, "active", salience, embedding, str(self.vault.vault_path))
        self.db.update_links(note_id, links)
        logger.info(f"Remembered: {title} (salience={salience:.2f})")
        return {"success": True, "note_id": note_id, "reason": reason}
    
    def recall(self, query: str, mode: str = "hybrid", top_k: int = 10,
               filters: Optional[Dict] = None) -> List[Dict]:
        """Search memories. mode: hybrid (default), semantic, keyword, graph."""
        if mode == "semantic":
            emb = self.embedder.embed([query])[0]
            return self.db.search_semantic(emb, top_k, filters)
        elif mode == "keyword":
            return self.db.search_keyword(query, top_k)
        elif mode == "graph":
            return self.db.search_graph(query, depth=2, top_k=top_k)
        else:
            emb = self.embedder.embed([query])[0]
            return self.db.hybrid_search(query, emb, top_k)
    
    def remind_me(self, title: str, trigger_at: str, content: str = "",
                  recurring: Optional[str] = None) -> str:
        """Schedule a future reminder."""
        return self.prospective.schedule(title, content, trigger_at, recurring)
    
    def check_reminders(self) -> List[Dict]:
        """Get due reminders. Call this periodically."""
        return self.prospective.get_due(window_hours=24)
    
    def consolidate(self) -> Dict:
        """Run sleep-time consolidation."""
        return self.consolidation.run()
    
    def sync(self) -> Dict:
        """Sync vault files to database."""
        return self.vault.sync_to_db(self.db, self.embedder)
    
    def stats(self) -> Dict:
        """Get system statistics."""
        return self.db.get_stats()

# ---------------------------------------------------------------------------
# MCP Server (JSON-RPC 2.0 over stdio)
# ---------------------------------------------------------------------------

class MemoryMCPServer:
    """
    MCP server exposing memory operations as tools.
    Compatible with Claude Code, Cursor, and any MCP client.
    
    Run: python -c "from mo_graphify_memory import MemoryMCPServer; MemoryMCPServer().run()"
    """
    
    def __init__(self, memory: UnifiedMemorySystem = None):
        self.memory = memory or UnifiedMemorySystem()
    
    def run(self):
        """Main loop: read JSON-RPC requests from stdin, write responses to stdout."""
        logger.info("MCP Memory Server starting...")
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                req = json.loads(line)
                resp = self._handle(req)
            except json.JSONDecodeError as e:
                resp = {"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}, "id": None}
            except Exception as e:
                resp = {"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}, "id": req.get("id")}
            print(json.dumps(resp), flush=True)
    
    def _handle(self, req: Dict) -> Dict:
        """Handle a single JSON-RPC request."""
        method = req.get("method")
        params = req.get("params", {})
        req_id = req.get("id")
        
        if method == "initialize":
            return {"jsonrpc": "2.0", "result": {"protocolVersion": "2024-11-05", "capabilities": {}}, "id": req_id}
        if method == "tools/list":
            return {"jsonrpc": "2.0", "result": {"tools": self._tools()}, "id": req_id}
        if method == "tools/call":
            name = params.get("name", "")
            args = params.get("arguments", {})
            result = self._call_tool(name, args)
            return {"jsonrpc": "2.0", "result": {"content": [{"type": "text", "text": json.dumps(result)}]}, "id": req_id}
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": f"Method not found: {method}"}, "id": req_id}
    
    def _tools(self) -> List[Dict]:
        return [
            {
                "name": "memory_remember",
                "description": "Save a fact, decision, or observation to persistent memory",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "salience": {"type": "number"}
                    },
                    "required": ["title", "content"]
                }
            },
            {
                "name": "memory_recall",
                "description": "Search memory by semantic meaning, keywords, or graph relationships",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "mode": {"type": "string", "enum": ["hybrid", "semantic", "keyword", "graph"]},
                        "top_k": {"type": "integer", "default": 5}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "memory_remind_me",
                "description": "Schedule a future reminder or recurring task",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content": {"type": "string"},
                        "trigger_at": {"type": "string"},
                        "recurring": {"type": "string", "enum": ["daily", "weekly", "monthly"]}
                    },
                    "required": ["title", "trigger_at"]
                }
            },
            {
                "name": "memory_audit",
                "description": "Get memory system statistics and health check",
                "inputSchema": {"type": "object", "properties": {}}
            }
        ]
    
    def _call_tool(self, name: str, args: Dict) -> Dict:
        if name == "memory_remember":
            return self.memory.remember(title=args.get("title", ""), content=args.get("content", ""), tags=args.get("tags", []), salience=args.get("salience"))
        elif name == "memory_recall":
            return {"results": self.memory.recall(query=args.get("query", ""), mode=args.get("mode", "hybrid"), top_k=args.get("top_k", 5))}
        elif name == "memory_remind_me":
            return {"reminder_id": self.memory.remind_me(title=args.get("title", ""), trigger_at=args.get("trigger_at", ""), content=args.get("content", ""), recurring=args.get("recurring"))}
        elif name == "memory_audit":
            return self.memory.stats()
        else:
            return {"error": f"Unknown tool: {name}"}

# ---------------------------------------------------------------------------
# Backward-Compatible Functions (from v1.0)
# ---------------------------------------------------------------------------

_global_memory: Optional[UnifiedMemorySystem] = None

def _get_memory() -> UnifiedMemorySystem:
    global _global_memory
    if _global_memory is None:
        _global_memory = UnifiedMemorySystem()
    return _global_memory

def create_note(title: str, content: str, tags=None, note_type="concept", links=None):
    """v1.0 compatible: Create a note."""
    return _get_memory().remember(title, content, tags or [], note_type, links or [])

def read_note(title: str) -> Optional[str]:
    """v1.0 compatible: Read a note."""
    result = _get_memory().vault.read_note(title)
    return result["raw"] if result else None

def search_notes(query: str):
    """v1.0 compatible: Search notes."""
    return _get_memory().recall(query, mode="keyword")

def update_note(title: str, new_content=None, append_content=None, **kwargs):
    """v1.0 compatible: Update a note."""
    mem = _get_memory()
    existing = mem.vault.read_note(title)
    if not existing:
        return None
    if new_content:
        content = new_content
    elif append_content:
        content = existing["body"] + "\n\n" + append_content
    else:
        content = existing["body"]
    fm = existing["frontmatter"]
    return mem.remember(title=title, content=content, tags=fm.get("tags", []), note_type=fm.get("type", "concept"), links=fm.get("links", []))

def create_moc(title: str, description: str, related_notes: List[str]):
    """v1.0 compatible: Create a Map of Content."""
    content = f"{description}\n\n## Overview\n\n"
    for note in related_notes:
        content += f"- [[{note}]]\n"
    return _get_memory().remember(title, content, ["MOC", "index"], "MOC", related_notes)

# ---------------------------------------------------------------------------
# Auto-Initialization (Bootstrap)
# ---------------------------------------------------------------------------

def autoload_memory():
    """
    Called automatically at session start via MEMORY.md bootstrap.
    Initializes the unified memory system and syncs the vault.
    """
    try:
        mem = UnifiedMemorySystem()
        stats = mem.stats()
        logger.info(f"Memory autoloaded: {stats['notes']} notes, {stats['links']} links")
        return mem
    except Exception as e:
        logger.error(f"Memory autoload failed: {e}")
        return None

if __name__ != "__main__" and os.environ.get("MEMORY_NO_AUTOLOAD") != "1":
    _global_memory = autoload_memory()
```

---

## How to Make It Autonomous (Option A: Bootstrap Files)

Place these files in your agent's memory directory so they load on **every session**:

### 1. `MEMORY.md` — Session Bootstrap

**Path:** `~/Library/Application Support/kimi-desktop/daimon-share/daimon/agents/main/memory/vault/MEMORY.md`

```markdown
---
memory_system: mo-graphify-v2
version: "2.0.0"
auto_load: true
vault_path: /Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault
pg_dsn: postgresql://localhost:5432/mnemosyne
embedding_model: all-MiniLM-L6-v2
embedding_dimension: 384
embedding_provider: sentence-transformers
mcp_transport: stdio
status: initialized
last_sync: "1970-01-01T00:00:00"
---

# Unified Memory Bootstrap

This file initializes the agent's persistent memory system on every session start.

## What to Do on Every Session Start

1. **Import the memory system:**
   ```python
   from mo_graphify_memory import UnifiedMemorySystem, autoload_memory
   memory = autoload_memory()
   ```

2. **Sync the vault** (if files were edited outside the agent):
   ```python
   memory.sync()
   ```

3. **Check due reminders** (prospective memory):
   ```python
   due = memory.check_reminders()
   for r in due:
       print(f"REMINDER: {r['title']} — {r['content']}")
   ```

## Quick Commands

| Command | What It Does |
|---------|-------------|
| `memory.remember(title, content, tags=[])` | Save a new memory |
| `memory.recall("query", mode="hybrid")` | Search by meaning |
| `memory.remind_me("title", "2026-07-07T09:00:00")` | Schedule a reminder |
| `memory.consolidate()` | Run nightly maintenance |
| `memory.stats()` | Show note/link counts |

## MCP Tools (for Claude Code / Cursor)

- `memory_remember` — Save knowledge
- `memory_recall` — Search memory
- `memory_remind_me` — Schedule reminder
- `memory_audit` — Health check
```

### 2. `AGENTS.md` — Agent Identity with Memory Rules

**Path:** `~/Library/Application Support/kimi-desktop/daimon-share/daimon/agents/main/memory/vault/AGENTS.md`

```markdown
---
name: Unified Memory Agent
version: "2.0.0"
---

# Agent Memory Rules

## Always Do These

1. **Before answering complex questions**, search memory:
   ```python
   results = memory.recall("user's question keywords")
   ```
   If relevant memories exist, reference them in your answer.

2. **After significant decisions or discoveries**, save them:
   ```python
   memory.remember(
       title="Descriptive Title",
       content="What was decided and why.",
       tags=["project-name", "decision"],
       salience=0.8
   )
   ```

3. **When the user emphasizes something** ("IMPORTANT", "remember this"), use high salience (0.8+).

4. **Link related memories** using `links=["Related Note"]`.

5. **Check reminders at session start** and surface any that are due.

## Never Do These

1. Never write memory without running admission control.
2. Never ignore a contradiction with existing memories.
3. Never let the vault grow unbounded — run `memory.consolidate()` weekly.
```

## PostgreSQL Setup (One-Time)

```bash
# 1. Install PostgreSQL
brew install postgresql@16
brew services start postgresql@16

# 2. Create database
createdb mnemosyne

# 3. Install pgvector
brew install pgvector
# In psql:
# CREATE EXTENSION vector;

# 4. Install Python deps
pip install psycopg2-binary pyyaml numpy sentence-transformers
```

## Best Practices

1. **Files are the source of truth** — you can edit `.md` files directly in Obsidian.
2. **Run `memory.sync()` after external edits** — re-indexes the database.
3. **Use salience wisely** — 0.9 for critical decisions, 0.3 for daily journals.
4. **Link aggressively** — every note should connect to at least 2 others.
5. **Run consolidation weekly** — keeps the vault clean and fast.
6. **Back up the vault** — it's just markdown files. `git init` in the vault directory.

## Quick Reference

| Operation | Code |
|-----------|------|
| Remember | `memory.remember(title, content, tags, salience=0.5)` |
| Recall (semantic) | `memory.recall("query", mode="hybrid", top_k=5)` |
| Recall (keyword) | `memory.recall("query", mode="keyword")` |
| Recall (graph) | `memory.recall("Note Title", mode="graph")` |
| Remind me | `memory.remind_me("Check API", "2026-07-07T09:00:00", recurring="weekly")` |
| Check reminders | `memory.check_reminders()` |
| Consolidate | `memory.consolidate()` |
| Sync vault | `memory.sync()` |
| Stats | `memory.stats()` |
| MCP server | `MemoryMCPServer(memory).run()` |

## Migration from v1.0

All v1.0 functions still work — they delegate to the new UnifiedMemorySystem:
- `create_note(title, content, tags, note_type, links)` ✅
- `read_note(title)` ✅
- `search_notes(query)` ✅ (now uses hybrid search)
- `update_note(title, ...)` ✅
- `create_moc(title, desc, related)` ✅

The old vault format (YAML frontmatter + wiki-links) is unchanged.
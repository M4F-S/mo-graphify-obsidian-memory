# mo-graphify-obsidian-memory

> **Production-grade unified memory system for AI agents**
>
> Gives your AI agent a persistent brain: it can remember conversations, search memories by meaning, schedule future reminders, and protect itself from poisoned data. Everything is stored in plain markdown files you can read and edit in Obsidian, VS Code, or any text editor.

## What This Skill Does

| Feature | What It Means For You |
|---------|----------------------|
| **Markdown Vault** | All memories are plain `.md` files with YAML frontmatter. You own your data. |
| **Semantic Search** | Ask "what did we discuss about neural networks?" — it finds related ideas even if the exact words don't match. |
| **Graph Memory** | Notes link to each other via `[[Wiki Links]]`. The agent sees relationships, not isolated facts. |
| **Security Gate** | Bad data (prompt injection, contradictions, low-quality content) is caught before it poisons long-term memory. |
| **Salience Scoring** | Important memories (failures, user emphasis, contradictions) are weighted higher and persist longer. |
| **Prospective Memory** | The agent can set reminders: *"Check this again in 3 days"* — and actually surface them when due. |
| **Sleep Consolidation** | Nightly maintenance batch: archive stale notes, rebuild graph edges, merge duplicates. |
| **MCP Server** | Claude Code, Cursor, and any MCP client can read/write the agent's memory directly via JSON-RPC. |

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

- **PostgreSQL 14+** with [pgvector](https://github.com/pgvector/pgvector) extension
- **Python 3.9+**
- Python packages: `psycopg2-binary`, `pyyaml`, `numpy`
- *(Optional)* `sentence-transformers` for better local embeddings

### Quick PostgreSQL Setup (macOS)

```bash
brew install postgresql@16 pgvector
brew services start postgresql@16

# Create database
createdb mnemosyne

# Install pgvector in psql
psql mnemosyne -c "CREATE EXTENSION vector;"
```

## Installation

```bash
pip install psycopg2-binary pyyaml numpy sentence-transformers
```

Set environment variables *(or use defaults)*:

```bash
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

## Core Components

| Component | Responsibility |
|-----------|---------------|
| `UnifiedMemorySystem` | Main API — `remember()`, `recall()`, `remind_me()`, `consolidate()` |
| `PgVectorStore` | PostgreSQL + pgvector for semantic (cosine similarity), keyword (tsvector), and graph (recursive CTE) search |
| `VaultManager` | Obsidian-compatible markdown file I/O with YAML frontmatter |
| `Embedder` | 3-tier embedding: sentence-transformers → Ollama → deterministic hash fallback |
| `AdmissionControl` | Security gate: injection detection, near-duplicate check, length validation |
| `SalienceEngine` | Scores memory importance (0.0–1.0) based on emphasis markers, note type, and length |
| `ProspectiveMemory` | Scheduled future reminders with recurring support (daily/weekly/monthly) |
| `ConsolidationEngine` | Sleep-time batch: archive stale notes, rebuild links |
| `MemoryMCPServer` | JSON-RPC 2.0 MCP server exposing tools to external clients |

## MCP Tools

Compatible with Claude Code, Cursor, and any MCP stdio client:

- `memory_remember` — Save a fact or decision
- `memory_recall` — Search memory (hybrid, semantic, keyword, or graph)
- `memory_remind_me` — Schedule a reminder
- `memory_audit` — Health check and statistics

## Embedding Engine (3-Tier Fallback)

1. **sentence-transformers** — local, fast, no API calls
2. **Ollama** — local LLM server (`ollama pull nomic-embed-text`)
3. **Deterministic hash** — zero external dependencies, always works

## Search Modes

| Mode | Use When |
|------|----------|
| `hybrid` *(default)* | Best overall results; fuses semantic + keyword + salience via RRF |
| `semantic` | Finding related concepts even with different wording |
| `keyword` | Exact matches and specific terms |
| `graph` | Exploring connections from a known note (`[[Note Title]]`) |

## Best Practices

1. **Files are the source of truth** — you can edit `.md` files directly in Obsidian.
2. **Run `memory.sync()` after external edits** — re-indexes the database.
3. **Use salience wisely** — `0.9` for critical decisions, `0.3` for daily journals.
4. **Link aggressively** — every note should connect to at least 2 others via `[[Wiki Links]]`.
5. **Run consolidation weekly** — keeps the vault clean and fast.
6. **Back up the vault** — it's just markdown files. `git init` in the vault directory.

## Migration from v1.0

All v1.0 functions still work — they delegate to the new `UnifiedMemorySystem`:

- `create_note()` ✅
- `read_note()` ✅
- `search_notes()` ✅ *(now uses hybrid search)*
- `update_note()` ✅
- `create_moc()` ✅

The vault format (YAML frontmatter + wiki-links) is unchanged.

## License

MIT

---
name: mo-graphify-obsidian-memory
description: Graph-based knowledge memory system using Obsidian markdown vault files with wiki-links and graph visualizations. Triggered by graphify my knowledge, obsidian memory, unified memory, save to memory, remember this, knowledge graph, memory vault, prospective memory, memory search, consolidate memory, semantic search, graph traversal, salience scoring, admission control, MCP server.
---

# mo-Graphify + Obsidian Memory v2.0

Production-grade unified memory for AI agents. Remember conversations, search by meaning, schedule future reminders, and protect against poisoned data. All memories are plain `.md` files you can open in Obsidian or any text editor.

## What It Does

| Feature | What It Means |
|---------|-------------|
| **Markdown Vault** | Plain `.md` files with YAML frontmatter. Human-readable, Git-diffable, portable. |
| **Semantic Search** | Ask "what did we discuss about neural networks?" — finds related ideas even with different words. |
| **Graph Memory** | Notes link via `[[wiki-links]]`. Traverse relationships 2 hops deep. |
| **Security Gate** | Injection detection (MINJA/ADAM guard), near-duplicate check, contradiction flagging. |
| **Salience Scoring** | Important memories persist longer. Auto-calculated from emphasis markers + type. |
| **Prospective Memory** | "Remember to check this in 3 days" — and actually do it. |
| **Sleep Consolidation** | Nightly maintenance: archive stale, fix broken links, merge duplicates. |
| **MCP Server** | Claude Code, Cursor, and any MCP client can read/write memory directly. |

## Architecture

```
┌─────────────────────────────────────────────┐
│  Your Question                              │
│  "What did we decide about API rate limit?" │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  Unified Memory System                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │ Semantic │ │ Keyword  │ │  Graph   │     │
│  │ Search   │ │ Search   │ │ Search   │     │
│  │(pgvector)│ │(tsvector)│ │(wikilinks│     │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘     │
│       └────────────┬────────────┘             │
│                    │                          │
│            ┌───────▼────────┐               │
│            │ RRF Merge      │               │
│            └───────┬────────┘               │
│                    │                          │
│  ┌─────────────────▼──────────────────────┐  │
│  │ Markdown Vault (source of truth)     │  │
│  │ ~/Mnemosyne/obsidian-vault/*.md      │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

## Quick Start

```python
from mo_graphify_memory import UnifiedMemorySystem

memory = UnifiedMemorySystem()  # Auto-syncs vault to DB

# Save a memory
memory.remember(
    title="API Rate Limit Decision",
    content="100 req/min with burst to 200. Alert if p95 > 200ms.",
    tags=["api", "decision"],
    salience=0.9
)

# Search by meaning (not just keywords)
results = memory.recall("rate limiting policy", mode="hybrid", top_k=5)

# Schedule a future reminder
memory.remind_me("Review API metrics", "2026-07-07T09:00:00", recurring="weekly")

# Run nightly maintenance
memory.consolidate()
```

## API Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `remember(title, content, tags=[], salience=0.5)` | Save a memory | `memory.remember("Decision", "We chose X", salience=0.8)` |
| `recall(query, mode="hybrid", top_k=10)` | Search memory | `memory.recall("API rate limit")` |
| `remind_me(title, trigger_at, content="", recurring=None)` | Schedule reminder | `memory.remind_me("Check", "2026-07-07T09:00", recurring="weekly")` |
| `check_reminders()` | Get due reminders | `memory.check_reminders()` |
| `consolidate()` | Nightly maintenance | `memory.consolidate()` |
| `sync()` | Re-index vault files | `memory.sync()` |
| `stats()` | System health | `memory.stats()` |

## MCP Tools (for Claude Code / Cursor)

| Tool | Input | Output |
|------|-------|--------|
| `memory_remember` | title, content, tags, salience | {success, note_id, reason} |
| `memory_recall` | query, mode, top_k | ranked results with RRF score |
| `memory_remind_me` | title, trigger_at, content, recurring | {reminder_id} |
| `memory_audit` | (none) | {notes, links, pending, health} |

## Prerequisites

```bash
# PostgreSQL 16 + pgvector (Docker recommended)
docker run -d --name unified-memory-pg \
  -p 15432:5432 -e POSTGRES_USER=mnemosyne \
  -e POSTGRES_PASSWORD=mnemosyne_secret \
  -e POSTGRES_DB=mnemosyne \
  ankane/pgvector:latest

# Python dependencies
pip install psycopg2-binary pyyaml numpy sentence-transformers

# Environment variables
export MEMORY_DB_DSN="postgresql://mnemosyne:mnemosyne_secret@localhost:15432/mnemosyne"
export MEMORY_VAULT_PATH="$HOME/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"
```

## File Locations

| File | Purpose |
|------|---------|
| `scripts/mo_graphify_memory.py` | Full Python implementation (import this) |
| `~/Mnemosyne/obsidian-vault/` | Your notes (source of truth) |
| `~/.unified_memory_env` | Environment variables |
| `test_report.md` | 32/33 tests passed |

## Best Practices

1. **Files are the source of truth.** Edit `.md` files in Obsidian/VS Code. Run `memory.sync()` after external edits.
2. **Use salience wisely.** 0.9 for critical decisions, 0.3 for casual notes. Default 0.5.
3. **Link aggressively.** Every note should connect to at least 2 others via `[[wiki-links]]`.
4. **Run consolidation weekly.** Keeps the vault clean and fast.
5. **Back up the vault.** `git init` in the vault directory.

## Backward Compatibility (v1.0)

All v1.0 functions still work and delegate to UnifiedMemorySystem:

- `create_note(title, content, tags, note_type, links)` → `memory.remember()`
- `read_note(title)` → reads from vault
- `search_notes(query)` → `memory.recall(mode="keyword")`
- `update_note(title, ...)` → updates with admission control
- `create_moc(title, desc, related)` → creates Map of Content with salience

The vault format (YAML frontmatter + wiki-links) is unchanged.

## More Info

- **Research Report**: `memory_stack.docx` (40,000 words, 56 citations)
- **GitHub**: https://github.com/M4F-S/mo-graphify-obsidian-memory
- **Setup Guide**: `SETUP.md` in repo
- **Platform Brief**: `PLATFORM_BUILDER_BRIEF.md` in repo

## Implementation

The full Python implementation is in `scripts/mo_graphify_memory.py` (~1,200 lines). Import it to use the system:

```python
import sys
sys.path.insert(0, "/path/to/this/skill/scripts")
from mo_graphify_memory import UnifiedMemorySystem, MemoryMCPServer, autoload_memory
```

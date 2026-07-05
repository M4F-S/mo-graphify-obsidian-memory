# Unified Memory v2.0 — Setup Guide

This guide walks you through installing and running the production-grade unified memory system for AI agents.

## What Was Installed

| Component | Technology | Status |
|-----------|-----------|--------|
| Database | PostgreSQL 16 + pgvector (Docker) | ✅ Running on port 15432 |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) | ✅ Using Apple MPS |
| Python API | UnifiedMemorySystem | ✅ 9 notes indexed, 5 links |
| Vault | Obsidian markdown files | ✅ 10 files in `~/Mnemosyne/obsidian-vault/` |
| MCP Server | JSON-RPC 2.0 over stdio | ✅ Ready |

## Quick Start (Already Done)

```bash
# The database is already running
docker ps --filter name=unified-memory-pg

# Environment variables are set
export MEMORY_DB_DSN="postgresql://mnemosyne:mnemosyne_secret@localhost:15432/mnemosyne"
export MEMORY_VAULT_PATH="/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"

# Use it in Python
python3 -c "
from mo_graphify_memory import UnifiedMemorySystem
memory = UnifiedMemorySystem()
print(memory.stats())
"
```

## Docker Management

```bash
# View logs
docker logs unified-memory-pg

# Stop
docker stop unified-memory-pg

# Start
docker start unified-memory-pg

# Remove everything (WARNING: deletes all data)
docker rm -f unified-memory-pg
docker volume rm unified-memory-pg-data
```

## Connecting Other Agents

### Claude Code

Add to `claude_mcp_settings.json`:

```json
{
  "mcpServers": {
    "unified-memory": {
      "command": "python3",
      "args": [
        "-c",
        "import sys; sys.path.insert(0, '/Users/mohamedfathy/Documents/Kimi/Workspaces/Memory'); from mo_graphify_memory import MemoryMCPServer; MemoryMCPServer().run()"
      ],
      "env": {
        "MEMORY_DB_DSN": "postgresql://mnemosyne:mnemosyne_secret@localhost:15432/mnemosyne",
        "MEMORY_VAULT_PATH": "/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"
      }
    }
  }
}
```

### Hermes (HTTP REST)

Hermes requires HTTP REST. A wrapper is needed:

```python
# TODO: Add FastAPI/Flask HTTP wrapper for Hermes compatibility
# from mo_graphify_memory import create_rest_app
# app = create_rest_app(memory)
# app.run(host="0.0.0.0", port=8080)
```

## File Locations

| File | Path |
|------|------|
| Skill | `~/Library/.../skills/mo-graphify-obsidian-memory/SKILL.md` |
| Python module | `~/Documents/Kimi/Workspaces/Memory/mo_graphify_memory.py` |
| Vault (your notes) | `~/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault/` |
| Bootstrap | `~/Library/.../agents/main/memory/vault/MEMORY.md` |
| Agent rules | `~/Library/.../agents/main/memory/vault/AGENTS.md` |
| Setup script | `~/Documents/Kimi/Workspaces/Memory/setup_unified_memory.py` |

## Verification

Run the test script:

```bash
cd ~/Documents/Kimi/Workspaces/Memory
python3 run_migration.py
```

Expected output:
```
Notes: 9, Links: 5, Reminders: 0
Test write: PASS
Test search: PASS
Test stats: PASS
Test reminder: PASS
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `psycopg2 not found` | `pip3 install psycopg2-binary` |
| `sentence-transformers not found` | `pip3 install sentence-transformers` |
| Docker not running | Start Docker Desktop |
| Port 15432 in use | Change `DB_PORT` in setup script |
| Database connection refused | `docker start unified-memory-pg` |

## Next Steps

1. **Install Obsidian** (optional) to browse your vault visually
2. **Set up `.kimi/AGENTS.md`** in project directories for universal instructions
3. **Run `memory.consolidate()` weekly** via cron job
4. **Back up your vault** with `git init` in the vault directory

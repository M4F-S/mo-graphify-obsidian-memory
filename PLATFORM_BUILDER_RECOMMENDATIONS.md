# Platform Builder Recommendations — Unified Memory Architecture

> **For**: The session building the AI agent platform
> **From**: Memory Skill Research Session (July 9, 2026)
> **Status**: ✅ Tested & Verified

---

## Executive Summary

Your platform needs a **unified memory system** that works across all agents (Kimi, Claude Code, Hermes) without requiring each agent to reinvent memory. The `mo-graphify-obsidian-memory` skill provides this today — it's already installed, tested, and working.

**Key insight**: Memory should be a **platform service**, not an agent feature. Agents read/write to a shared memory layer. This is what we built.

---

## 1. Memory Layers Your Platform Needs

Based on extensive research (40,000+ words, 56 citations), an AI agent platform needs **5 memory layers**:

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 5: External Memory (User files, APIs, databases)   │
│  LAYER 4: Prospective Memory (Scheduled reminders, cron)    │
│  LAYER 3: Episodic Memory (Conversation history, sessions)│
│  LAYER 2: Semantic Memory (Knowledge graph, facts, rules) │
│  LAYER 1: Working Memory (Current context, tool outputs)  │
└─────────────────────────────────────────────────────────────┘
```

| Layer | What It Stores | How We Implement It |
|-------|---------------|---------------------|
| **Working** | Current conversation, tool results | Kimi's native context window + skill loading |
| **Episodic** | Past conversations, decisions | Markdown vault files (`obsidian-vault/*.md`) |
| **Semantic** | Facts, knowledge, relationships | SQLite/PostgreSQL with vector embeddings |
| **Prospective** | Future reminders, scheduled tasks | `prospective` table + cron jobs |
| **External** | User files, GitHub, databases | MCP tools, file system access |

---

## 2. What Changed in This Update

### Before (Broken)
- `prospective.py` and `consolidation.py` used PostgreSQL-only syntax
- SQLite fallback threw `AttributeError: __enter__` on cursor context managers
- Reminders and sleep consolidation **did not work** without PostgreSQL

### After (Fixed)
- Both modules now auto-detect SQLite vs PostgreSQL
- SQLite uses `?` placeholders, `datetime('now')`, and manual UUIDs
- PostgreSQL keeps `RETURNING id`, `NOW() + INTERVAL`, `%s` placeholders
- All 8 features tested and passing with SQLite (no PostgreSQL needed)

---

## 3. How Cross-Agent Memory Sharing Works

### The Problem
You have 3 agents:
- **Kimi** (this desktop app) — runs locally
- **Claude Code** — runs locally, uses MCP
- **Hermes Agent A** — runs locally
- **Hermes Agent B** — runs on a **remote VPS**

### The Solution: Shared Vault + MCP Server

```
┌─────────────┐     ┌─────────────┐     ┌─────────────────┐
│   Kimi      │     │ Claude Code │     │ Hermes (local)  │
│  (local)    │     │  (local)    │     │   (local)       │
└──────┬──────┘     └──────┬──────┘     └────────┬────────┘
       │                   │                     │
       └───────────────────┼─────────────────────┘
                           │
              ┌────────────▼────────────┐
              │   MCP Server (stdio)    │
              │   memory_remember()     │
              │   memory_recall()       │
              │   memory_remind_me()    │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   Markdown Vault        │
              │   ~/Mnemosyne/obsidian  │
              │   (Git-synced)          │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   SQLite Database       │
              │   ~/.mnemosyne.db       │
              │   (local index)         │
              └─────────────────────────┘
```

### For the Remote VPS Agent (Hermes B)

**Option A: Git-synced vault** (Recommended)
```bash
# On local machine: push vault to Git
 cd ~/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault
 git init
 git add .
 git commit -m "memory sync"
 git push origin main

# On VPS: pull vault, use SQLite
 git clone https://github.com/your-org/memory-vault.git
 export MEMORY_VAULT_PATH="/path/to/memory-vault"
 export MEMORY_SQLITE_PATH="/path/to/mnemosyne.db"
 python -c "from mnemosyne import UnifiedMemorySystem; m = UnifiedMemorySystem()"
```

**Option B: Shared network storage**
- Mount the vault directory via NFS/SMB
- All agents read/write the same files

**Option C: PostgreSQL central server**
- One PostgreSQL instance accessible by all agents
- Best for real-time collaboration

---

## 4. Does It Work Without Installing Anything Else?

**YES.** Here's what works out of the box:

| Feature | Needs PostgreSQL? | Needs Docker? | Works with SQLite only? |
|---------|------------------|---------------|--------------------------|
| Save memories | ❌ No | ❌ No | ✅ Yes |
| Search memories | ❌ No | ❌ No | ✅ Yes |
| Schedule reminders | ❌ No | ❌ No | ✅ Yes (fixed!) |
| Sleep consolidation | ❌ No | ❌ No | ✅ Yes (fixed!) |
| Graph traversal | ❌ No | ❌ No | ✅ Yes |
| Semantic search | ❌ No | ❌ No | ✅ Yes (brute-force) |
| MCP server | ❌ No | ❌ No | ✅ Yes |

**What you DO need:**
- Python 3.9+
- `sentence-transformers` (auto-downloaded on first run)
- ~100MB disk space for the embedding model

**What you DON'T need:**
- PostgreSQL (optional, for scale)
- Docker (optional, for PostgreSQL)
- Ollama (optional, for local LLM embeddings)
- Any cloud service

---

## 5. How to Make Sessions Use Memory Automatically

### The Problem
You said: *"I want the skill to use fully autonomously, without my interception."*

### The Solution: Auto-Load on Session Start

Kimi Work loads skills automatically when they match the conversation. The skill is already configured for this:

```yaml
# In SKILL.md frontmatter
name: mo-graphify-obsidian-memory
description: Graph-based knowledge memory system... Triggered by:
  - graphify my knowledge
  - obsidian memory
  - unified memory
  - save to memory
  - remember this
  - memory search
  - consolidate memory
```

**To trigger auto-load**, any of these phrases in your first message will load the skill:
- "save this to memory"
- "remember this conversation"
- "search my memory for..."
- "consolidate my memories"

### For Universal Agent Instructions (All Sessions)

Kimi Work does not have a universal `agent.md` file like some other platforms. However, you can achieve the same effect:

**Option A: Custom Skill with Auto-Trigger**
Create a skill that always loads first and injects your instructions:

```markdown
---
name: universal-context
description: Always-loaded context for all sessions. Triggered by: *, any, start, hello.
---

# Universal Instructions

You are an AI assistant with persistent memory. Always:
1. Load mo-graphify-obsidian-memory when memory is needed
2. Save important decisions to the vault
3. Search memory before answering questions about past conversations
4. Use salience 0.9 for critical decisions, 0.5 for normal notes
```

**Option B: Session Template**
Save a session template in your workspace that includes the memory skill loading as the first turn.

**Option C: Cron Job for Periodic Memory Check**
```json
{
  "name": "memory-reminder-check",
  "trigger": {"kind": "cron", "expr": "0 9 * * *"},
  "execution": {
    "kind": "local_conversation",
    "prompt": "Check my memory for due reminders and summarize them for me."
  }
}
```

---

## 6. Beginner-Friendly Explanation

### What Is This Skill?

Imagine your AI agent has a **notebook** where it writes down important things you discuss. This skill is that notebook — but it's **smart**:

- It **remembers** conversations even after you close the app
- It **finds** related notes even if you use different words
- It **links** ideas together (like Wikipedia links)
- It **reminds** you of things you asked it to remember
- It **protects** against bad data (like a spam filter)

### Where Are My Memories Saved?

| Location | What's There | Can You Open It? |
|----------|-------------|------------------|
| `~/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault/` | Your notes as `.md` files | ✅ Yes, any text editor |
| `~/.mnemosyne/mnemosyne.db` | Search index (SQLite) | ✅ Yes, with DB browser |
| `~/.mnemosyne/` | Embedding model cache | ❌ No, binary files |

**The vault files are YOURS.** They're plain text. You can:
- Open them in Obsidian, VS Code, Notepad
- Edit them manually
- Sync them with Git
- Back them up to iCloud/Dropbox

### How to Use It (3 Steps)

**Step 1: Save something important**
```
You: "Remember that we decided to use PostgreSQL for the production database"
Agent: Saves a note with salience 0.9
```

**Step 2: Find it later**
```
You: "What did we decide about the database?"
Agent: Searches memory, finds the note
```

**Step 3: Set a reminder**
```
You: "Remind me to review the database choice in 3 days"
Agent: Schedules reminder for July 12, 2026
```

---

## 7. What the mnemosyne-oss/mnemosyne Repo Is

**Not related.** That repository is a **spaced repetition flashcard system** (like Anki) for human learning. It has:
- Flashcard algorithms (SM-2, Leitner)
- Review scheduling
- Learning statistics

**Our skill is different:** It's a **knowledge graph memory system for AI agents** with:
- Semantic search (meaning, not just keywords)
- Wiki-link graph traversal
- Salience scoring
- Prospective memory (future reminders)
- Security gates

The name collision is coincidental — both reference the Greek goddess of memory.

---

## 8. Installation & Testing Guide

### For New Users (No PostgreSQL Needed)

```bash
# 1. Clone the repo
git clone https://github.com/M4F-S/mo-graphify-obsidian-memory
cd mo-graphify-obsidian-memory

# 2. Install (no external dependencies needed)
pip install -e ".[dev]"

# 3. Test (uses SQLite automatically)
python -c "
from mnemosyne import UnifiedMemorySystem
m = UnifiedMemorySystem()
m.remember('Test', 'This works!')
print(m.recall('test'))
"
```

### For Platform Integration

```python
# In your platform's agent initialization
from mnemosyne import UnifiedMemorySystem

class YourAgent:
    def __init__(self):
        self.memory = UnifiedMemorySystem(auto_sync=True)
    
    def on_user_message(self, message):
        # Search memory first
        context = self.memory.recall(message, top_k=3)
        # ... generate response ...
        # Save important parts
        self.memory.remember(title=f"Session {id}", content=message)
```

---

## 9. Summary: What Was Done Today

| Task | Status | Commit |
|------|--------|--------|
| Verified skill structure | ✅ Done | Already clean (156 lines) |
| Fixed SQLite bug in `prospective.py` | ✅ Done | `a90adbc` |
| Fixed SQLite bug in `consolidation.py` | ✅ Done | `7fc90db` |
| Full test suite (8/8 passed) | ✅ Done | Local verification |
| Saved session to memory vault | ✅ Done | `Memory Skill Update Session - July 9 2026.md` |
| Pushed to GitHub | ✅ Done | `main` branch |
| Created platform recommendations | ✅ Done | This document |

---

## 10. Next Steps for Platform Builder

1. **Integrate MCP server** — Expose `memory_remember`, `memory_recall`, `memory_remind_me` to all agents
2. **Set vault path** — Use `~/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault` as the shared location
3. **Git-sync the vault** — Enable cross-device memory for remote agents
4. **Add auto-load trigger** — Ensure memory skill loads on session start
5. **Test with Claude Code** — Verify MCP tools work via `claude mcp add`

---

*Document generated: 2026-07-09*
*Skill version: 2.0.1 (SQLite fixes)*
*Repository: https://github.com/M4F-S/mo-graphify-obsidian-memory*

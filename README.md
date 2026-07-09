# ⚠️ DEPRECATED — Moved to New Repositories

This repository has been **split into two focused repositories** for better organization:

## 🧠 Mnemosyne Platform (Full Project)
**Research, architecture, build plans, infrastructure**

→ **https://github.com/M4F-S/mnemosyne**

Contains:
- Research documents and competitive analysis
- Architecture and design decisions
- V3 rebuild plan and strategic decisions
- Docker, Makefile, CI/CD infrastructure
- Platform builder brief and setup guides

## 🔌 Kimi Mnemosyne Skill (Minimal Skill)
**Kimi AI integration — clean, installable, focused**

→ **https://github.com/M4F-S/kimi-mnemosyne-skill**

Contains:
- `SKILL.md` — Kimi skill definition
- `mnemosyne/` — Python package (core, vault, embedder, security, MCP server, stores)
- `tests/` — Full test suite
- `pyproject.toml` — Package configuration

---

## Why the Split?

The original repo mixed **skill files** (for Kimi AI integration) with **platform files** (research, docs, infrastructure). This made it confusing for users who just wanted the skill vs. those who wanted the full platform.

**Now:**
- Developers who want to **use memory in Kimi** → `kimi-mnemosyne-skill`
- Developers who want to **contribute to the platform** → `mnemosyne`

---

## Original Description

> Production-grade unified memory system for AI agents. Gives your AI agent a persistent brain: it can remember conversations, search memories by meaning, schedule future reminders, and protect itself from poisoned data. Everything is stored in plain markdown files you can read and edit in Obsidian, VS Code, or any text editor.

This functionality now lives in the two repositories linked above.

---

*Last updated: July 9, 2026*

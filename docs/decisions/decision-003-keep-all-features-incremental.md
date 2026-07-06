---
title: "Decision: Keep All Features, Build Incrementally"
date: 2026-07-06
tags: [decision, architecture, features, incremental]
type: decision
salience: 0.9
links: []
---

# Decision: Keep All Features, Build Incrementally

## Context

The user stated: "I want to keep all but we can start small and add features along the way, as much as we can code."

The audit recommended cutting 70% of features. The user rejected this and wants to keep the full vision but build incrementally.

## Decision

We ACCEPT the user's decision to keep all features. The implementation strategy is:

1. **Core features are already built** (15 features in `mo_graphify_memory.py`):
   - Remember, recall, semantic search, keyword search, graph search, hybrid RRF
   - Markdown vault, YAML frontmatter, wiki-links
   - Admission control, salience scoring, prospective memory, consolidation
   - MCP server, backward compatibility

2. **Phase 0-2 makes the core shippable** (restructure, SQLite, MCP v2)

3. **Later phases add new features** (connectors, viz, dashboard, etc.)

4. **The architecture is designed to accommodate all features** without rewriting

## Feature Inventory

### Already Built (in `mo_graphify_memory.py`)

| Feature | Status | File |
|---------|--------|------|
| Remember/Recall | ✅ | `mo_graphify_memory.py` |
| Semantic Search | ✅ | `mo_graphify_memory.py` |
| Keyword Search | ✅ | `mo_graphify_memory.py` |
| Graph Search | ✅ | `mo_graphify_memory.py` |
| Hybrid RRF | ✅ | `mo_graphify_memory.py` |
| Markdown Vault | ✅ | `mo_graphify_memory.py` |
| YAML Frontmatter | ✅ | `mo_graphify_memory.py` |
| Wiki-Links | ✅ | `mo_graphify_memory.py` |
| Admission Control | ✅ | `mo_graphify_memory.py` |
| Salience Scoring | ✅ | `mo_graphify_memory.py` |
| Prospective Memory | ✅ | `mo_graphify_memory.py` |
| Consolidation | ✅ | `mo_graphify_memory.py` |
| MCP Server | ✅ | `mo_graphify_memory.py` |
| Backward Compat | ✅ | `mo_graphify_memory.py` |
| 3-Tier Embedder | ✅ | `mo_graphify_memory.py` |

### To Be Added (phased)

| Feature | Phase | Effort |
|---------|-------|--------|
| SQLite Fallback | Phase 1 | 3 days |
| MCP v2 (stateless) | Phase 2 | 3 days |
| CLI Tool | Phase 3 | 3 days |
| VPS Deploy | Phase 4 | 3 days |
| GitHub Connector | Phase 6 | 3 days |
| Slack Connector | Phase 6 | 3 days |
| File Import | Phase 6 | 2 days |
| Graph Visualization | Phase 7 | 3 days |
| Web Dashboard | Phase 7 | 1 week |
| Emotional Salience v2 | Phase 7 | 2 days |
| Memory Versioning | Phase 7 | 1 week |
| Plugin System | Phase 7 | 2 weeks |
| Browser Extension | Phase 7 | 2 weeks |
| VS Code Extension | Phase 7 | 2 weeks |
| Mobile App | Phase 7 | 1 month |
| Plugin Marketplace | Year 2 | 3 months |
| SOC 2 | Year 2 | 3 months |
| EU AI Act | Year 2 | 3 months |
| TEE Integration | Year 2 | 2 months |
| Differential Privacy | Year 2 | 2 months |

## Rationale

The user is the decision-maker. They want to keep the full vision. Our job is to make it implementable by breaking it into phases. The core is already built - we're packaging and extending, not rewriting.

## Consequences

- Positive: Full vision preserved, each phase adds value
- Negative: Longer timeline, more complexity, risk of never finishing
- Mitigation: Phase 0-2 is the MVP - if we stop there, we still have a working product

## Status: ACCEPTED

## Date: 2026-07-06

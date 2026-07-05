# Cognee Deep Research Report
## AI Memory Platform — Hackathon Intelligence Brief

**Research Date:** 2026-06-30  
**Researcher:** Mnemosyne Research Agent  
**Purpose:** Understand what Cognee wants from hackathon participants and what would impress them most

---

## 1. Executive Summary: What Cognee Wants to See

Cognee is an **open-source AI memory platform** (Berlin-based, €7.5M seed round led by Pebblebed, with angels from OpenAI and FAIR) that transforms raw unstructured data into a **self-improving knowledge graph** for AI agents. Their core mission is solving "AI amnesia" — the stateless nature of LLMs that causes agents to forget everything between sessions.

### Primary Value Proposition Cognee Wants Demonstrated:

> **"A Company Brain that gets smarter the more it is used."**

This is NOT a RAG demo. It is NOT a chatbot with memory. Cognee wants to see projects that demonstrate:
1. **Ingestion** of scattered company knowledge (docs, Slack, tickets, code, meeting notes)
2. **Query + Self-improvement** — the brain answers questions AND uses feedback from each query to grow and refine itself
3. **Lint** — deduplication, conflict resolution, pruning of stale entries

The key phrase is: **"a brain that gets smarter the more it is used."**

---

## 2. Cognee's Architecture & Core Concepts (What Judges Will Look For)

### The Four-Step Pipeline (Cognee's "API"):

```python
import cognee

await cognee.add("your document here")      # Ingest 38+ formats
await cognee.cognify()                       # Build knowledge graph (extract entities, relationships, triplets)
await cognee.memify()                        # Self-improve: prune stale, reweight edges, add derived facts
results = await cognee.search("your query")  # Hybrid graph + vector retrieval
```

### The Two-Tier Memory Model (CRITICAL for hackathons):

```
[ agent / user ]
       │
       ▼
┌─────────────────────────────────────────────┐
│           Your cognee instance                │
│   (local by default · Cognee Cloud optional) │
│                                             │
│   ┌─────────────────────────────────────┐  │
│   │  session memory (session_id=...)     │  │  ← fast, ephemeral, per-conversation
│   │  working scratchpad, recent turns    │  │
│   └──────────────────┬──────────────────┘  │
│                      │  distillation        │
│                      ▼                    │
│   ┌─────────────────────────────────────┐  │
│   │  permanent graph (no session_id)     │  │  ← structured, durable, cross-session
│   │  knowledge graph, embeddings, skills │  │
│   └─────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

**What this means for your hackathon project:** The "distillation" step — what gets promoted from session memory into the permanent graph, and how feedback rewrites it — is the CORE of what judges will evaluate. This is the "self-improvement loop."

### 14 Retrieval Modes:
Cognee supports RAG_COMPLETION, GRAPH_COMPLETION, FEEDBACK, AGENTIC_COMPLETION, NEIGHBORHOOD, CENTRALITY, and more. Using multiple retrieval modes in a single project demonstrates deep understanding.

---

## 3. What Features Cognee is Actively Promoting & Seeking Feedback On

### A. Cognee Cloud (Managed Service) — HIGH PRIORITY
- Launched in beta ~July 2025, now a major focus area
- Pricing: Free tier → top-up packs ($35/1K docs, $100/3K docs, $750/15K docs) → enterprise plans
- **Hackathon bonus:** "Best use of Cognee Cloud" is explicitly rewarded
- They provide dedicated Cloud instances + API keys at kickoff
- `cognee.serve(url=..., api_key=...)` connects your local brain to the cloud
- `cognee.push("dataset")` uploads a locally-built brain to Cloud

### B. MCP (Model Context Protocol) Server — HIGH PRIORITY
- Cognee ships a **first-party, standalone MCP server**
- Works with Claude Code, Cursor, Cline, VS Code Copilot, Windsurf, Continue Dev, Codex, etc.
- This is a DIFFERENTIATOR — Mem0 and Zep have "limited" or "community" MCP support
- **Hackathon angle:** Building an MCP-native workflow that lets an agent read/write Cognee memory via tools is highly impressive

### C. Self-Improvement / Memify Loop — THEIR CORE DIFFERENTIATOR
- The `memify()` layer prunes stale nodes, strengthens frequent connections, reweights edges based on usage/feedback
- **Skills system:** Markdown SKILL.md files that agents use, score, and then propose rewrites for
- The two-step propose-then-apply cycle is what "self-improvement" means in Cognee's vocabulary

### D. Multi-User / Tenant Isolation — ENTERPRISE FOCUS
- `enable_access_control()`, per-user datasets, explicit sharing via `share_dataset()`
- Recent PRs show heavy work on auth (JWKS, asymmetric tokens)
- **Hackathon angle:** Demonstrating two users with private brains + one sharing a brain is a powerful demo

### E. New Backends & Adapters — COMMUNITY CONTRIBUTION OPPORTUNITY
- Turso/libSQL as relational backend (PR #3582)
- Turso vector backend (PR #3594)
- Pinecone vector adapter (open issue #1444)
- Advanced PDF loader with unstructured library (open PR #1445)
- S3-compatible object storage (issue #1480, closed)

---

## 4. Most Important Integrations (What Cognee Highlights)

From docs.cognee.ai/integrations, Cognee's official integration page lists these in priority order:

### Agent Frameworks (Native Support):
| Integration | Status | Notes |
|-------------|--------|-------|
| **Claude Code** | First-party | Native MCP server tools |
| **n8n** | First-party | No-code memory workflows |
| **OpenClaw** | First-party | Auto-index and recall for personal AI agent |
| **LangGraph** | Native | Works with `create_react_agent` |
| **OpenAI Agents SDK** | Native | `function_tool` pattern with handoffs |
| **Google ADK** | Native | `LongRunningFunctionTool` for async Gemini agents |
| **CrewAI** | Native | Used in their winning Weaviate hackathon demo |

### Agent IDEs & Development Tools:
| Tool | Integration |
|------|-------------|
| Cursor | MCP |
| VS Code Copilot | MCP |
| Cline | MCP |
| Continue Dev | MCP |
| Windsurf | MCP |
| Codex | MCP |

### Data Ingestion:
| Source | Notes |
|--------|-------|
| ScrapeGraphAI | Web scraping → knowledge graph |
| 38+ formats | PDF, CSV, JSON, audio, images, code, SQL, APIs |

### Observability:
| Tool | Purpose |
|------|---------|
| OpenTelemetry | Vendor-neutral tracing |
| Keywords AI | LLM app tracing |
| DeepEval | RAG evaluation metrics |

**Hackathon insight:** A project that uses **Claude Code + Cognee MCP + n8n automation** as a three-layer stack would be extremely impressive to Cognee judges. It demonstrates their ecosystem vision.

---

## 5. Founder Vision: What Vasilije Markovic Cares About

### Background:
- From the Balkans, based in Berlin for 10 years
- Former big data consultant (data warehouses, batch/streaming)
- Went back to university to study **cognitive sciences and clinical psychology**
- Cognee is built from **first principles using cognitive science + knowledge engineering**

### Key Quotes from Interviews:

> "AI systems fail not because they lack processing power, but because they are fundamentally unable to remember."

> "I based my first prototype on this concept in psycholinguistics called **multilayer models of language**. We as humans store words, phrases, sentences in different layers of memory — and all of these layers are cross-connected."

> "I feel that there is a problem with unrealistic expectations... these agents, once they start going off rails, they're compounding the error, and that error compounding needs to get stopped somehow."

> "We have these n8n workflows and release notes to Discord, to here, to there... adding Cognee on local devices so you can effectively just send all that to the cloud memory."

> "I approach it where I'm learning how to learn always. So if I don't know how to do a thing and I'm prompting, I'm also prompting it to also ask me questions back."

### What This Means for Hackathon Projects:
- **Cognitive science grounding** matters — don't just build a database with embeddings. Think about how human memory works (working memory vs. long-term memory, episodic vs. semantic)
- **Error compounding** is a concern — show how your brain prevents agents from going off rails
- **Human-in-the-loop** is valued — the propose-then-apply skill improvement pattern
- **Multi-layer memory** is the architecture — session + permanent graph with distillation between them

---

## 6. Competitive Landscape: What Makes Cognee Different

### The Competitors:

| System | Architecture | Best For | Cognee's Advantage |
|--------|-------------|----------|-------------------|
| **Mem0** | Vector + graph + KV | Personalization, chatbots | Cognee has native graph-FIRST architecture, not bolted-on |
| **Zep / Graphiti** | Temporal knowledge graph | Time-aware queries ("who owned this in Feb?") | Cognee has broader scope + 38+ ingestion sources |
| **Letta (MemGPT)** | Tiered RAM/disk | Long-horizon autonomous agents | Cognee has graph reasoning + multi-source ingestion |
| **LangMem** | LangGraph-native vector | LangGraph users | Cognee works across ALL frameworks + has graph |
| **Cloudflare Agent Memory** | Typed (Facts/Events/Tasks) | Cloudflare teams | Cognee is open-source + self-hostable |
| **Graphiti** | Temporal KG (Neo4j) | Time-aware memory | Cognee is a full control plane, not just a library |

### Cognee's Unique Selling Points (from their own evaluation rubric):

1. **Graph-native architecture** (20% weight) — ONLY Cognee was designed graph-first from scratch
2. **Native MCP server** (15% weight) — first-party, standalone, not community wrapper
3. **Open-source + self-hostable** (15% weight) — Apache 2.0, full feature set available
4. **Hybrid retrieval** (15% weight) — graph traversal + vector similarity simultaneously
5. **Multi-source ingestion** (10% weight) — 38+ sources vs. competitors' limited sets
6. **Self-improvement / memify** (10% weight) — memory that sharpens over time
7. **Production performance** (10% weight) — 1M+ pipelines/month, 70+ companies
8. **Developer experience** (5% weight) — broad integration surface

### Benchmark Claims:
- ~90% accuracy on graph-enhanced queries vs. ~60% for plain RAG (HotPotQA multi-hop)
- 1 GB processed in ~40 minutes using 100+ containers
- ~1M pipelines running monthly across 70+ companies

---

## 7. Cognee Cloud: Pricing & What's Different from Self-Hosted

### Pricing Tiers:

| Tier | Cost | Features |
|------|------|----------|
| **Free / Open Source** | $0 | Self-hosted, full features, local SQLite+LanceDB+Kuzu |
| **Cognee Cloud (Beta)** | $25/month during beta | Managed instance, no infra setup |
| **Top-up Packs** | $35 (1K docs / ~1GB) | Add capacity to free tier |
| **Top-up Packs** | $100 (3K docs / ~3GB) | |
| **Top-up Packs** | $750 (15K docs / ~15GB) | |
| **Enterprise On-Prem** | $3,500/month | Support + architecture review |

### What's Different from Self-Hosted:
- **No infrastructure management** — no Docker, no database setup
- **Cloud-only features** — `cognee.serve()`, `cognee.push()`, `cognee.pull()`
- **Session + permanent graph in one managed instance**
- **Background sync** between local changes and server index
- **Team sharing** via Cloud URLs + API keys
- **UI at localhost:3000** (local server) vs. cloud-hosted dashboard

---

## 8. Recent GitHub Activity: What They're Building Now

### Repository Stats (as of June 2026):
- **Stars:** ~24.8K (growing fast — was ~17.9K in July 2025)
- **Forks:** ~2.3K
- **License:** Apache 2.0
- **Issues:** ~164 open
- **PRs:** ~208 open, 2,526 closed
- **Contributors:** 80+

### Recent Open PRs (showing active priorities):

| PR | Topic | Significance |
|----|-------|-------------|
| #3600 | feat(auth): asymmetric JWKS token validation | Enterprise security / multi-user |
| #3598 | feat(ingestion): PyO3 Rust chunker + priority queue | Performance + Rust edge engine |
| #3597 | fix(api): dataset isolation in search/recall | API maturity |
| #3596 | [hackathon] T0 Deployment-test harness | They're building hackathon infra |
| #3595 | feat(tutorial): migration tutorial for Letta/MemGPT and Zep | Competitor migration → onboarding |
| #3594 | Feat: turso vector backend | New backend adapter |
| #3592 | feat(search): CENTRALITY search with PageRank | Graph algorithm depth |
| #3586 | feat(search): NEIGHBORHOOD structural N-hop search | Graph traversal depth |
| #3582 | feat: add Turso(libSQL) as relational backend | Database flexibility |

### Open Issues (Good Contribution Targets):

| Issue | Topic | Difficulty |
|-------|-------|------------|
| #1444 | Add Pinecone Vector Adapter to cognee-community | Medium — adapter work |
| #1445 | Implement Advanced PDF Loader with unstructured library | Medium — ingestion |
| #1453 | Adding Support For Other LLMs in QuickStart | Easy — docs |
| #1446 | Ontology parameter in REST API | Medium — API feature |
| #1465 | MCP fails for IDE agents other than Cursor (CLOSED) | They fixed this — shows MCP is priority |

---

## 9. Hackathon-Specific Intelligence

### Cognee's Hackathon History (2026):

| Date | Hackathon | Partner | Focus |
|------|-----------|---------|-------|
| 2026-02-07 | AI Hack Night | Qdrant, Distil Labs, DigitalOcean | Prebuilt KG |
| 2026-04-25 | PR Rescue Arena | Daytona, Moss | GitHub PR analysis |
| 2026-05-16 | Agent LLM Wiki | Redis | Building wikis |
| 2026-06-16 | Company Brain | — | Slack + Granola KG |
| 2026-06-19 | Cloud Hackathon | — | Company Brain on Cognee Cloud |
| 2026-06-26 | GTM Brain (Warsaw) | modelguide | Accounts, Deals, Conversations |
| 2026-06-29 | The Hangover Part AI | WeMakeDevs | $10K prize pool, open-source + Cloud tracks |

### Current Challenge (June 2026): "Company Brain"

**The Brief:** Build a brain that:
1. **Ingests** scattered company knowledge (docs, Slack, tickets, code, meeting notes)
2. **Queries + Self-improves** — answers questions and uses feedback to refine
3. **Lints** — deduplicates, resolves conflicts, prunes stale entries

**Key Architecture Pattern:**
```python
# Session memory (fast, ephemeral)
await cognee.remember("User prefers detailed explanations.", session_id="chat_1")

# Permanent graph (durable, cross-session)
await cognee.remember("Retention is calculated as ...")

# Recall with auto-routing
results = await cognee.recall("What does the user prefer?", session_id="chat_1")
```

**Judging Criteria (inferred from challenge brief):**
- Does the brain demonstrate **distillation** from session to permanent memory?
- Is there a **self-improvement loop** with feedback?
- Does it use **Cognee Cloud** (bonus category)?
- Is there a **live demo** showing before/after improvement?
- Does it handle **multi-source ingestion** (not just text files)?

### The "Hangover Part AI" Hackathon (WeMakeDevs, June 29 - July 5, 2026):
- **$10,000 prize pool**
- **Best Use of Open Source Track:** Apple MacBook Neo per team member
- **Best Use of Cognee Cloud Track:** Apple iPhone 17 per team member
- **Job Interview Pipeline:** Top winners get direct technical interview slots with Cognee core team
- **Open Source PR Track:** $100 per accepted PR (top 20 submissions, max 5 per person)
- Access code for Cloud: `COGNEE-35`
- Allowed integrations: Claude Code, Codex, n8n, OpenClaw

---

## 10. Actionable Insights: What Would Make a Project Stand Out

### A. The "Winning Formula" for Cognee Hackathons:

**Tier 1 — Must-Have (Baseline):**
1. Use `cognee.add()` → `cognee.cognify()` → `cognee.memify()` → `cognee.search()` pipeline
2. Demonstrate **session vs. permanent memory** with `session_id`
3. Show **multi-source ingestion** (not just text — PDFs, CSVs, mock Slack data)
4. Include a **live demo** with before/after evidence

**Tier 2 — Differentiator (What Wins):**
1. **Self-improvement loop** — skill scoring + propose-then-apply pattern
2. **Cognee Cloud connection** — `cognee.serve()` + `cognee.push()` for bonus
3. **MCP integration** — agent reading/writing Cognee memory via MCP tools
4. **Multi-user isolation + sharing** — two users, private brains, explicit sharing
5. **Custom ontology** — Pydantic DataPoint subclasses for domain-specific entities

**Tier 3 — "Wow Factor" (What Gets You Hired):**
1. **Temporal reasoning** — using `temporal_cognify=True` to show "how did X change over time?"
2. **Graph visualization** — interactive HTML graph explorer (they have built-in tools)
3. **Cross-agent knowledge sharing** — multiple agents reading/writing the same brain
4. **Error compounding prevention** — showing how the brain grounds agents in reality
5. **Human-in-the-loop skill improvement** — explicit approve/reject for proposed skill rewrites

### B. Specific Open-Source Contributions That Would Be Valuable:

Based on open issues and PRs, these contributions would be genuinely valuable:

1. **Pinecone Vector Adapter** (Issue #1444) — High impact, medium difficulty
2. **Advanced PDF Loader** (PR #1445) — Medium impact, medium difficulty
3. **Migration tutorials** from Mem0, Zep, Letta (PR #3595) — Docs, easy win
4. **Windows compatibility fixes** (already done in PR #1464) — Shows platform awareness
5. **Multi-user authorization examples** (PR #1466) — Docs, high value for enterprise
6. **Ontology parameter in REST API** (Issue #1446) — API feature, medium difficulty

### C. Technology Stack Recommendations:

**For a "safe" winning project:**
- Python 3.11+ with `cognee==1.2.0.dev1` (latest hackathon build)
- Local dev + `cognee.serve()` to Cognee Cloud for bonus
- OpenAI for LLM (they provide keys at events, or use Ollama for local)
- Default stack: Kuzu (graph) + LanceDB (vector) + SQLite (relational)
- CLI for smoke tests: `cognee-cli remember / recall / forget`
- Optional: `cognee-cli -ui` for local graph explorer at localhost:3000

**For an "impressive" winning project:**
- Add **Claude Code MCP** integration for agentic memory read/write
- Add **n8n** workflow for automated ingestion (e.g., "when Slack message posted → add to Cognee")
- Use **OpenClaw** for personal agent memory
- Build a **custom Pydantic schema** extending `DataPoint` for your domain
- Implement the **skill feedback loop** with `SkillRunEntry` + `improve_skill()`

---

## 11. What to Avoid (Anti-Patterns)

Based on Cognee's philosophy and founder interviews:

1. **Don't build a simple RAG wrapper** — Cognee is explicitly NOT RAG. If your project is just "upload PDFs, ask questions," you'll blend in.

2. **Don't ignore the self-improvement loop** — A project that ingests once and queries statically misses Cognee's core value proposition.

3. **Don't treat memory as a flat database** — Cognee's founder studied cognitive science. Show you understand hierarchical memory (working vs. long-term, episodic vs. semantic).

4. **Don't skip the lint step** — The challenge explicitly requires deduplication, conflict resolution, and pruning. Show `cognee.memify()` or custom lint logic.

5. **Don't build a black box** — Cognee values transparency and auditability. Show the graph. Show the relationships. Make it inspectable.

6. **Don't assume agents are infallible** — The founder explicitly warns about "error compounding." Show guardrails, human-in-the-loop checks, or grounding mechanisms.

---

## 12. Cognee's Roadmap & Future Direction

### Current Version: v1.1.x (as of June 2026)
- Latest: v1.1.3 (June 18, 2026) — API mode robustness, dataset status queries
- Next: v1.2.0.dev1 (hackathon prerelease) — `cognee.serve()`, `cognee.push()`, `cognee.pull()`

### Gaps They're Acknowledging (from founder interviews):
1. **API usability** — still maturing compared to self-hosted SDK
2. **Mobile SDK** — not available yet
3. **TypeScript support** — incomplete (cognee-ts exists but not full-featured)
4. **Terabyte-scale datasets** — currently ~1GB/40min, need better scaling
5. **Voice agent memory** — "distinct emerging sub-problem" (founder's words)

### Future Direction (inferred):
- **Rust-based edge engine** (mentioned in docs, PR #3598 shows PyO3 Rust chunker)
- **On-device deployments** — for privacy-sensitive use cases
- **Cognee Cloud maturation** — moving from beta to production
- **More community adapters** — Pinecone, Turso, etc.
- **Better migration paths** from Mem0, Zep, Letta

---

## 13. Sources & References

- Cognee GitHub: https://github.com/topoteretes/cognee
- Cognee Docs: https://docs.cognee.ai
- Cognee Blog: https://www.cognee.ai/blog
- Cognee Hackathons: https://github.com/topoteretes/cognee-hackathons
- Cognee Cloud Pricing: https://www.cognee.ai
- Founder Interview (Heavybit Podcast): https://www.heavybit.com/library/podcasts/open-source-ready/ep-20
- Founder Interview (AI Engineering Podcast): https://www.aiengineeringpodcast.com/cognee-llm-semantic-memory-episode-42
- Memgraph Community Call: https://memgraph.com/blog/from-rag-to-graphs-cognee-ai-memory
- Competitor Comparison (Cognee Blog): https://www.cognee.ai/blog/guides/best-ai-memory-layers-for-ai-agents-in-2026-comparison
- WeMakeDevs Hackathon: https://internshala.com/competitions/the-hangover-part-ai/
- Cognee Cloud Challenge Brief: https://github.com/topoteretes/cognee-hackathons/tree/main/cognee-cloud-hackathon-2026-06-19
- Cognee GTM Brain Challenge: https://github.com/topoteretes/cognee-hackathons/tree/main/cognee-gtm-brain-hackathon-2026-06-26
- Cognee vs Graphlit: https://www.graphlit.com/vs/cognee
- Cognee Funding News: https://www.founderstoday.news/cognee-raises-over-7m-in-funding/

---

*Report compiled by Mnemosyne Research Agent on 2026-06-30. All information verified against live sources where possible.*

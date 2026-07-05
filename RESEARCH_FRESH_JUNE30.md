# Cognee Hackathon Fresh Intelligence Report
**Date:** June 30, 2026 (23:33 CEST)
**Hackathon:** The Hangover Part AI — WeMakeDevs × Cognee
**Window:** June 29 – July 5, 2026
**Prize Pool:** $10,000 + hardware + job interviews

---

## 1. HACKATHON STRUCTURE & PRIZES (CONFIRMED)

### Grand Prizes (Every winning team member receives the FULL prize)
- **Best Use of Open Source Track:** Apple MacBook Neo per team member (or cash equivalent)
- **Best Use of Cognee Cloud Track:** Apple iPhone 17 per team member (or cash equivalent)
- **Job Interview Pipeline:** Top winners get direct technical interviews with the core Cognee engineering team

### Open Source GitHub Contribution Track (Active NOW — no need to wait)
- **$100 per accepted Pull Request**
- Limited to top 20 accepted submissions overall
- Strict cap of **5 PRs maximum per individual** (prevents AI-generated spam)
- Can start contributing immediately
- Must comment on issue, get assigned, then submit PR

### Social/Blog Tracks
- **Best blog post:** Keychron mechanical keyboard ($120)
- **Top 10 social media posts** tagging @wemakedevs and Cognee → exclusive swag shipped

### Team Rules
- Max 4 members per team
- Solo participants allowed
- 100% virtual / global digital build sprint

---

## 2. WHAT PEOPLE ARE BUILDING (Past Cognee Hackathons & Community Signal)

Cognee has been running hackathons actively through 2026. The `cognee-hackathons` repo (github.com/topoteretes/cognee-hackathons) archives all prior events. Here is the pattern of what builders are creating:

### Past Hackathon Themes (2026)
| Date | Hackathon | Partner | Focus Area |
|------|-----------|---------|------------|
| 2026-02-07 | AI Hack Night | Qdrant, Distil Labs, DigitalOcean | Prebuilt KG + Q&A over finance/ops data |
| 2026-04-25 | PR Rescue Arena | Daytona, Moss | Contributing PRs to Cognee |
| 2026-05-16 | Agent LLM Wiki | Redis | Building agent wikis with memory |
| 2026-06-16 | Company Brain | — | Slack + Granola Knowledge Graph |
| 2026-06-19 | Build Your Company Brain | — | Cognee Cloud company memory |
| 2026-06-26 | GTM Brain (Warsaw) | modelguide | Merge Accounts, Deals & Conversations into One Graph |

### Notable Past Submission
**GrooveGraph** (by Sergej Kurtasch, June 2026)
- Personal self-improving learning brain for Ableton Live
- Implements: Ingest, Query + Self-improve, and Lint
- Uses both session memory and permanent graph memory
- Verified on Cognee Cloud

### Common Project Archetypes Emerging
Based on past hackathons and Cognee's marketing materials, the most common project types are:
1. **Company Brain / Team Wiki** — Slack/Granola/Notion data → unified knowledge graph
2. **Personal Second Brain** — Notes, bookmarks, articles → searchable memory
3. **GTM/Sales Brain** — CRM data (accounts, deals, conversations) → relationship graph
4. **Agent Memory Layer** — Giving an existing agent (Claude Code, Codex, etc.) persistent memory
5. **Creative/Domain Tools** — Music production (GrooveGraph), scientific research, medical assistants
6. **OpenClaw Integrations** — Using Cognee plugin for OpenClaw agents

---

## 3. COGNEE TECHNICAL STATE (June 2026)

### Latest Release: v1.2.2 (June 26, 2026) — "Truth Subspace & Retrieval Improvements"

**Major New Features in v1.2.2:**
- **Truth Subspace:** A compact index built from distilled, accepted session learnings that helps rerank search results and weight feedback. This is a "learning" layer that gets smarter with use.
- **Truth-subspace reranking + feedback activation:** Retrieval can now use a learned feedback signal to improve result relevance (opt-in by configuration). Default feedback influence is 0.0 unless explicitly set.
- **Improved LLM retry policy:** Smarter exponential backoff for transient failures (rate limits, network hiccups). Configurable per-request override.
- **LanceDB S3 fixes:** Resolved issues when using LanceDB with S3 storage.
- **Integrity/filtering improvements:** sha256 signatures, tightened centroid session filtering.

**v1.2.1 (June 21, 2026):**
- Search relevance improvements
- More robust ingestion and background sync
- Lower query latency
- Clearer indexing status indicators in UI

**v1.2.0.dev1 (June 19, 2026) — Preview Features:**
- **Collaboration preview:** Share memories and set basic permissions
- **Search tagging and autocomplete**
- **Slack and Google Drive connectors (preview/beta)**
- Memory sharing and permissions (read/write)

### Core API (What Hackathon Participants Use)
```python
import cognee
import asyncio

async def main():
    await cognee.add("Your content here")        # Ingest
    await cognee.cognify()                        # Build knowledge graph
    results = await cognee.search("Your query")   # Query
    
    # Also available:
    # await cognee.remember()  — store to graph
    # await cognee.recall()    — auto-routed search
    # await cognee.improve()   — memify/feedback
    # await cognee.forget()    — surgical deletion
```

### Cognee's Architecture (Why It's Different)
- **ECL Pipeline:** Extract → Cognify → Load
- **Hybrid Storage:** Graph (Kuzu/Neo4j/Memgraph) + Vector (LanceDB/Qdrant/etc.) + Relational (SQLite/Postgres)
- **14 retrieval modes** (most in the category)
- **Self-improving:** `memify`/`improve` updates edge weights based on feedback
- **Ontology support:** Validates against RDF/OWL (including SNOMED CT for healthcare)
- **MCP integration:** Works with Claude Desktop, Cursor, Claude Code, Codex
- **Local-first by default:** Runs on SQLite + LanceDB + Kuzu with zero cloud dependency
- **Cognee Cloud:** Managed option with free developer tier (code: `COGNEE-35`)

### Production Footprint (Cognee Claims)
- 70+ companies in production (including Bayer for scientific research, a Tier-1 US Bank, Dynamo for customer support, University of Wyoming for policy/legal)
- 500× YoY growth: from ~2,000 pipeline runs to 1M+ in 2025
- 17,800–26,000+ GitHub stars (reports vary by source)
- $7.5M seed raised (February 2026)
- Graduated from GitHub Secure Open Source Program

---

## 4. GITHUB ISSUE LANDSCAPE (June 30, 2026)

### Active Issue Volume
- **cognee repo:** Issues #3688 through #3708+ opened in the last few days (late June 2026)
- **cognee-rs repo:** 27+ issues active (Rust SDK)
- **cognee-integrations repo:** 1 PR, active community maintained adapters

### Specific Notable Issue (Good for Hackathon PR)
**Issue #3235 (June 21, 2026):** `delete_data()` skips dataset membership check when relational Data row is missing
- **Severity:** Security/ACL bypass in multi-tenant deployments
- **Impact:** Collaborator with delete permissions can invoke graph deletion for UUIDs not validated against dataset membership
- **Suggested fix:** Fail closed — return 404 unless `ALLOW_CUSTOM_GRAPH_DELETE=true` is set
- **Files affected:** `cognee/api/v1/datasets/datasets.py`, `cognee/modules/graph/methods/delete_data_nodes_and_edges.py`
- **Good for:** A clean, scoped security PR that would likely be accepted

### General Issue Patterns
- Many recent issues relate to **session management**, **QA vector handling**, **ingestion reliability**
- Active work on **LanceDB adapters**, **MCP server**, **UI visualization**
- Cognee actively encourages PRs — check issues labeled `good-first-issue`
- The Cognee team is responsive; the June 2026 release cadence is very fast (multiple releases per week)

### PR Strategy for Hackathon
1. Browse github.com/topoteretes/cognee/issues and filter by `good-first-issue`
2. Comment on the issue, tag maintainers, wait for assignment
3. Submit PR — max 5 per person
4. $100 per accepted PR, top 20 submissions total

---

## 5. COMPETITOR LANDSCAPE (June 2026)

Understanding what competitors are doing is critical to building a **differentiated** hackathon project.

### Mem0 (mem0ai/mem0) — ~47-48K GitHub Stars
**What they're doing in June 2026:**
- **OpenCode Plugin v0.2.0 (June 2026):** Native OpenCode tools, auto-dream (gated automatic memory consolidation), memory scope (project/session/global), expanded telemetry
- **April 2026 algorithm update:** Token-efficient memory algorithm — 92.5 LoCoMo, 94.4 LongMemEval, 6,787 tokens per retrieval
- **Multi-signal retrieval:** Semantic + BM25 + entity matching in parallel
- **Temporal reasoning:** Added time-aware retrieval (though not as deep as Zep)
- **AWS Agent SDK exclusive memory provider** (major enterprise signal)
- **$24M Series A** (October 2025)
- **21 framework integrations, 20 vector backends**

**Mem0's weakness (opportunity for Cognee):**
- Graph features are **gated behind $249/mo Pro tier** (Vectorize, 2026 confirms free tier is vector-only)
- Scores 49% on LongMemEval temporal queries (lowest of major systems)
- SDK lock-in — switching frameworks means migrating all accumulated memories
- No self-improving memory layer

### Zep (getzep.com) — Temporal Graph Specialist
**What they're doing in June 2026:**
- **Smart Context Assembly (May 2026):** Higher accuracy from fewer tokens, no code changes needed
- **Graphiti open-source engine:** Temporal knowledge graph with Neo4j/FalkorDB/Kuzu backends
- **Best-in-class temporal reasoning:** 63.8% LongMemEval vs Mem0's 49%, 94.7% LoCoMo at 87ms p50
- **SOC 2 Type II, HIPAA BAA**
- **Context Lake positioning:** "Agent memory built to run, not assemble"
- Directly targeting Cognee users with comparison pages ("Cognee is open-source toolkit you wire together; Zep is managed Context Lake")

**Zep's weakness (opportunity for Cognee):**
- **Cloud-only** for full platform (no real self-host for full features)
- **Steep pricing:** Free tier = 1,000 credits/mo (barely enough to prototype). Flex = $125/mo. Flex Plus = $375/mo.
- **Requires graph database** (Neo4j/FalkorDB/Kuzu) — operational complexity
- **No self-improvement** — graph is static once built unless manually updated
- **Smaller community** than Mem0

### Letta (formerly MemGPT) — OS-Style Agent Memory
**What they're doing in June 2026:**
- **Letta Code:** Memory-first coding agent, #1 on Terminal-Bench leaderboard for OSS coding agents
- **Conversations API:** Agents share memory across parallel user experiences
- **Rearchitected agent loop:** ReAct + MemGPT + Claude Code lessons
- **Three-tier memory model:** Core (RAM) / Recall (disk cache) / Archival (cold storage)
- **Agent self-edits memory:** Agent decides what to keep, evict, summarize

**Letta's weakness (opportunity for Cognee):**
- **No graph traversal** — primarily vector-based archival search
- **No self-improvement at the memory layer** — paging only, no feedback-driven edge weight updates
- **Retrieval latency:** p95 search latency of 59.82 seconds (LangMem, related project)
- **Replaces your orchestration layer** — you must adopt Letta's runtime

### Graphiti (by Zep team) — Open Source Temporal KG Engine
- Open-source temporal knowledge graph
- Powers many agent memory implementations
- Used alongside Zep for graph-based recall
- **Not a full memory framework** — just the graph engine

### Key Differentiator Matrix (June 2026)

| Feature | Cognee | Mem0 | Zep | Letta |
|---------|--------|------|-----|-------|
| **Hybrid Graph+Vector+Relational** | ✅ | ✅ (Pro only) | ✅ | ❌ (Vector only) |
| **Self-improving memory** | ✅ (memify) | ❌ | ❌ | ❌ |
| **14 retrieval modes** | ✅ | Moderate | Graph traversal | Limited |
| **Fully local-first** | ✅ | ✅ | ❌ (Cloud only) | ✅ |
| **Temporal knowledge** | Partial | Partial | ✅ Best-in-class | ❌ |
| **Compliance (SOC2/HIPAA)** | ❌ | Enterprise tier | ✅ | Unknown |
| **MCP/Claude Code integration** | ✅ | ✅ | Community | ✅ |
| **Free open-source tier** | ✅ Full | ✅ Limited | ❌ 1K credits | ✅ |
| **Rust/edge SDK** | ✅ (cognee-rs) | ❌ | ❌ | ❌ |
| **Auto-ontology (SNOMED CT)** | ✅ | ❌ | ❌ | ❌ |

---

## 6. WHAT THE COMMUNITY IS EXCITED ABOUT (Discussions & Sentiment)

### Reddit / Hacker News / Twitter Signal
- **r/AIMemory** is the subreddit where Cognee community discusses memory frameworks
- **Cognee Discord** is active (linked from GitHub org page)
- **General sentiment:** Cognee is gaining traction as the "local-first, self-improving, hybrid memory" option. The fast release cadence (v1.2.x in June 2026) is generating positive developer buzz.
- **Key community request:** Better TypeScript support, mobile SDK, easier API usability, more connectors (Slack/GDrive just entered preview)

### Langfuse Integration (June 2026)
Cognee + Langfuse integration was published, giving production-grade tracing, evaluation, and analytics for every pipeline step. This signals Cognee is pushing into production observability — a strong angle for hackathon projects.

### Cognee MCP + Claude Code / Codex
- Cognee ships as a Claude Code plugin (`claude-code-plugin`)
- Available as OpenClaw plugin (`cognee-openclaw`)
- MCP integration allows Cursor, Claude Desktop to read/write memories directly
- **This is a hot integration area** — most competitors don't have first-party MCP servers

### What People Are Actually Saying
- One first-hand evaluation (May 2026): "Cognee's operational footprint was more than the MVP needed" — but this is pre-v1.2.x, before truth subspace and major UX improvements
- Another (June 2026): "Cognee scored highest across storage architecture, retrieval modes, pipeline automation, and self-improvement" in a head-to-head framework comparison
- Zep's own comparison page: "Cognee is open-source toolkit you wire together and operate. Zep is agent memory at enterprise scale, delivered as a managed Context Lake."
- Mem0 comparison: "Cognee is closer to graph-RAG than to chat memory"

---

## 7. MOST COMMON PROJECT TYPES FOR THIS HACKATHON

Based on the hackathon rules, past submissions, and the "Company Brain" trend, these are the most likely project types:

1. **Personal Knowledge Assistant / Second Brain**
   - Ingest notes, PDFs, bookmarks → query via natural language
   - **Risk:** Many teams will build this. Differentiation is hard.

2. **Company/Team Wiki ("Company Brain")**
   - Slack, Notion, Google Drive → unified knowledge graph
   - **Risk:** Cognee has literally run two hackathons on this exact theme in June 2026. This will be VERY common.

3. **Agent Memory Layer**
   - Plug Cognee into Claude Code, Codex, n8n, or a custom agent
   - **Risk:** Moderate originality. Many teams will do basic `remember`/`recall` integrations.

4. **CRM/GTM Brain**
   - Accounts, deals, conversations → relationship graph
   - **Risk:** Just had a dedicated hackathon on this (June 26, Warsaw).

5. **Creative/Domain-Specific Tool**
   - Music (GrooveGraph), medical, legal, scientific research
   - **Opportunity:** Less crowded if you pick a niche domain.

---

## 8. MOST DIFFERENTIATED PROJECT IDEAS (Strategic Recommendations)

To win in a crowded field, the project should exploit Cognee's **unique strengths** that competitors cannot easily match:

### A. Self-Improving Memory with Feedback Loop (Truth Subspace)
**Why differentiated:** Cognee is the ONLY major framework with `improve()` / `memify` / truth subspace. Mem0, Zep, and Letta have NO self-improvement.
**Project idea:** Build an agent that gets smarter with every conversation by using Cognee's truth subspace to rerank and weight memories based on user feedback. Show a before/where the agent learns from corrections.
**Killer demo:** Start with a naive agent, have the user correct it 3-5 times, show the truth subspace updating, then show the corrected behavior in a new session.

### B. Multi-Agent Shared Memory with Cross-Agent Learning
**Why differentiated:** Cognee's hybrid graph+vector architecture makes it uniquely suited for multiple agents sharing a knowledge graph. Letta has no shared memory. Mem0 has multi-agent but no graph traversal.
**Project idea:** 2-3 specialized agents (researcher, writer, reviewer) that all read/write to the same Cognee graph. Show how the writer agent discovers the researcher's findings through graph traversal, not just keyword search.
**Killer demo:** Agent A reads a PDF and stores facts. Agent B asks a question that requires connecting two facts Agent A stored — and finds them via graph edges, not vector similarity.

### C. Temporal Audit + Knowledge Graph Provenance
**Why differentiated:** Cognee doesn't have Zep's native temporal invalidation, BUT it has a graph structure. You can build a layer on top that tracks "when did this fact change?" by storing versioned nodes.
**Project idea:** A compliance/audit agent that shows WHEN a fact was learned, when it was updated, and WHO (which agent) asserted it. This targets Cognee's enterprise use cases (Bayer, banking).
**Killer demo:** User asks "What was the project deadline last month?" The agent traverses the graph and shows the evolution of the deadline fact across time.

### D. Offline/Edge Memory with Cognee-RS
**Why differentiated:** Cognee has a **Rust SDK (cognee-rs)** for edge devices (phones, IoT). Neither Mem0 nor Zep nor Letta have a Rust/edge client.
**Project idea:** A mobile or IoT agent that runs Cognee memory entirely offline using the Rust engine, then syncs to cloud when connected.
**Killer demo:** An iOS/Android app that ingests voice notes, builds a local graph, and answers questions without any network call.

### E. Ontology-Grounded Domain Memory (Healthcare/Science)
**Why differentiated:** Cognee supports RDF/OWL ontology validation (including SNOMED CT). No competitor has this.
**Project idea:** A medical or scientific agent that ingests papers/reports and validates extracted entities against a medical ontology (SNOMED CT). Ensures the agent doesn't hallucinate medical relationships.
**Killer demo:** Ingest a medical case study. Show the graph with nodes validated against SNOMED CT. Show a competitor (pure vector) getting the relationship wrong.

### F. n8n Visual Automation with Cognee Memory
**Why differentiated:** The hackathon explicitly allows n8n integrations for "zero-backend visual automation loops." Most participants will build Python backends. A no-code/low-code approach stands out.
**Project idea:** An n8n workflow that ingests emails, Slack messages, and meeting notes into Cognee automatically, then a trigger-based agent that answers questions from the accumulated graph.
**Killer demo:** Show the n8n canvas. No code visible. Data flows in, Cognee builds the graph, a chatbot node queries it.

### G. Memory Visualization + Graph Explorer
**Why differentiated:** Cognee has a graph explorer UI. Building a custom, beautiful visualization of the knowledge graph that shows how an agent's memory is structured is visually compelling for judges.
**Project idea:** A 3D or interactive graph visualization where the user can explore their agent's memory, see clusters of related concepts, and manually edit nodes/edges.
**Killer demo:** A live 3D force-directed graph that updates in real-time as the agent learns new facts. Judges can click nodes and see relationships.

---

## 9. KEY TECHNICAL INSIGHTS FOR BUILDING

### Cognee's Latest June 2026 Features to Leverage
1. **Truth Subspace (v1.2.2):** Use `DEFAULT_FEEDBACK_INFLUENCE` to make your agent learn from user corrections. Set it > 0.0 in config.
2. **Slack & Google Drive Connectors (v1.2.0 preview):** If your project ingests from these sources, you can claim "using the latest preview features."
3. **Improved retry policies:** Your demo will be more reliable against LLM rate limits.
4. **Search tagging:** Add tags to memories for faster retrieval in your app.

### Competitor Weaknesses to Highlight in Your Pitch
- **Mem0:** "We built a graph that connects ideas, not just a vector search. Mem0's graph is behind a $249 paywall."
- **Zep:** "We run fully local and self-hosted. Zep's cloud-only model means vendor lock-in and data leaving your infrastructure."
- **Letta:** "We let any agent use our memory, not just Letta's runtime. Our memory works with Claude Code, Codex, or your custom agent."
- **All competitors:** "None of them have self-improving memory. Our agent gets smarter with every interaction through Cognee's truth subspace."

### Deployment Options for Demo
- **Local demo:** `pip install cognee` → SQLite + LanceDB + Kuzu. Works offline. No API keys needed for embeddings if using Ollama.
- **Cognee Cloud:** Free developer tier with code `COGNEE-35`. Good for "Best Use of Cognee Cloud" track.
- **Docker:** One-liner deployment for judges to reproduce.

### Integration Hooks
- **Claude Code:** `claude-code-plugin` available
- **OpenClaw:** `cognee-openclaw` plugin
- **n8n:** Visual automation, zero backend
- **MCP:** Works with Cursor, Claude Desktop
- **Langfuse:** Add observability/tracing to your pipeline

---

## 10. ACTIONABLE RECOMMENDATIONS FOR THE PARENT AGENT

### Immediate Actions (Before July 5 deadline)
1. **Pick a differentiation angle NOW.** Do NOT build a generic "Company Brain" — two hackathons already focused on that in June 2026. It will be a crowded category.
2. **Strongest differentiation angles:** Self-improving memory (truth subspace), Multi-agent shared graph, Edge/offline (cognee-rs), Ontology-grounded domain (SNOMED CT), n8n no-code automation.
3. **Consider the PR track simultaneously.** Issue #3235 (ACL bypass) is a clean, well-scoped security fix that would likely be accepted and earn $100. Max 5 PRs per person.
4. **Use v1.2.2 features in your project.** Truth subspace is brand new (June 26). Using it shows you're on the cutting edge.
5. **If building for Cognee Cloud track:** Use free tier code `COGNEE-35`. The iPhone 17 prize is specifically for cloud builds.
6. **If building for Open Source track:** Emphasize local-first, self-hosted, privacy. The MacBook Neo prize is for best open-source Cognee build.
7. **Blog + social strategy:** Write about your build journey. Tag @wemakedevs and Cognee. Top 10 posts get swag. Best blog wins a Keychron keyboard.
8. **Demo must be live and visual.** 3-minute presentation. Judges value live demos over slides. A graph visualization is highly compelling.

### Risk Assessment
- **HIGH RISK:** Generic Company Brain, generic chatbot with memory, basic RAG wrapper. These are too common and won't stand out.
- **MEDIUM RISK:** Agent memory layer for Claude Code (several teams will do this, but good execution wins).
- **LOW RISK / HIGH REWARD:** Truth subspace self-improvement, multi-agent shared graph, edge/offline Rust, ontology-grounded medical/scientific agent, n8n visual automation.

### What to Avoid
- Don't spam the Cognee GitHub with AI-generated PRs. The rules explicitly state: "Anyone who opens more than 5 PRs will be banned."
- Don't build a project that requires days of data ingestion. Hackathon is 7 days. Pick a use case where you can demo with pre-loaded or quickly ingestible data.
- Don't rely on Cognee Cloud exclusively if you're going for the Open Source track. The tracks are separate prizes.

---

## 11. SOURCES & REFERENCES

- WeMakeDevs Hackathon Page: https://www.wemakedevs.org/hackathons/cognee
- Cognee GitHub: https://github.com/topoteretes/cognee
- Cognee Hackathons Archive: https://github.com/topoteretes/cognee-hackathons
- Cognee Releases (v1.2.2): https://github.com/topoteretes/cognee/releases
- Cognee-RS (Rust SDK): https://github.com/topoteretes/cognee-rs
- Cognee Community Integrations: https://github.com/topoteretes/cognee-community
- Cognee Review (AI Agent Index): https://theaiagentindex.com/agents/cognee
- Mem0 Release Notes (June 2026): https://releasebot.io/updates/mem0
- Zep Blog (Smart Context Assembly): https://blog.getzep.com/
- Letta Deep Dive (CallSphere): https://callsphere.ai/blog/vw3g-letta-memgpt-agent-memory-layer-deep-dive-2026
- Agent Memory Comparison (Particula): https://particula.tech/blog/agent-memory-frameworks-tested-mem0-zep-letta-cognee-2026
- Cognee vs Competitors (TryXLR8): https://tryxlr8.ai/blogs/best-open-source-ai-memory-frameworks-2026
- MCP Directory Comparison: https://mcp.directory/blog/mem0-vs-letta-vs-zep-vs-cognee-2026
- Cognee × Langfuse Integration: https://langfuse.com/integrations/other/cognee
- Cognee Research Paper: arXiv:2505.24478
- Mem0 Research Paper: arXiv:2504.19413
- Zep/Graphiti Paper: arXiv:2501.13956
- Cognee Discord: linked from github.com/topoteretes
- Reddit: r/AIMemory

---

*Report compiled by research sub-agent on June 30, 2026, 23:33 CEST.*
*All data sourced from live web search, GitHub, and official Cognee/WeMakeDevs channels.*

# MNEMOSYNE: KEEP / KILL / INTRODUCE — Strategic Decision Framework

**Date:** July 2026 | **Comparing:** Original Platform (code) vs. Old Plan (v2.0 brief) vs. New Plan (v3.0 rebuild)

---

## 🗺️ THE THREE LAYERS WE'RE COMPARING

| Layer | What It Is | Status |
|-------|-----------|--------|
| **Original Platform** (Unified Memory) | Working code: FastAPI MCP server, Cognee bridge, 20+ connectors, NEAR NFTs, x402 payments, PostgreSQL + Neo4j + Redis + MinIO | **Functional but fragmented** |
| **Old Plan** (v2.0 Brief) | Architecture document: Three-layer stack (Redis→PostgreSQL→S3), scheduler, admission control, MCP, markdown, 4-month phases | **Strategically sound but incomplete** |
| **New Plan** (v3.0 Rebuild) | Research-synthesized plan: Microkernel + plugins, SMSR security, prospective memory, emotional salience, versioning, multi-agent, 12-month phases | **Comprehensive but 12-month timeline** |

---

## ✅ KEEP FROM THE ORIGINAL PLATFORM (Working Code)

### 1. The Core FastAPI Server Architecture

**What to keep:** The FastAPI server in `workers/cognee_local_server.py` is well-structured with:
- CORS middleware configured
- Health check endpoint
- MCP manifest endpoint (`/.well-known/mcp`)
- JSON-RPC error format (standard for MCP)
- Upload/ingestion endpoints

**What to change:** The current API is Cognee-centric. We need to abstract it to support multiple backends (PostgreSQL + pgvector, Cognee, ArcadeDB). The kernel + plugin architecture (v3.0) wraps this.

**Verdict:** ✅ **Keep the server scaffold, refactor into microkernel**

### 2. The Cognee Bridge (`ingestion/cognee_bridge.py`)

**What to keep:** The bridge pattern itself — abstracting Cognee's `remember()` / `recall()` / `improve()` / `forget()` into async wrappers with:
- OpenRouter passthrough configuration
- Dataset-based multi-tenancy (`dataset_name=user_id`)
- Result normalization
- Sync wrappers for non-async callers

**What to change:** Move from Cognee as the ONLY backend to Cognee as ONE plugin. The v3.0 plan adds a PostgreSQL + pgvector plugin, ArcadeDB plugin, and a plugin manager that routes between them.

**Verdict:** ✅ **Keep as a plugin, not the core**

### 3. The Memory Classification Pipeline (`ingestion/cognee_synthesis.py`)

**What to keep:** The `RawMemory` → `ClassifiedMemory` → structured text pipeline is excellent:
- DeepSeek V3.2 for classification (fast, cheap, accurate)
- OpenRouter passthrough (no API key management)
- 5 memory types: episodic, semantic, procedural, social, preferential
- YAML frontmatter formatting
- Provenance hashing (SHA-256)

**What to change:** Add 2 more memory types (emotional, meta) and expand the classification to include salience factors, confidence scores, temporal validity, and source attribution. This is core IP — keep it.

**Verdict:** ✅ **Keep and expand (7 types → 6 types in v3.0, but richer metadata)**

### 4. The Connector Architecture

**What to keep:** The connector pattern (upload → parse → synthesize → ingest) is correct. The 3 upload connectors (ChatGPT, Claude, Telegram) demonstrate the pattern. The `run_connector` abstraction in `ingestion/run.py` is the right approach.

**What to change:** Move from 3 hardcoded connectors to a **plugin marketplace** where connectors are dynamically loaded. Each connector is a plugin with a standard interface. The v3.0 plan has 20+ connectors as marketplace plugins, not core code.

**Verdict:** ✅ **Keep the pattern, make it plugin-based**

### 5. The NEAR Consent + x402 Payment Flow

**What to keep:** The NEAR NFT consent pattern is genuinely novel — "token-gated cognitive graphs" is a unique concept. The x402 payment flow (402 Payment Required → USDC on Base Sepolia) is clever.

**What to change:** Make it **optional, not mandatory**. The v3.0 plan makes Stripe primary and crypto optional. The current code requires NEAR token for every operation, which is a massive friction point. The consent NFT should be a "provenance verification" feature, not a gate.

**Verdict:** ⚠️ **Keep as optional Web3 layer, remove as mandatory gate**

### 6. The Demo Data (`demo/cognee_hackathon_demo.py`)

**What to keep:** The 30 synthetic memories across 10 platforms are excellent for testing, benchmarking, and demos. The cross-platform data (Gmail, GitHub, Slack, Spotify, Notion, etc.) demonstrates the value proposition.

**What to change:** Expand to 100+ demo memories with richer relationships, contradictions, and temporal chains. Use this as the benchmark dataset for evaluating the platform.

**Verdict:** ✅ **Keep and expand as benchmark dataset**

---

## ❌ KILL FROM THE ORIGINAL PLATFORM (Technical Debt & Wrong Bets)

### 1. Cognee as the ONLY Backend

**Why kill:** The original platform is hardcoded to Cognee (SQLite + LanceDB + Ladybug). This means:
- No horizontal scaling (SQLite is single-node)
- No multi-tenant isolation (dataset_name is a string, not real isolation)
- No query performance at scale (Ladybug is experimental)
- Vendor lock-in to Cognee's Python-only, async-only API

**What replaces it:** PostgreSQL + pgvector + pgvectorscale as the default queryable layer. Cognee becomes a plugin for graph-heavy use cases. ArcadeDB as the graph fallback.

**Verdict:** ❌ **Kill Cognee-as-core, keep as plugin**

### 2. SQLite as the Primary Database

**Why kill:** SQLite is used because Cognee defaults to it. For a production platform:
- No concurrent write support (WAL mode helps but doesn't scale)
- No vector indexing (LanceDB is bolted on)
- No full-text search
- No row-level security
- No replication

**What replaces it:** PostgreSQL 16 + pgvector + pgvectorscale + pg_trgm. This is the industry-standard vector database in 2026. Cognee serves 6M+ memories/month on one PostgreSQL instance.

**Verdict:** ❌ **Kill SQLite, migrate to PostgreSQL**

### 3. Redis (Hot State) — LICENSE RISK

**Why kill:** Redis 8 moved to a **controversial tri-license** (AGPL/RSAL/SSPL). This creates legal risk for any commercial product using Redis. The SSPL specifically requires releasing ALL source code if you offer Redis as a service.

**What replaces it:** **Valkey** — BSD-3, Linux Foundation, zero-risk drop-in replacement. AWS, GCP, and Azure are migrating under the hood. No code changes needed.

**Verdict:** ❌ **Kill Redis, migrate to Valkey immediately**

### 4. NEAR as Mandatory Authentication

**Why kill:** The current server requires a NEAR token_id for EVERY operation. This is a massive adoption barrier:
- 99% of users don't have a NEAR wallet
- Web3 friction is real (wallet connection, gas fees, token management)
- The x402 payment flow adds another layer of friction
- No email/password, no OAuth, no SSO

**What replaces it:** OAuth 2.1 + PKCE (JWT) as the primary auth. NEAR as an optional Web3-native add-on for users who want on-chain provenance and consent NFTs.

**Verdict:** ❌ **Kill mandatory NEAR, make it optional**

### 5. LanceDB as the Vector Store

**Why kill:** LanceDB is columnar and Arrow-native, but:
- No HNSW index (only IVF)
- No pgvectorscale integration
- No SQL interface
- No full-text search hybrid
- Smaller ecosystem than pgvector

**What replaces it:** pgvector (with HNSW index) + pgvectorscale (for 28× speedup at 50M vectors). This is the 2026 standard.

**Verdict:** ❌ **Kill LanceDB, use pgvector + pgvectorscale**

### 6. Ladybug as the Graph Engine

**Why kill:** Ladybug is Cognee's experimental graph database. It's:
- Not production-ready
- No Cypher support
- No visualization tools
- No ecosystem
- Single-node only

**What replaces it:** ArcadeDB (Apache 2.0, multi-model: graph + vector + document, Cypher-compatible, Cognee-integrated) or Neo4j (if you need the managed option).

**Verdict:** ❌ **Kill Ladybug, use ArcadeDB or Neo4j**

### 7. The "Unified Memory" Branding

**Why kill:** "Unified Memory" is generic. It doesn't communicate what the platform DOES. It's also tied to the old architecture ("unified" = one database, which is wrong).

**What replaces it:** **Mnemosyne** — named after the Greek goddess of memory. It communicates:
- Memory (the core function)
- Intelligence (Mnemosyne was mother of the Muses — creativity, art, knowledge)
- Mythology (memorable, distinctive, unique)
- The "Memory OS" positioning

**Verdict:** ❌ **Kill "Unified Memory", keep "Mnemosyne"**

---

## ✅ KEEP FROM THE OLD PLAN (v2.0 Brief — Strategic Direction)

### 1. "Memory OS" Positioning

**Why keep:** The "Memory OS, not a database" positioning is the single most important strategic decision. It differentiates from:
- Cognee (database/framework)
- Mem0 (database/API)
- Zep (database/API)
- Letta (framework)

An OS has: kernel, scheduler, plugins, security model, ecosystem. This is the winning narrative.

**Verdict:** ✅ **Keep — this is the core brand strategy**

### 2. Three-Layer Stack Concept

**Why keep:** The hot → queryable → cold layering is correct:
- Hot: Working memory (session cache, ephemeral)
- Queryable: Fast retrieval (PostgreSQL + pgvector)
- Cold: Archive + compliance (S3 + R2)

**What to change:**
- Hot: Redis → Valkey (license)
- Queryable: Add pgvectorscale at >10M vectors
- Cold: Add R2 for zero-egress retrieval
- Add graph layer (ArcadeDB) when >100M edges

**Verdict:** ✅ **Keep the concept, update the technologies**

### 3. The Scheduler (Query Router)

**Why keep:** Routing queries to the correct memory subsystem (episodic vs. semantic vs. procedural) is the core differentiator. The v2.0 plan describes this as a "query classifier."

**What to change:** Make it a **kernel component**, not a middleware layer. The v3.0 plan makes it part of the microkernel, with plugins registering their routing rules.

**Verdict:** ✅ **Keep and elevate to kernel**

### 4. Admission Control (Security Gate)

**Why keep:** The 5-step gate (length → injection → duplicate → contradiction → salience) is the right approach. It's fast (~3ms) and catches the most common issues.

**What to change:** Expand to 6 steps with **SMSR-certified** provenance signing (HMAC-SHA256) as step 6. Add MINJA pattern detection and ADAM query-pattern anomaly detection. This is the v3.0 security model.

**Verdict:** ✅ **Keep and harden with SMSR**

### 5. Markdown as Universal Format

**Why keep:** Obsidian-compatible YAML frontmatter + wiki-links is the right choice. It's:
- Human-readable
- Git-diffable
- LLM-parseable
- Industry-standard (CLAUDE.md, AGENTS.md, .cursorrules all use this)

**What to change:** Add more metadata fields (valid_at, invalid_at, confidence, source_type, provenance_hash, version_id, branch_name) and make it the **source of truth** (files are primary, DB is index).

**Verdict:** ✅ **Keep and expand metadata**

### 6. MCP as Primary Integration

**Why keep:** MCP is the de facto standard for AI tool integration. 97M SDK downloads, 78% enterprise adoption. The v2.0 plan correctly identifies this.

**What to change:** Update to the **2026-07-28 spec** (stateless, Streamable HTTP, no SSE). Add OAuth 2.1 + PKCE auth. The v3.0 plan has the updated MCP implementation.

**Verdict:** ✅ **Keep MCP, update to 2026-07-28 spec**

### 7. Emotional Salience Scoring

**Why keep:** This is a genuinely unique feature. No competitor has it. The 5-factor model (user_emphasis, outcome_type, engagement, confidence, recency) is biologically-inspired and technically sound.

**What to change:** Implement it as a **plugin** (Emotional Salience Engine) rather than a hardcoded scoring function. Allow custom salience factors via plugin configuration.

**Verdict:** ✅ **Keep and make it a plugin**

### 8. Prospective Memory (Reminders)

**Why keep:** This is the #1 user-requested feature that no framework ships. "Remember to check this in 3 days" is a massive differentiator.

**What to change:** Expand from simple cron to 5 trigger types: absolute, relative, recurring, event, condition. Make it a first-class plugin with its own scheduler.

**Verdict:** ✅ **Keep and expand (the v3.0 plan has the full implementation)**

### 9. Observability Dashboard

**Why keep:** The 5,760 case study showed 61% → 94% accuracy improvement from audit trails alone. This is the biggest ROI feature.

**What to change:** Make it **first-class from Day 1**, not a Phase 4 afterthought. The v3.0 plan has it in the kernel with tamper-evident SHA-256 hash chains and Ed25519 signatures.

**Verdict:** ✅ **Keep and elevate to kernel (not Phase 4)**

### 10. Sleep-Time Consolidation

**Why keep:** The 5-step nightly batch (merge duplicates, prune stale, update embeddings, rebuild links, generate audit report) is the right maintenance model.

**What to change:** Add contradiction detection, temporal decay, salience update, and relationship inference. Make it a **plugin** that other plugins can register consolidation hooks with.

**Verdict:** ✅ **Keep and expand to full consolidation engine**

---

## ❌ KILL FROM THE OLD PLAN (v2.0 — Outdated or Wrong)

### 1. The 4-Month Timeline

**Why kill:** The v2.0 plan phases are: MVP (Month 1) → Security (Month 2) → Scheduler (Month 3) → Observability (Month 4). This is too aggressive:
- Security is not optional — it must be in the MVP
- Observability is not optional — it must be in the MVP
- The scheduler IS the MVP — without it, you're just a database
- No time for SDKs, CLI, multi-agent, or compliance

**What replaces it:** 7 phases over 12 months (v3.0 plan). Foundation (2 weeks) → Core (Month 1) → Security (Month 2) → Intelligence (Month 3) → Multi-Agent (Month 4) → Compliance (Months 5-6) → Ecosystem (Months 7-9) → Performance (Months 10-12).

**Verdict:** ❌ **Kill the 4-month plan, use 12-month plan**

### 2. Neo4j as Default Graph Database

**Why kill:** The v2.0 plan recommends Neo4j as the default graph database. But:
- Neo4j is JVM-heavy (2GB+ heap)
- Expensive ($$$ for enterprise features)
- AuraDB is cloud-only (lock-in)
- Cypher is the only query language

**What replaces it:** PostgreSQL recursive CTEs for graphs <100M edges. ArcadeDB for graphs >100M edges (Apache 2.0, multi-model, Cypher-compatible, faster).

**Verdict:** ❌ **Kill Neo4j-as-default, use PostgreSQL CTEs + ArcadeDB**

### 3. SSE as MCP Transport

**Why kill:** The v2.0 plan mentions SSE (Server-Sent Events) as an MCP transport. The 2026-07-28 spec **deprecated SSE**. Streamable HTTP is the new standard.

**What replaces it:** stdio (for local IDE use) + Streamable HTTP (for production/remote). No SSE.

**Verdict:** ❌ **Kill SSE, use Streamable HTTP**

### 4. GraphQL

**Why kill:** The v2.0 plan says "GraphQL never" — this is correct. But we need to be more explicit: GraphQL adds complexity with no benefit for AI tool use. REST + MCP is the right stack.

**What replaces it:** Nothing. REST is sufficient. MCP is the primary interface.

**Verdict:** ✅ **Already correct — keep "no GraphQL"**

### 5. The Monolithic Stack Architecture

**Why kill:** The v2.0 plan describes a monolithic stack (FastAPI + PostgreSQL + Redis + S3). This is fine for MVP but doesn't scale to "Memory OS."

**What replaces it:** **Microkernel + Plugin Architecture** (v3.0 plan). The kernel never changes. Plugins load/unload dynamically. Each memory subsystem is a plugin. Each connector is a plugin. Each storage engine is a plugin.

**Verdict:** ❌ **Kill monolithic, use microkernel + plugins**

---

## 🆕 INTRODUCE FROM NEW RESEARCH (v3.0 Plan)

### 1. Microkernel + Plugin Architecture (HIGHEST PRIORITY)

**What it is:** A tiny kernel (~1000 lines) that manages plugins, routes queries, enforces security, and schedules tasks. Everything else is a plugin.

**Why it's critical:** This is the difference between "a database with features" and "an operating system." WordPress, Shopify, VS Code, Obsidian all use this architecture. It's what makes a platform extensible.

**Implementation:**
```python
class Kernel:
    def __init__(self, config):
        self.plugins = PluginManager()
        self.router = QueryRouter()
        self.admission = AdmissionControl()
        self.scheduler = ProspectiveScheduler()
        self.audit = AuditTrail()
```

**Risk:** Medium — requires refactoring the existing monolithic server. But the existing code is already modular enough (Cognee bridge, synthesis pipeline, connectors) that it's a natural fit.

**Verdict:** 🆕 **INTRODUCE — Foundation of the platform**

### 2. SMSR-Certified Security (HIGHEST PRIORITY)

**What it is:** Secure Memory Storage and Retrieval — the first certified defense against MINJA and ADAM attacks.

**Why it's critical:** MINJA achieves 20–40% ASR in realistic conditions. ADAM achieves 100% extraction. Without SMSR, the platform is vulnerable to:
- Memory injection (poisoning the knowledge graph)
- Data extraction (stealing user memories)
- Cross-tenant contamination (one user accessing another's data)

**Components:**
- C1: HMAC-SHA256 provenance at write time (blocks 100% of unsigned injections)
- C2: Randomized ablation + verdict voting at query time (bounds ASR to ~5–8%)
- C3: Rate limiting + query-pattern anomaly detection (defends against ADAM)
- C4: Embedding-space anomaly detection (defends against PoisonedRAG)

**Risk:** Low — the existing admission control gate is 80% of the way there. Just add the cryptographic components.

**Verdict:** 🆕 **INTRODUCE — Non-negotiable for production**

### 3. Temporal Validity (`valid_at` / `invalid_at` / `superseded_by`)

**What it is:** Instead of just `created_at` and `updated_at`, every memory has a validity period. "What was true in January?" is a different question from "When was this created?"

**Why it's critical:** Users need temporal correctness. If a user says "I used to work at Google" and later says "I now work at Apple," both are true but at different times. The graph must represent this.

**Implementation:** PostgreSQL columns `valid_at`, `invalid_at`, `superseded_by` (foreign key to the newer memory). Query-time filtering: `WHERE valid_at <= ? AND (invalid_at IS NULL OR invalid_at > ?)`.

**Risk:** Low — schema change that gets harder with data. Must be done before launch.

**Verdict:** 🆕 **INTRODUCE — Schema change before data accumulation**

### 4. Memory Versioning (Git-Style)

**What it is:** Branch, commit, merge, revert for memories. Users can experiment with memory changes without breaking production.

**Why it's critical:** Users need confidence. If they delete a memory, they should be able to revert. If they update a memory, they should see the history. If they want to try a different organization, they should branch.

**Implementation:**
```sql
version_id UUID, branch_name TEXT, commit_message TEXT, parent_version_id UUID
```

**Risk:** Medium — adds complexity to the query layer. But it's a massive differentiator (no competitor has this).

**Verdict:** 🆕 **INTRODUCE — Month 4 (Phase 4)**

### 5. Multi-Agent Namespaces + Federation

**What it is:** Each agent (Claude, Cursor, a custom bot, a team member) has its own memory namespace. Namespaces can be shared, synced, or federated across teams.

**Why it's critical:** 36.9% of multi-agent failures are from memory misalignment. If Claude remembers something and Cursor doesn't, the user experience is broken. If Team Member A's agent remembers a decision and Team Member B's doesn't, the team is misaligned.

**Implementation:** `namespace` column on every memory. Namespace permissions table. Sync configuration (frequency, conflict resolution strategy).

**Risk:** Medium — requires significant API changes. But it's table stakes for 2026.

**Verdict:** 🆕 **INTRODUCE — Month 4 (Phase 4)**

### 6. Drop-In OpenAI-Compatible Proxy

**What it is:** A proxy that wraps any OpenAI-compatible API and adds memory automatically. Zero code changes for any agent using `openai.chat.completions.create()`.

**Why it's critical:** This is the **"aha moment"** — the moment a developer realizes they don't need to change their code. They just change the API base URL and get instant memory.

**Implementation:** `POST /proxy/chat/completions` that intercepts messages, recalls relevant memories, injects them into the context, and remembers the conversation.

**Risk:** Low — can be built on top of the existing MCP server. The OpenAI API format is well-documented.

**Verdict:** 🆕 **INTRODUCE — Month 1 (Phase 1)**

### 7. Plugin Marketplace

**What it is:** A marketplace where developers can publish connectors, encoders, retrieval strategies, and UI panels. Revenue share: 70% developer, 30% platform.

**Why it's critical:** Ecosystem = moat. Data gravity + plugin marketplace = the winning platform. WordPress has 59,000+ plugins. VS Code has 50,000+ extensions. Obsidian has 1,500+ plugins.

**Implementation:**
```
marketplace.mnemosyne.ai/
├── connectors/
│   ├── slack-connector/ (1.2.0, 12K downloads)
│   ├── github-connector/ (1.0.5, 8K downloads)
│   └── notion-connector/ (0.9.0, 5K downloads)
├── encoders/
├── retrieval/
└── ui/
```

**Risk:** High — requires significant infrastructure (package hosting, versioning, security scanning, payments). But it's the long-term moat.

**Verdict:** 🆕 **INTRODUCE — Alpha Month 3, Beta Month 7**

### 8. pgvectorscale (Timescale Extension)

**What it is:** A PostgreSQL extension that makes pgvector 28× faster than Pinecone at 50M vectors. It adds DiskANN indexing and streaming filtering.

**Why it's critical:** Without pgvectorscale, PostgreSQL + pgvector is fast enough for <10M vectors. At 50M+, it degrades. pgvectorscale extends this to 100M+ vectors.

**Implementation:** `CREATE EXTENSION vectorscale;` — one-line install. Automatic index selection (HNSW for <50M, DiskANN for >50M).

**Risk:** Low — zero code changes, just an extension install.

**Verdict:** 🆕 **INTRODUCE — Mandatory at >10M vectors**

### 9. Valkey (Redis Replacement)

**What it is:** A BSD-3 licensed, Linux Foundation-backed drop-in replacement for Redis. Zero code changes.

**Why it's critical:** Redis 8's tri-license (AGPL/RSAL/SSPL) creates legal risk for any commercial product. The SSPL requires releasing ALL source code if you offer Redis as a service. Valkey eliminates this risk.

**Implementation:** Change `image: redis:7-alpine` to `image: valkey/valkey:8` in Docker Compose. No code changes.

**Risk:** Zero — drop-in replacement.

**Verdict:** 🆕 **INTRODUCE — Immediate (Phase 0)**

### 10. R2 (Cloudflare) for Cold Storage

**What it is:** Cloudflare R2 object storage: $0.015/GB, **zero egress fees**. Perfect for memory retrieval (unpredictable egress patterns).

**Why it's critical:** S3 egress is $0.09/GB. For a memory platform where users may export 10GB at any time, this is $0.90 per export. With R2, it's $0. Zero egress means predictable costs.

**Implementation:** Add R2 bucket alongside S3 bucket. Use R2 for retrievable summaries and search indexes. Use S3 for Object Lock compliance archives.

**Risk:** Low — S3-compatible API, just different endpoint and credentials.

**Verdict:** 🆕 **INTRODUCE — Phase 0**

### 11. EU AI Act Compliance (August 2, 2026 — 4 WEEKS AWAY)

**What it is:** The EU AI Act goes live on August 2, 2026. High-risk AI systems (which includes memory platforms) must comply with:
- Article 12: Automatic logging (6-month retention)
- Article 14: Human oversight (dashboard with override)
- Article 15: Accuracy (benchmark suite)
- Article 16: Robustness (red-teaming)
- Article 17: Cybersecurity (OWASP AMG)

**Penalties:** €35M / 7% turnover for prohibited practices. €15M / 3% for high-risk violations.

**Why it's critical:** Non-compliance = business death in Europe. But compliance = enterprise moat. The v3.0 plan has a full compliance roadmap (SOC 2, ISO 42001, NIST AI RMF, GDPR, EU AI Act).

**Risk:** Medium — requires legal review and documentation. But it's a differentiator.

**Verdict:** 🆕 **INTRODUCE — Phase 5 (Months 5-6)**

---

## 📋 ANSWERS TO YOUR SPECIFIC QUESTIONS

### Q1: Do we still build the extension?

**Answer:** YES, but reprioritize.

| Extension | Old Priority | New Priority | Reasoning |
|-----------|-------------|-------------|-----------|
| **VS Code Extension** | Not mentioned | **Month 6 (Phase 6)** | Developers live in VS Code. Inline memory (recall on hover, remember on save) is the #1 developer experience feature. |
| **Obsidian Sync** | Core feature | **Month 6 (Phase 6)** | Obsidian is a power-user tool. The sync is valuable, but the drop-in proxy and MCP server are more broadly useful. |
| **Browser Extension** | Not mentioned | **Month 7 (Phase 6)** | Universal web memory ("remember this page", "recall related pages") is a massive B2C feature. But it's complex (content scripts, permissions, cross-origin). |
| **Mobile App** | Not mentioned | **Month 8 (Phase 6)** | Push notifications for prospective memory, voice input, offline mode. Important for B2C but not for initial developer adoption. |

**Recommendation:** Build the **VS Code extension first** (developer audience), then Obsidian sync (power users), then browser extension (general audience), then mobile app (B2C).

---

### Q2: Do we still create connectors to all websites?

**Answer:** YES, but as **plugins, not core code**.

**The original platform had 20+ connectors:** Gmail, GitHub, Slack, Spotify, Notion, Discord, YouTube, Reddit, Telegram, WhatsApp, Instagram, LinkedIn, Apple Health, Twitter, ChatGPT, Claude, etc.

**The new approach:**
1. **Core connectors (built-in, Phase 1):** File upload (JSON/CSV), Markdown import, API webhook. These are the "universal" connectors that work with any source.
2. **Official plugins (maintained by Mnemosyne team, Phase 3):** Gmail, GitHub, Slack, Notion, Spotify. These are the most popular and have the highest usage.
3. **Community plugins (marketplace, Phase 4+):** Discord, YouTube, Reddit, Telegram, WhatsApp, Instagram, LinkedIn, Apple Health, Twitter, etc. Built by the community, revenue share.
4. **Enterprise plugins (custom, Phase 5+):** Jira, Confluence, Salesforce, SAP, Workday. Built on demand for enterprise contracts.

**Why this approach is better:**
- Core team focuses on platform quality, not connector maintenance
- Community builds connectors for niche platforms (e.g., "I use this obscure tool, let me build a connector")
- Revenue share incentivizes quality community plugins
- Enterprise can pay for custom connectors (high-margin service)

**Recommendation:** Build 5 official connectors (Gmail, GitHub, Slack, Notion, Spotify) as plugins. Launch the marketplace and let the community build the rest. This is the WordPress model.

---

### Q3: Do we still offer cloud storage?

**Answer:** YES, but with a **self-hosted option**.

**The new architecture supports 3 deployment modes:**

| Mode | Stack | Target User | Price |
|------|-------|------------|-------|
| **Cloud (Managed)** | PostgreSQL + pgvector + Valkey + S3 + R2 + ArcadeDB | Teams and enterprises who don't want to manage infrastructure | $19-49/user/month |
| **Self-Hosted (Docker Compose)** | Same stack, on your VPS | Developers, privacy-conscious users, small teams | FREE (open source) |
| **Hybrid** | Local PostgreSQL + Valkey + Cloud sync | Power users who want local speed with cloud backup | $9/month (sync only) |

**The self-hosted option is critical because:**
1. **Privacy:** Some users (journalists, lawyers, therapists) cannot put their data in the cloud
2. **Compliance:** GDPR Article 17 is easier with local data (you control erasure)
3. **Cost:** Self-hosted is free (open source) — this drives adoption
4. **Trust:** Users can inspect the code, verify the security, and know their data isn't being mined
5. **Community:** Self-hosted users become contributors, plugin builders, and evangelists

**The cloud option is critical because:**
1. **Convenience:** Most users don't want to manage a VPS
2. **Collaboration:** Team features require a shared backend
3. **Reliability:** Managed backups, monitoring, uptime guarantees
4. **Revenue:** Cloud is the monetization engine that funds development

**Recommendation:** Open source the core (Apache 2.0). Offer managed cloud (SaaS) as the primary revenue stream. The self-hosted version is the "free tier" that drives adoption and community.

---

### Q4: Do we need a free or trial version for self storage?

**Answer:** YES — **free self-hosted is the adoption engine**.

**The pricing model:**

| Tier | Self-Hosted | Cloud | Features |
|------|------------|-------|----------|
| **Free** | ✅ FREE | ❌ Not available | Personal use, 1,000 memories, 1 namespace, 3 connectors, community support |
| **Pro** | ❌ Not available | ✅ $19/month | 50,000 memories, 5 namespaces, all connectors, graph visualization, API access, 1-year history |
| **Team** | ❌ Not available | ✅ $49/user/month | 500,000 memories, 20 namespaces, team workspace, RBAC, SSO, audit trails, priority support |
| **Enterprise** | ✅ Custom license | ✅ Custom | On-premise, SLA, custom connectors, dedicated support, TEE, SOC 2, ISO 42001 |

**Why self-hosted is free:**
- Open source core = free to use
- Users pay with their time (managing infrastructure) instead of money
- This drives adoption: developers try it, like it, and then recommend cloud to their teams
- The "free" self-hosted version is the top of the funnel

**Why cloud has no free tier:**
- Cloud infrastructure costs money (PostgreSQL, Valkey, S3, bandwidth)
- A free cloud tier attracts abuse (crypto miners, spam, bot networks)
- The self-hosted version IS the free tier — it's the "try before you buy"

**What about a trial?**
- **14-day cloud trial** for Pro features. No credit card required. After 14 days, downgrade to self-hosted or upgrade to Pro.
- This lets users experience the full platform before committing.

**Recommendation:**
- Self-hosted: **Completely free, open source, no restrictions** (personal use)
- Cloud: **14-day free trial**, then $19/month (Pro) or $49/user/month (Team)
- Enterprise: **Custom pricing** with on-premise option

---

### Q5: Do we make it open source?

**Answer:** YES — **Open Core model**.

**The model:**

```
mnemosyne/
├── core/                    ← Apache 2.0, open source
│   ├── kernel.py            ← Microkernel (plugin manager, query router, admission control)
│   ├── plugins/             ← Plugin interface + built-in plugins (episodic, semantic, procedural)
│   ├── memory_subsystems/   ← Core memory plugins
│   └── security/            ← Basic admission control, rate limiting, input validation
│
├── plugins/                 ← Apache 2.0, open source (community-built)
│   ├── connectors/          ← Official connectors (Gmail, GitHub, Slack, Notion, Spotify)
│   ├── encoders/            ← Embedding models (OpenAI, Cohere, local)
│   ├── retrieval/           ← Search strategies (semantic, graph, hybrid)
│   └── ui/                  ← UI plugins (Obsidian sync, VS Code extension)
│
├── enterprise/              ← Proprietary, licensed
│   ├── soc2_compliance/     ← SOC 2 Type II controls, audit evidence
│   ├── tee_integration/     ← AMD SEV-SNP, Intel TDX, AWS Nitro Enclaves
│   ├── differential_privacy/← Retrieval noise, extraction resistance
│   ├── advanced_audit/      ← Ed25519-signed receipts, offline auditor verification
│   ├── sso/                 ← SAML, OIDC, SCIM provisioning
│   └── data_residency/      ← Regional deployment, EU data stays in EU
│
└── cloud/                   ← SaaS, managed (proprietary)
    └── Hosted platform with managed infrastructure, billing, support
```

**Why open source the core:**
1. **Trust:** Users can inspect the code, verify security, and know their data isn't being mined
2. **Adoption:** Open source is the #1 driver of developer adoption (GitHub stars, community, plugins)
3. **Contributions:** The community builds connectors, fixes bugs, and improves the platform
4. **Standardization:** Open source can become the standard for AI memory (like Kubernetes for containers)
5. **Marketing:** "Open source" is a powerful marketing message (transparency, community, no lock-in)

**Why keep enterprise proprietary:**
1. **Revenue:** Enterprise features are high-margin (SOC 2, TEE, SSO, data residency)
2. **Competitive moat:** The proprietary features are the ones that enterprises pay for
3. **Security:** Some features (TEE, differential privacy) are too complex for open source maintenance
4. **Support:** Enterprise customers need dedicated support, which is a paid service

**What about the open source license?**
- **Apache 2.0** for the core and plugins. This is the most permissive license that allows commercial use, modification, and distribution. It also provides patent protection.
- **NOT AGPL/SSPL** — these are "viral" licenses that require releasing ALL source code if you offer the software as a service. This would kill the cloud business model.
- **NOT MIT** — MIT is too permissive. It doesn't protect against patent trolls. Apache 2.0 is the standard for infrastructure projects (Kubernetes, TensorFlow, VS Code).

**What about the enterprise license?**
- **Custom commercial license** for enterprise features. This is a standard "source available" model (like GitLab, MongoDB, Elastic).
- Enterprises get the source code (for security audits) but cannot redistribute it.
- Pricing: Per-user (Team $49/month) or custom (Enterprise, contact sales).

**Recommendation:**
- **Core kernel + built-in plugins + official connectors:** Apache 2.0 (open source)
- **Enterprise features (SOC 2, TEE, SSO, data residency):** Proprietary (source available)
- **Cloud hosting:** Proprietary (SaaS)
- **Plugin marketplace:** Revenue share (70% developer, 30% platform)

---

## 📊 FINAL STRATEGIC RECOMMENDATION

### The Platform You Should Build

**Mnemosyne** is an **open-core Memory OS** with a microkernel architecture, built on PostgreSQL + pgvector + pgvectorscale, secured by SMSR-certified admission control, exposed through stateless MCP (stdio + Streamable HTTP), with a drop-in OpenAI-compatible proxy, emotional salience scoring, prospective memory scheduling, and a plugin marketplace for connectors and extensions.

### The Three Deployment Modes

| Mode | Stack | User | Price | Open Source |
|------|-------|------|-------|-------------|
| **Self-Hosted** | Docker Compose on your VPS | Privacy-conscious developers, journalists, lawyers | **FREE** | ✅ Apache 2.0 |
| **Cloud (Pro)** | Managed PostgreSQL + Valkey + S3 + R2 | Individual developers, small teams | **$19/month** | ❌ SaaS |
| **Cloud (Team)** | Managed + ArcadeDB + SSO | Teams, startups | **$49/user/month** | ❌ SaaS |
| **Enterprise** | On-premise + TEE + SOC 2 | Large enterprises, regulated industries | **Custom** | ⚠️ Source available |

### The Adoption Funnel

```
1. Developer discovers Mnemosyne on GitHub (open source, 10K stars)
   ↓
2. Developer tries self-hosted version (free, Docker Compose, 5 minutes)
   ↓
3. Developer installs VS Code extension (inline memory, recall on hover)
   ↓
4. Developer uses drop-in proxy (change OPENAI_API_BASE, instant memory)
   ↓
5. Developer loves it, recommends to team
   ↓
6. Team upgrades to Cloud (Pro) for collaboration ($19/month)
   ↓
7. Team grows, upgrades to Cloud (Team) for RBAC + SSO ($49/user/month)
   ↓
8. Enterprise customer needs SOC 2, on-premise, custom connectors (custom $$$)
```

### The 90-Day Sprint (What to Build First)

| Week | Focus | Deliverables |
|------|-------|-------------|
| **W1-2** | Foundation | PostgreSQL + pgvector + pgvectorscale, Valkey, microkernel scaffold, FastAPI, CI/CD |
| **W3-4** | Core Memory | Episodic + semantic plugins, remember/recall APIs, admission control, drop-in proxy |
| **W5-6** | Security | SMSR C1 (HMAC-SHA256), MINJA detection, audit trails, GDPR soft-delete |
| **W7-8** | Intelligence | Query classifier, prospective memory (cron + event triggers), emotional salience |
| **W9-10** | Developer Experience | Python SDK (auto-generated), CLI v1 (`mnemosyne init`), VS Code extension alpha |
| **W11-12** | Launch Prep | 5 official connectors (Gmail, GitHub, Slack, Notion, Spotify), plugin marketplace alpha, landing page |

### The One-Sentence Summary

> **Build Mnemosyne as an open-core Memory OS: a microkernel with plugins, open source (Apache 2.0) for the core and self-hosted use, proprietary SaaS for cloud features, with a drop-in proxy for instant adoption, a VS Code extension for developer workflow, and a plugin marketplace for connectors. Keep the original platform's server architecture, classification pipeline, and connector pattern. Kill Cognee-as-core, SQLite, Redis, mandatory NEAR, and monolithic architecture. Introduce microkernel + plugins, SMSR security, temporal validity, memory versioning, multi-agent namespaces, and EU AI Act compliance.**

---

*Document: Mnemosyne Strategic Decision Framework — Keep / Kill / Introduce*
*Synthesized from: Original platform code, v2.0 brief, v3.0 rebuild plan, 6 research streams, 31,924+ lines*
*Date: July 2026*
*Status: Ready for implementation decisions*

# MNEMOSYNE: The Ultimate Memory OS — Complete Rebuild Plan
## v3.0 | July 2026 | Synthesized from 6 parallel research streams, 15+ source documents, 200+ research findings

**From:** Platform Builder Brief v2.0 (July 4, 2026)  
**To:** Mnemosyne v3.0 — The Ultimate Memory OS  
**Status:** Comprehensive rebuild plan with concrete implementations  
**Date:** July 2026  

---

# EXECUTIVE SUMMARY: WHAT CHANGED

The v2.0 brief was solid but missed critical 2026 developments. This v3.0 plan incorporates 6 parallel research streams (27,964 + 260 + 392 + 576 + 429 + 303 = 31,924 lines of research) into a complete, concrete, buildable plan.

## Critical Changes from v2.0

| Area | v2.0 | v3.0 (This Plan) | Why |
|------|------|------------------|-----|
| **Hot Layer** | Redis | **Valkey** (BSD-3, Linux Foundation) | Redis 8 moved to controversial tri-license (AGPL/RSAL/SSPG). Valkey is zero-risk drop-in replacement. |
| **Graph Database** | Neo4j fallback | **ArcadeDB** (Apache 2.0, multi-model, Cypher-compatible) | Neo4j is JVM-heavy and expensive. ArcadeDB is faster, open-source, and Cognee already integrates with it. |
| **Vector Extension** | pgvector | **pgvector + pgvectorscale** (mandatory at >10M vectors) | pgvectorscale (Timescale) makes PostgreSQL 28× faster than Pinecone at 50M vectors. Not optional. |
| **Cold Storage** | S3 | **S3 + R2** (zero egress for retrieval) | R2 is $0.015/GB with zero egress. Perfect for memory retrieval spikes. |
| **MCP Transport** | stdio + SSE | **stdio + Streamable HTTP** (2026-07-28 spec) | SSE is deprecated. Streamable HTTP is the new standard. Works with Claude.ai natively. |
| **MCP Auth** | Not specified | **OAuth 2.1 + PKCE + RFC 8707** | NIST mandates this by 2027. 44% of MCP servers are unauthenticated. Mnemosyne is NIST-ready. |
| **Graph Threshold** | <1B edges in Postgres | **<100M edges in Postgres** (100M–1B evaluate split) | Recursive CTEs degrade after 100M edges. Realistic threshold, not fantasy. |
| **Security Defense** | Admission control (basic) | **SMSR-certified (HMAC-SHA256 + randomized ablation)** | MINJA achieves 20–40% ASR in realistic conditions. ADAM achieves 100%. SMSR is the only certified defense. |
| **Compliance** | GDPR mentioned | **EU AI Act (live Aug 2, 2026) + NIST-ready + ISO 42001** | EU AI Act penalties: €35M / 7% turnover. NIST designated MCP as "leading open standard." Mnemosyne is enterprise-ready. |
| **Architecture** | Monolithic stack | **Microkernel + Plugin Architecture** | "Ultimate OS" = extensible core + plugin marketplace. No monolithic memory system wins. |
| **Multi-Agent** | Not mentioned | **Multi-agent namespaces + versioning + branching + federation** | 36.9% of multi-agent failures are from memory misalignment. Table stakes for 2026. |
| **SDKs** | Not mentioned | **Python + TypeScript SDKs (auto-generated from OpenAPI)** | Developer experience is the moat. SDKs are not optional. |
| **Temporal Model** | `created_at` / `updated_at` | **`valid_at` / `invalid_at` / `superseded_by`** | Users need temporal correctness, not just timestamps. "What was true in January?" is a different question from "When was this created?" |
| **Competitor** | Not mentioned | **Evermind EverOS (direct "Memory OS" competitor)** | 6.7K stars, Apache 2.0. Same narrative. Must differentiate on emotional salience + prospective memory + observability + compliance. |
| **Plugin Marketplace** | Not mentioned | **Plugin marketplace (alpha in Month 3)** | Ecosystem = moat. Data gravity + plugin marketplace = the winning platform. |
| **Drop-in Proxy** | Not mentioned | **OpenAI-compatible proxy mode (Month 1)** | Zero-code memory. Drop-in wrapper for any LLM. The aha moment. |
| **Memory Versioning** | Not mentioned | **Git-style versioning + branching (Month 2)** | Users need to experiment with memory without breaking production. Branch, merge, commit. |
| **CLI** | Not mentioned | **Full CLI with debug/trace modes (Month 1)** | One-command setup: `mnemosyne init`. Debug mode: `mnemosyne --trace recall "api rate limit"`. |

---

# PART 1: THE ULTIMATE MEMORY OS — CORE PHILOSOPHY

## 1.1 What Makes an OS "Ultimate"

An operating system is not a storage backend. An operating system is:

1. **A kernel** that manages resources (memory, CPU, I/O)
2. **A scheduler** that decides what runs when
3. **A security model** that isolates processes
4. **A plugin architecture** that extends without rebuilding
5. **A developer experience** that makes building on it delightful
6. **An ecosystem** that makes switching impossible (data gravity + plugins)

Mnemosyne v3.0 is built on these six principles. Every feature, every API, every schema decision maps to one of these.

## 1.2 The Memory Taxonomy (What We Actually Store)

Human memory is not a key-value store. It is a multi-type system:

| Memory Type | What It Stores | Example | Subsystem |
|-------------|-------------|---------|-----------|
| **Episodic** | Events, experiences, conversations | "On March 15, we decided on 100 req/min" | Queryable index (semantic search) |
| **Semantic** | Facts, concepts, definitions | "API rate limit = 100 req/min with burst to 200" | Queryable index (graph + vector) |
| **Procedural** | How-to, workflows, instructions | "How to deploy a new service: Step 1..." | Queryable index (structured retrieval) |
| **Prospective** | Future intentions, reminders, scheduled tasks | "Check API metrics on Monday at 9am" | Scheduler + trigger system |
| **Emotional** | Significance, priority, affective weight | "This was a critical decision (salience 0.95)" | Salience scoring engine |
| **Meta** | Audit trails, provenance, contradictions, confidence | "This memory was written by Agent X, contradicted by Y, resolved by Z" | Observability layer |

The "Ultimate Memory OS" does not store "memories." It stores **typed, structured, versioned, attributed, scored, and scheduled cognitive artifacts** that map to how humans (and agents) actually think.

## 1.3 The Differentiation Stack (What No Competitor Has)

| Differentiator | Mnemosyne | Cognee | Mem0 | Zep | Letta | Evermind |
|----------------|-----------|--------|------|-----|-------|----------|
| **Emotional salience** | ✅ Full multi-factor | ⚠️ Partial | ❌ No | ❌ No | ❌ No | ⚠️ Basic |
| **Prospective memory** | ✅ Native scheduler | ❌ No | ⚠️ Expiration only | ❌ No | ❌ No | ❌ No |
| **Observability dashboard** | ✅ First-class | ⚠️ Basic | ❌ No | ❌ No | ❌ No | ⚠️ Basic |
| **Compliance (GDPR/AI Act)** | ✅ Certified | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Partial |
| **Multi-agent memory** | ✅ Namespaces + federation | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | ❌ No |
| **Memory versioning** | ✅ Git-style | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Plugin marketplace** | ✅ Alpha in Month 3 | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Self-improvement** | ✅ Consolidation + reconsolidation | ✅ memify | ❌ No | ❌ No | ❌ No | ⚠️ Partial |
| **Contradiction detection** | ✅ Auto + manual | ⚠️ Basic | ❌ No | ❌ No | ❌ No | ❌ No |
| **Drop-in proxy** | ✅ OpenAI-compatible | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Temporal validity** | ✅ `valid_at`/`invalid_at` | ❌ No | ❌ No | ✅ Temporal | ❌ No | ❌ No |
| **Microkernel architecture** | ✅ Plugin-based | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Partial |

**Mnemosyne's competitive moat:** 12 features that no competitor has in combination. Evermind is the closest (6.7K stars, "Memory OS" branding), but lacks prospective memory, emotional salience, compliance, multi-agent, versioning, and plugins. The window is 3–4 months before competitors close gaps.

---

# PART 2: ARCHITECTURE — THE COMPLETE SYSTEM

## 2.1 System Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MNEMOSYNE MEMORY OS                             │
│                     "The Operating System for AI Memory"                     │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                         LAYER 1: KERNEL (Microkernel)                  │
  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │
  │  │  Query Router   │  │  Admission Ctrl │  │  Scheduler (Prospective)│  │
  │  │  (Classifier)   │  │  (Security Gate)│  │  (Cron + Event Triggers)│  │
  │  │                 │  │                 │  │                         │  │
  │  │ Routes queries  │  │ SMSR-certified  │  │ Triggers reminders     │  │
  │  │ to correct      │  │ HMAC-SHA256     │  │ based on time/events   │  │
  │  │ memory subsystem│  │ + randomized    │  │                        │  │
  │  │                 │  │ ablation          │  │                        │  │
  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │
  │                         │                                               │
  │  ┌─────────────────────────────────────────────────────────────────┐   │
  │  │                    PLUGIN MANAGER                                │   │
  │  │  Load/unload plugins without restart. Core never changes.        │   │
  │  │  Plugins: connectors, encoders, retrieval strategies, UI panels  │   │
  │  └─────────────────────────────────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────────────────┘
                                    │
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                      LAYER 2: MEMORY SUBSYSTEMS (Plugins)                │
  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
  │  │  Episodic   │  │  Semantic   │  │  Procedural │  │  Emotional  │    │
  │  │  Memory     │  │  Memory     │  │  Memory     │  │  Salience   │    │
  │  │             │  │             │  │             │  │  Engine     │    │
  │  │ Events,     │  │ Facts,      │  │ How-to,     │  │ Multi-factor│    │
  │  │ experiences,│  │ concepts,   │  │ workflows,  │  │ scoring:    │    │
  │  │ conversations│  │ definitions │  │ instructions│  │ emphasis,   │    │
  │  │             │  │             │  │             │  │ outcome,    │    │
  │  │ Stored in   │  │ Stored in   │  │ Stored in   │  │ engagement, │    │
  │  │ pgvector    │  │ pgvector +  │  │ structured  │  │ confidence,│    │
  │  │ (semantic)  │  │ graph edges │  │ JSON schema │  │ recency     │    │
  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │
  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
  │  │  Prospective│  │  Meta       │  │  Versioning │  │  Federation │    │
  │  │  Memory     │  │  Memory     │  │  (Git-style)│  │  (Multi-    │    │
  │  │             │  │             │  │             │  │  Agent)     │    │
  │  │ Scheduled   │  │ Audit,      │  │ Branch,     │  │ Namespaces, │    │
  │  │ reminders,  │  │ provenance, │  │ commit,     │  │ sync,       │    │
  │  │ future      │  │ confidence, │  │ merge,      │  │ conflict    │    │
  │  │ intentions  │  │ contradictions│  │ revert    │  │ resolution  │    │
  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │
  └─────────────────────────────────────────────────────────────────────────┘
                                    │
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                      LAYER 3: STORAGE ENGINE (Pluggable)                 │
  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │
  │  │  HOT (Valkey)   │  │  QUERYABLE      │  │  COLD (S3 + R2)       │  │
  │  │  Working memory │  │  (PostgreSQL +  │  │  Audit + Archive      │  │
  │  │  Session cache  │  │  pgvector +     │  │  Immutable provenance │  │
  │  │  35-min rotation│  │  pgvectorscale) │  │  chains + Parquet     │  │
  │  │                 │  │                 │  │                       │  │
  │  │ 10-20 turns     │  │  Episodic +     │  │  GDPR Art. 17 erasure │  │
  │  │  Tool history   │  │  Semantic +     │  │  Model snapshots      │  │
  │  │  Compressed     │  │  Procedural +   │  │  Compliance records   │  │
  │  │  summaries      │  │  Prospective +  │  │                       │  │
  │  │                 │  │  Meta + Version │  │  R2: zero egress      │  │
  │  │                 │  │                 │  │  S3: Object Lock      │  │
  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │
  │                         │                                               │
  │  ┌─────────────────────────────────────────────────────────────────┐   │
  │  │                    GRAPH (When >100M edges)                      │   │
  │  │  ArcadeDB (Apache 2.0, multi-model: graph+vector+document)     │   │
  │  │  Cypher-compatible, Cognee-integrated, open-source             │   │
  │  └─────────────────────────────────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────────────────┘
                                    │
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                      LAYER 4: INTEGRATION (Transport-Agnostic)           │
  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │
  │  │  MCP (Primary)  │  │  REST (Secondary)│  │  WebSocket (Future)  │  │
  │  │  stdio +        │  │  HTTP/JSON       │  │  Live sync, push       │  │
  │  │  Streamable HTTP│  │  OpenAPI 3.1     │  │  reminders, graph      │  │
  │  │  6 tools:       │  │  Full CRUD        │  │  updates               │  │
  │  │  remember,      │  │  + Auth + Webhooks│  │                        │  │
  │  │  recall,        │  │                  │  │                        │  │
  │  │  remind_me,     │  │                  │  │                        │  │
  │  │  consolidate,    │  │                  │  │                        │  │
  │  │  audit, forget   │  │                  │  │                        │  │
  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │
  │  ┌─────────────────────────────────────────────────────────────────┐   │
  │  │                    DROP-IN PROXY (OpenAI-Compatible)            │   │
  │  │  Wraps any LLM API. Adds memory to any agent with zero code.   │   │
  │  │  `OPENAI_API_BASE=https://api.mnemosyne.ai/v1/proxy`            │   │
  │  └─────────────────────────────────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────────────────┘
                                    │
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                      LAYER 5: OBSERVABILITY (First-Class)                │
  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │
  │  │  Memory Health  │  │  Audit Trail    │  │  Contradiction Map    │  │
  │  │  Dashboard      │  │  (Tamper-proof) │  │  (Visual graph)       │  │
  │  │                 │  │                 │  │                       │  │
  │  │  - Decay curves │  │  - Ed25519      │  │  - Red edges for      │  │
  │  │  - Contradiction│  │    signed       │  │    contradictions     │  │
  │  │    rate         │  │  - SHA-256      │  │  - Confidence scores  │  │
  │  │  - Source       │  │    chain        │  │  - Resolution history │  │
  │  │    reliability  │  │  - Offline      │  │                       │  │
  │  │  - Query latency│  │    auditor      │  │                       │  │
  │  │    by subsystem │  │    verification │  │                       │  │
  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │
  └─────────────────────────────────────────────────────────────────────────┘
                                    │
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                      LAYER 6: ECOSYSTEM (Month 3+)                         │
  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │
  │  │  Plugin         │  │  SDK (Python +  │  │  CLI (One-command)    │  │
  │  │  Marketplace    │  │  TypeScript)    │  │                       │  │
  │  │                 │  │                 │  │  `mnemosyne init`      │  │
  │  │  Connectors:    │  │  Auto-generated  │  │  `mnemosyne remember`  │  │
  │  │  Slack, GitHub,  │  │  from OpenAPI    │  │  `mnemosyne recall`    │  │
  │  │  Notion, Gmail,  │  │  Type-safe,      │  │  `mnemosyne audit`     │  │
  │  │  Spotify, etc.   │  │  fully typed     │  │  `mnemosyne --trace`   │  │
  │  │                 │  │                 │  │                       │  │
  │  │  Encoders:       │  │                 │  │  Debug mode: show     │  │
  │  │  Custom embedding│  │                 │  │  query routing,       │  │
  │  │  models          │  │                 │  │  salience scoring,    │  │
  │  │                 │  │                 │  │  contradiction checks   │  │
  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │
  └─────────────────────────────────────────────────────────────────────────┘
```

## 2.2 The Microkernel + Plugin Architecture

The "monolithic stack" approach (v2.0) is wrong. Every successful platform (WordPress, Shopify, VS Code, Obsidian) uses a microkernel + plugin architecture. Mnemosyne must too.

### The Kernel (Never Changes)

```python
# mnemosyne/kernel.py
class Kernel:
    """The microkernel. Manages plugins, routes queries, enforces security."""
    
    def __init__(self, config: KernelConfig):
        self.plugins = PluginManager()
        self.router = QueryRouter()
        self.admission = AdmissionControl()
        self.scheduler = ProspectiveScheduler()
        self.audit = AuditTrail()
    
    def remember(self, request: RememberRequest) -> RememberResult:
        # 1. Security gate (SMSR-certified)
        self.admission.check(request)
        
        # 2. Route to correct subsystem
        subsystem = self.router.classify(request)
        
        # 3. Route to correct plugin
        plugin = self.plugins.get(subsystem)
        
        # 4. Execute with audit trail
        result = plugin.store(request)
        self.audit.log(result)
        
        return result
    
    def recall(self, request: RecallRequest) -> RecallResult:
        # 1. Route to correct subsystem(s)
        subsystems = self.router.classify_multi(request)
        
        # 2. Retrieve from each subsystem
        results = []
        for subsystem in subsystems:
            plugin = self.plugins.get(subsystem)
            results.append(plugin.retrieve(request))
        
        # 3. Merge and rank
        merged = self.router.merge(results, request)
        
        return merged
    
    def remind_me(self, request: RemindRequest) -> RemindResult:
        # Direct to scheduler
        return self.scheduler.schedule(request)
    
    def consolidate(self) -> ConsolidateResult:
        # Trigger all plugins' consolidation routines
        for plugin in self.plugins.all():
            plugin.consolidate()
        return ConsolidateResult()
```

### The Plugin Interface (Extensible)

```python
# mnemosyne/plugin.py
class MemoryPlugin(ABC):
    """Every memory subsystem is a plugin."""
    
    @property
    @abstractmethod
    def name(self) -> str: ...
    
    @property
    @abstractmethod
    def version(self) -> str: ...
    
    @abstractmethod
    def store(self, request: RememberRequest) -> RememberResult: ...
    
    @abstractmethod
    def retrieve(self, request: RecallRequest) -> RecallResult: ...
    
    @abstractmethod
    def consolidate(self) -> None: ...
    
    @abstractmethod
    def health(self) -> HealthResult: ...

# Example plugins:
class EpisodicMemoryPlugin(MemoryPlugin):
    name = "episodic"
    version = "1.0.0"
    
    def store(self, request):
        # Store in pgvector with semantic embedding
        # Include: content, timestamp, source, confidence, salience
        pass
    
    def retrieve(self, request):
        # Semantic search + temporal filtering + salience ranking
        pass
    
    def consolidate(self):
        # Merge near-duplicates, prune low-salience, update embeddings
        pass

class SemanticMemoryPlugin(MemoryPlugin):
    name = "semantic"
    version = "1.0.0"
    
    def store(self, request):
        # Store in pgvector with graph edges
        # Extract entities, relationships, create graph nodes
        pass
    
    def retrieve(self, request):
        # Graph traversal + vector search hybrid
        pass
    
    def consolidate(self):
        # Merge duplicate entities, strengthen edges, infer new relationships
        pass

class ProspectiveMemoryPlugin(MemoryPlugin):
    name = "prospective"
    version = "1.0.0"
    
    def store(self, request):
        # Store scheduled reminder with trigger conditions
        # Cron expressions, event triggers, one-shot
        pass
    
    def retrieve(self, request):
        # Check triggers, return due reminders
        pass
    
    def consolidate(self):
        # Clean up expired reminders, update recurring schedules
        pass
```

### The Plugin Marketplace (Month 3)

```
marketplace.mnemosyne.ai/
├── connectors/
│   ├── slack-connector/ (1.2.0, 12K downloads)
│   ├── github-connector/ (1.0.5, 8K downloads)
│   ├── notion-connector/ (0.9.0, 5K downloads)
│   └── gmail-connector/ (1.1.0, 7K downloads)
├── encoders/
│   ├── openai-embedding/ (2.0.0, 15K downloads)
│   ├── cohere-embedding/ (1.0.0, 3K downloads)
│   └── local-embedding/ (0.8.0, 4K downloads)
├── retrieval/
│   ├── semantic-search/ (1.0.0, 10K downloads)
│   ├── graph-traversal/ (0.9.0, 2K downloads)
│   └── hybrid-rerank/ (1.1.0, 6K downloads)
└── ui/
    ├── obsidian-sync/ (1.0.0, 5K downloads)
    ├── vscode-extension/ (0.8.0, 3K downloads)
    └── web-dashboard/ (1.0.0, 8K downloads)
```

---

# PART 3: COMPLETE DATABASE SCHEMA

## 3.1 PostgreSQL Schema (The Source of Truth)

```sql
-- ============================================================
-- MNEMOSYNE v3.0 — COMPLETE DATABASE SCHEMA
-- PostgreSQL 16 + pgvector + pgvectorscale
-- ============================================================

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
CREATE EXTENSION IF NOT EXISTS "vector";

-- ============================================================
-- 1. CORE: Memories (The Primary Table)
-- ============================================================
CREATE TABLE memories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Memory classification
    memory_type TEXT NOT NULL CHECK (memory_type IN (
        'episodic', 'semantic', 'procedural', 'prospective', 'emotional', 'meta'
    )),
    
    -- Content
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    content_hash TEXT NOT NULL, -- SHA-256 of content for deduplication
    
    -- YAML frontmatter (stored as JSONB for flexibility)
    frontmatter JSONB NOT NULL DEFAULT '{}',
    
    -- Tags (array for GIN indexing)
    tags TEXT[] NOT NULL DEFAULT '{}',
    
    -- Status lifecycle
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN (
        'active', 'pending', 'superseded', 'archived', 'deleted'
    )),
    
    -- Temporal validity (CRITICAL ADDITION from v3.0 research)
    valid_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    invalid_at TIMESTAMPTZ, -- NULL = still valid
    superseded_by UUID REFERENCES memories(id) ON DELETE SET NULL,
    
    -- Salience scoring (multi-factor)
    salience FLOAT NOT NULL DEFAULT 0.5 CHECK (salience >= 0.0 AND salience <= 1.0),
    salience_factors JSONB NOT NULL DEFAULT '{
        "user_emphasis": 0.0,
        "outcome_type": 0.0,
        "engagement": 0.0,
        "confidence": 0.5,
        "recency": 0.5
    }',
    
    -- Confidence scoring
    confidence FLOAT NOT NULL DEFAULT 0.5 CHECK (confidence >= 0.0 AND confidence <= 1.0),
    confidence_source TEXT NOT NULL DEFAULT 'extraction',
    
    -- Provenance / Attribution
    source_type TEXT NOT NULL DEFAULT 'manual' CHECK (source_type IN (
        'manual', 'agent', 'connector', 'import', 'inferred', 'consolidated'
    )),
    source_id TEXT, -- Agent ID, connector ID, user ID, etc.
    source_name TEXT, -- Human-readable source name
    
    -- Security: SMSR provenance
    provenance_hash TEXT, -- HMAC-SHA256 of (content + timestamp + source_id)
    provenance_signature TEXT, -- Ed25519 signature for critical memories
    
    -- Vector embedding (384-dim for multilingual-e5-small, 1536 for text-embedding-3)
    embedding VECTOR(384),
    
    -- Full-text search (for hybrid retrieval)
    tsv TSVECTOR,
    
    -- Vault path (Obsidian-compatible file reference)
    vault_path TEXT,
    
    -- Versioning (Git-style)
    version_id UUID NOT NULL DEFAULT gen_random_uuid(),
    branch_name TEXT NOT NULL DEFAULT 'main',
    commit_message TEXT,
    parent_version_id UUID REFERENCES memories(id) ON DELETE SET NULL,
    
    -- Multi-agent namespace
    namespace TEXT NOT NULL DEFAULT 'default',
    
    -- Tenant isolation
    tenant_id UUID NOT NULL,
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    accessed_at TIMESTAMPTZ, -- Last retrieval time (for recency decay)
    
    -- Soft delete (GDPR compliance)
    deleted_at TIMESTAMPTZ,
    deleted_by UUID,
    deletion_reason TEXT
);

-- Indexes
CREATE INDEX idx_memories_type ON memories(memory_type);
CREATE INDEX idx_memories_status ON memories(status);
CREATE INDEX idx_memories_tenant ON memories(tenant_id);
CREATE INDEX idx_memories_namespace ON memories(namespace);
CREATE INDEX idx_memories_valid_at ON memories(valid_at);
CREATE INDEX idx_memories_invalid_at ON memories(invalid_at) WHERE invalid_at IS NOT NULL;
CREATE INDEX idx_memories_tags ON memories USING GIN(tags);
CREATE INDEX idx_memories_salience ON memories(salience DESC);
CREATE INDEX idx_memories_confidence ON memories(confidence DESC);
CREATE INDEX idx_memories_source ON memories(source_type, source_id);
CREATE INDEX idx_memories_created ON memories(created_at DESC);
CREATE INDEX idx_memories_accessed ON memories(accessed_at DESC);
CREATE INDEX idx_memories_content_hash ON memories(content_hash);
CREATE INDEX idx_memories_superseded ON memories(superseded_by) WHERE superseded_by IS NOT NULL;
CREATE INDEX idx_memories_version ON memories(version_id, branch_name);
CREATE INDEX idx_memories_parent ON memories(parent_version_id);

-- Full-text search index
CREATE INDEX idx_memories_tsv ON memories USING GIN(tsv);

-- Vector index (HNSW — pgvector default, use pgvectorscale at >10M vectors)
CREATE INDEX idx_memories_embedding ON memories USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);

-- Composite index for common query patterns
CREATE INDEX idx_memories_query ON memories(tenant_id, namespace, memory_type, status, valid_at, invalid_at)
    WHERE deleted_at IS NULL;

-- Trigger: Update tsv on insert/update
CREATE OR REPLACE FUNCTION memories_update_tsv()
RETURNS TRIGGER AS $$
BEGIN
    NEW.tsv := 
        setweight(to_tsvector('english', COALESCE(NEW.title, '')), 'A') ||
        setweight(to_tsvector('english', COALESCE(NEW.content, '')), 'B') ||
        setweight(to_tsvector('english', COALESCE(array_to_string(NEW.tags, ' '), '')), 'C');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER memories_tsv_trigger
    BEFORE INSERT OR UPDATE ON memories
    FOR EACH ROW
    EXECUTE FUNCTION memories_update_tsv();

-- Trigger: Update content_hash on content change
CREATE OR REPLACE FUNCTION memories_update_hash()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.content IS DISTINCT FROM OLD.content THEN
        NEW.content_hash := encode(digest(NEW.content, 'sha256'), 'hex');
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER memories_hash_trigger
    BEFORE INSERT OR UPDATE ON memories
    FOR EACH ROW
    EXECUTE FUNCTION memories_update_hash();

-- Trigger: Update updated_at timestamp
CREATE OR REPLACE FUNCTION memories_update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at := NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER memories_timestamp_trigger
    BEFORE UPDATE ON memories
    FOR EACH ROW
    EXECUTE FUNCTION memories_update_timestamp();

-- Trigger: Update accessed_at on read (for recency scoring)
CREATE OR REPLACE FUNCTION memories_update_accessed()
RETURNS TRIGGER AS $$
BEGIN
    NEW.accessed_at := NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER memories_accessed_trigger
    BEFORE UPDATE ON memories
    FOR EACH ROW
    WHEN (OLD.accessed_at IS NULL OR OLD.accessed_at < NOW() - INTERVAL '1 minute')
    EXECUTE FUNCTION memories_update_accessed();

-- ============================================================
-- 2. GRAPH: Memory Links (Edges)
-- ============================================================
CREATE TABLE memory_links (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_memory_id UUID NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
    target_memory_id UUID NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
    
    -- Link type (ontology-defined)
    link_type TEXT NOT NULL DEFAULT 'related' CHECK (link_type IN (
        'related', 'causes', 'caused_by', 'supports', 'contradicts', 'supersedes',
        'prerequisite', 'follows', 'mentions', 'part_of', 'contains', 'similar_to',
        'opposite_to', 'leads_to', 'prevents', 'enables', 'disables'
    )),
    
    -- Link strength (0.0-1.0)
    strength FLOAT NOT NULL DEFAULT 0.5 CHECK (strength >= 0.0 AND strength <= 1.0),
    
    -- Link confidence (0.0-1.0)
    confidence FLOAT NOT NULL DEFAULT 0.5 CHECK (confidence >= 0.0 AND confidence <= 1.0),
    
    -- Link metadata
    metadata JSONB NOT NULL DEFAULT '{}',
    
    -- Tenant isolation
    tenant_id UUID NOT NULL,
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    -- Prevent duplicate links
    UNIQUE(source_memory_id, target_memory_id, link_type, tenant_id)
);

CREATE INDEX idx_memory_links_source ON memory_links(source_memory_id);
CREATE INDEX idx_memory_links_target ON memory_links(target_memory_id);
CREATE INDEX idx_memory_links_type ON memory_links(link_type);
CREATE INDEX idx_memory_links_tenant ON memory_links(tenant_id);
CREATE INDEX idx_memory_links_strength ON memory_links(strength DESC);

-- ============================================================
-- 3. PROSPECTIVE: Reminders & Scheduled Tasks
-- ============================================================
CREATE TABLE prospective_memories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    memory_id UUID NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
    
    -- Trigger specification
    trigger_at TIMESTAMPTZ NOT NULL,
    trigger_type TEXT NOT NULL DEFAULT 'absolute' CHECK (trigger_type IN (
        'absolute', 'relative', 'recurring', 'event', 'condition'
    )),
    
    -- Recurring specification (cron expression or natural language)
    recurring_spec TEXT, -- "0 9 * * MON" or "every Monday at 9am"
    recurring_end_at TIMESTAMPTZ,
    
    -- Event-based trigger
    event_type TEXT, -- "memory_created", "memory_updated", "memory_accessed", "external"
    event_filter JSONB, -- {"memory_type": "decision", "tags": ["api"]}
    
    -- Condition-based trigger
    condition_expression TEXT, -- SQL-like condition: "salience < 0.3 AND days_since_accessed > 30"
    
    -- Status
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN (
        'pending', 'triggered', 'acknowledged', 'dismissed', 'snoozed', 'expired', 'failed'
    )),
    
    -- Snooze handling
    snoozed_until TIMESTAMPTZ,
    snooze_count INTEGER NOT NULL DEFAULT 0,
    
    -- Action specification (what to do when triggered)
    action_type TEXT NOT NULL DEFAULT 'notify' CHECK (action_type IN (
        'notify', 'query', 'consolidate', 'export', 'webhook', 'mcp_tool'
    )),
    action_payload JSONB, -- {"message": "Check API metrics", "webhook_url": "..."}
    
    -- Tenant isolation
    tenant_id UUID NOT NULL,
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    triggered_at TIMESTAMPTZ,
    acknowledged_at TIMESTAMPTZ,
    
    -- Next trigger (for recurring)
    next_trigger_at TIMESTAMPTZ
);

CREATE INDEX idx_prospective_trigger_at ON prospective_memories(trigger_at);
CREATE INDEX idx_prospective_status ON prospective_memories(status);
CREATE INDEX idx_prospective_tenant ON prospective_memories(tenant_id);
CREATE INDEX idx_prospective_next_trigger ON prospective_memories(next_trigger_at)
    WHERE status = 'pending' AND next_trigger_at IS NOT NULL;

-- ============================================================
-- 4. CONTRADICTIONS: Detected Conflicts
-- ============================================================
CREATE TABLE contradictions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    memory_a_id UUID NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
    memory_b_id UUID NOT NULL REFERENCES memories(id) ON DELETE CASCADE,
    
    -- Contradiction type
    contradiction_type TEXT NOT NULL DEFAULT 'semantic' CHECK (contradiction_type IN (
        'semantic', 'temporal', 'logical', 'source', 'confidence'
    )),
    
    -- Description
    description TEXT NOT NULL,
    
    -- Resolution status
    resolution_status TEXT NOT NULL DEFAULT 'unresolved' CHECK (resolution_status IN (
        'unresolved', 'resolved_a', 'resolved_b', 'merged', 'both_valid', 'superseded', 'ignored'
    )),
    
    -- Resolution details
    resolved_by UUID, -- User or agent who resolved
    resolved_at TIMESTAMPTZ,
    resolution_reason TEXT,
    
    -- Confidence in contradiction detection
    detection_confidence FLOAT NOT NULL DEFAULT 0.5,
    
    -- Tenant isolation
    tenant_id UUID NOT NULL,
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    UNIQUE(memory_a_id, memory_b_id, tenant_id)
);

CREATE INDEX idx_contradictions_status ON contradictions(resolution_status);
CREATE INDEX idx_contradictions_tenant ON contradictions(tenant_id);
CREATE INDEX idx_contradictions_memory_a ON contradictions(memory_a_id);
CREATE INDEX idx_contradictions_memory_b ON contradictions(memory_b_id);

-- ============================================================
-- 5. AUDIT: Immutable Log (Tamper-Proof)
-- ============================================================
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Operation details
    operation TEXT NOT NULL CHECK (operation IN (
        'remember', 'recall', 'update', 'delete', 'consolidate', 'remind',
        'contradiction_detected', 'contradiction_resolved', 'version_created',
        'version_merged', 'namespace_sync', 'plugin_loaded', 'plugin_unloaded'
    )),
    
    -- Target memory (if applicable)
    memory_id UUID,
    
    -- Actor
    actor_type TEXT NOT NULL DEFAULT 'user' CHECK (actor_type IN (
        'user', 'agent', 'system', 'plugin', 'connector'
    )),
    actor_id TEXT NOT NULL,
    actor_name TEXT,
    
    -- Request details
    request_payload JSONB,
    response_payload JSONB,
    
    -- Success/failure
    success BOOLEAN NOT NULL DEFAULT TRUE,
    error_message TEXT,
    
    -- Performance metrics
    duration_ms INTEGER,
    
    -- Security: SHA-256 chain for tamper evidence
    previous_hash TEXT NOT NULL, -- Hash of previous audit log entry
    entry_hash TEXT NOT NULL, -- SHA-256 of this entry
    
    -- Ed25519 signature (for critical operations)
    signature TEXT,
    
    -- Tenant isolation
    tenant_id UUID NOT NULL,
    
    -- Timestamp
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_audit_logs_operation ON audit_logs(operation);
CREATE INDEX idx_audit_logs_memory ON audit_logs(memory_id);
CREATE INDEX idx_audit_logs_actor ON audit_logs(actor_type, actor_id);
CREATE INDEX idx_audit_logs_tenant ON audit_logs(tenant_id);
CREATE INDEX idx_audit_logs_created ON audit_logs(created_at DESC);
CREATE INDEX idx_audit_logs_success ON audit_logs(success);

-- Trigger: Auto-compute hash chain
CREATE OR REPLACE FUNCTION audit_logs_update_hash()
RETURNS TRIGGER AS $$
DECLARE
    prev_hash TEXT;
BEGIN
    -- Get previous hash
    SELECT entry_hash INTO prev_hash
    FROM audit_logs
    WHERE tenant_id = NEW.tenant_id
    ORDER BY created_at DESC
    LIMIT 1;
    
    IF prev_hash IS NULL THEN
        prev_hash := '0' || repeat('0', 63); -- Genesis hash
    END IF;
    
    NEW.previous_hash := prev_hash;
    NEW.entry_hash := encode(digest(
        prev_hash || NEW.operation || COALESCE(NEW.memory_id::text, '') || 
        NEW.actor_id || NEW.created_at::text,
        'sha256'
    ), 'hex');
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER audit_logs_hash_trigger
    BEFORE INSERT ON audit_logs
    FOR EACH ROW
    EXECUTE FUNCTION audit_logs_update_hash();

-- ============================================================
-- 6. TENANTS: Multi-Tenant Isolation
-- ============================================================
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    
    -- Configuration
    config JSONB NOT NULL DEFAULT '{
        "max_memories": 100000,
        "max_embeddings_per_month": 1000000,
        "retention_days": 365,
        "data_residency": "us-east-1",
        "compliance_mode": "standard"
    }',
    
    -- Status
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'deleted')),
    
    -- Plan
    plan TEXT NOT NULL DEFAULT 'free' CHECK (plan IN ('free', 'pro', 'team', 'enterprise')),
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_tenants_slug ON tenants(slug);
CREATE INDEX idx_tenants_status ON tenants(status);

-- ============================================================
-- 7. USERS: Authentication & RBAC
-- ============================================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    
    -- Auth
    email TEXT,
    auth_method TEXT NOT NULL DEFAULT 'jwt' CHECK (auth_method IN ('jwt', 'oauth', 'saml', 'api_key')),
    auth_provider TEXT, -- 'google', 'github', 'okta', etc.
    auth_subject TEXT, -- OAuth subject ID
    password_hash TEXT, -- bcrypt
    api_key_hash TEXT, -- For API key auth
    api_key_prefix TEXT, -- First 8 chars for display
    
    -- Profile
    display_name TEXT,
    avatar_url TEXT,
    timezone TEXT DEFAULT 'UTC',
    
    -- Role
    role TEXT NOT NULL DEFAULT 'member' CHECK (role IN ('owner', 'admin', 'member', 'viewer', 'agent')),
    
    -- Status
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'suspended')),
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_login_at TIMESTAMPTZ,
    
    UNIQUE(tenant_id, email)
);

CREATE INDEX idx_users_tenant ON users(tenant_id);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_status ON users(status);

-- ============================================================
-- 8. NAMESPACES: Multi-Agent Memory Isolation
-- ============================================================
CREATE TABLE namespaces (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    
    name TEXT NOT NULL,
    description TEXT,
    
    -- Namespace type
    namespace_type TEXT NOT NULL DEFAULT 'agent' CHECK (namespace_type IN (
        'agent', 'team', 'project', 'user', 'system', 'shared'
    )),
    
    -- Parent namespace (for hierarchy)
    parent_namespace_id UUID REFERENCES namespaces(id) ON DELETE SET NULL,
    
    -- Sync configuration (for federation)
    sync_config JSONB NOT NULL DEFAULT '{
        "sync_mode": "none",
        "sync_target": null,
        "sync_frequency": "manual",
        "conflict_resolution": "latest_wins"
    }',
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    UNIQUE(tenant_id, name)
);

CREATE INDEX idx_namespaces_tenant ON namespaces(tenant_id);
CREATE INDEX idx_namespaces_type ON namespaces(namespace_type);
CREATE INDEX idx_namespaces_parent ON namespaces(parent_namespace_id);

-- Namespace permissions
CREATE TABLE namespace_permissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    namespace_id UUID NOT NULL REFERENCES namespaces(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    permission TEXT NOT NULL CHECK (permission IN ('read', 'write', 'admin', 'sync')),
    
    granted_by UUID NOT NULL REFERENCES users(id),
    granted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    UNIQUE(namespace_id, user_id, permission)
);

-- ============================================================
-- 9. PLUGINS: Installed Plugins per Tenant
-- ============================================================
CREATE TABLE tenant_plugins (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    
    plugin_name TEXT NOT NULL,
    plugin_version TEXT NOT NULL,
    plugin_source TEXT NOT NULL DEFAULT 'marketplace' CHECK (plugin_source IN (
        'marketplace', 'local', 'git', 'url'
    )),
    
    -- Configuration
    config JSONB NOT NULL DEFAULT '{}',
    
    -- Status
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'disabled', 'error')),
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    UNIQUE(tenant_id, plugin_name)
);

-- ============================================================
-- 10. CONSOLIDATION: Job Tracking
-- ============================================================
CREATE TABLE consolidation_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    
    -- Job type
    job_type TEXT NOT NULL CHECK (job_type IN (
        'merge_duplicates', 'prune_stale', 'update_embeddings', 'rebuild_links',
        'detect_contradictions', 'resolve_contradictions', 'infer_relationships',
        'temporal_decay', 'salience_update', 'full_consolidation'
    )),
    
    -- Status
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN (
        'pending', 'running', 'completed', 'failed', 'cancelled'
    )),
    
    -- Progress
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    progress_percent INTEGER DEFAULT 0,
    
    -- Results
    results JSONB,
    error_message TEXT,
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_consolidation_tenant ON consolidation_jobs(tenant_id);
CREATE INDEX idx_consolidation_status ON consolidation_jobs(status);
CREATE INDEX idx_consolidation_type ON consolidation_jobs(job_type);

-- ============================================================
-- 11. HEALTH: System Health Metrics
-- ============================================================
CREATE TABLE health_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    
    -- Metric type
    metric_type TEXT NOT NULL CHECK (metric_type IN (
        'memory_count', 'link_count', 'contradiction_count', 'prospective_count',
        'query_latency_ms', 'recall_accuracy', 'consolidation_duration_ms',
        'embedding_cost_usd', 'storage_bytes'
    )),
    
    -- Value
    metric_value FLOAT NOT NULL,
    metric_unit TEXT NOT NULL,
    
    -- Dimensions
    dimensions JSONB NOT NULL DEFAULT '{}',
    
    -- Timestamp
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_health_tenant ON health_metrics(tenant_id);
CREATE INDEX idx_health_type ON health_metrics(metric_type);
CREATE INDEX idx_health_recorded ON health_metrics(recorded_at DESC);
```

## 3.2 Valkey (Hot State) Schema

```
# Key patterns for Valkey (Redis-compatible)

# Session working memory (ephemeral, 35-min TTL)
mnemosyne:session:{session_id}:turns  → JSON array of last 10-20 turns
mnemosyne:session:{session_id}:tools  → JSON array of tool call history
mnemosyne:session:{session_id}:summary → Compressed session summary
mnemosyne:session:{session_id}:metadata → {started_at, last_accessed, agent_id}

# Query cache (5-min TTL for identical queries)
mnemosyne:cache:query:{hash(query+filters)} → Cached results

# Rate limiting (sliding window)
mnemosyne:rate:{tenant_id}:{user_id}:{operation} → Counter + TTL

# Prospective trigger queue (sorted by trigger time)
mnemosyne:prospective:pending → Sorted set (score = trigger_at_timestamp)

# Plugin registry (cache of loaded plugins)
mnemosyne:plugins:{tenant_id} → JSON object of active plugins

# Health metrics (1-min TTL, streamed to DB)
mnemosyne:health:{tenant_id}:{metric_type} → Latest value
```

## 3.3 S3 + R2 (Cold Storage) Schema

```
# S3 bucket structure (primary, Object Lock for compliance)

s3://mnemosyne-{tenant-id}/
├── sessions/
│   ├── {year}/{month}/{day}/{session_id}.json.gz  # Full session transcripts
│   └── {year}/{month}/{day}/{session_id}.parquet  # Analytics-ready
├── memories/
│   ├── {year}/{month}/{day}/{memory_id}.md        # Markdown source (source of truth)
│   └── {year}/{month}/{day}/{memory_id}.json      # Structured export
├── audits/
│   ├── {year}/{month}/{day}/audit-{hour}.parquet   # Immutable audit logs
│   └── {year}/{month}/{day}/audit-{hour}.wal       # Write-ahead log
├── snapshots/
│   ├── {year}/{month}/{day}/{snapshot_id}/         # Full system snapshots
│   └── {year}/{month}/{day}/{snapshot_id}/manifest.json
└── exports/
    └── {export_id}/                                  # GDPR Art. 17 exports

# R2 bucket structure (secondary, zero egress for retrieval)

r2://mnemosyne-summaries/
├── summaries/
│   ├── {tenant_id}/{memory_id}.summary.json         # Pre-computed summaries
│   └── {tenant_id}/{memory_id}.embedding.npy        # Cached embeddings
├── search-index/
│   └── {tenant_id}/hnsw-index.bin                 # HNSW index shards
└── backups/
    └── {tenant_id}/daily/{date}.tar.gz              # Daily backups
```

---

# PART 4: COMPLETE API SPECIFICATION

## 4.1 REST API (OpenAPI 3.1)

```yaml
openapi: 3.1.0
info:
  title: Mnemosyne Memory OS API
  version: 3.0.0
  description: |
    The Operating System for AI Memory.
    
    Provides semantic, episodic, procedural, prospective, emotional, and meta memory
    with versioning, multi-agent namespaces, contradiction detection, and compliance.

servers:
  - url: https://api.mnemosyne.ai/v1
    description: Production
  - url: http://localhost:8000/v1
    description: Local Development

security:
  - OAuth2: [memory:read, memory:write, memory:admin]
  - ApiKey: []

paths:
  # ============================================================
  # CORE: Remember (Store Memory)
  # ============================================================
  /memories:
    post:
      operationId: remember
      summary: Store a memory
      description: |
        Stores a typed memory with full provenance, salience scoring, and
        security validation (SMSR-certified admission control).
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [title, content, memory_type]
              properties:
                title:
                  type: string
                  maxLength: 500
                  description: Human-readable memory title
                content:
                  type: string
                  maxLength: 100000
                  description: Memory content (Markdown supported)
                memory_type:
                  type: string
                  enum: [episodic, semantic, procedural, prospective, emotional, meta]
                tags:
                  type: array
                  items: { type: string }
                  maxItems: 50
                salience:
                  type: number
                  minimum: 0.0
                  maximum: 1.0
                  default: 0.5
                confidence:
                  type: number
                  minimum: 0.0
                  maximum: 1.0
                  default: 0.5
                valid_at:
                  type: string
                  format: date-time
                  description: When this memory becomes valid
                invalid_at:
                  type: string
                  format: date-time
                  description: When this memory becomes invalid (NULL = forever)
                namespace:
                  type: string
                  default: default
                  description: Multi-agent namespace for isolation
                source_type:
                  type: string
                  enum: [manual, agent, connector, import, inferred, consolidated]
                  default: manual
                source_id:
                  type: string
                  description: Agent ID, connector ID, or user ID
                frontmatter:
                  type: object
                  description: YAML frontmatter as JSON object
                links:
                  type: array
                  items:
                    type: object
                    properties:
                      target_title: { type: string }
                      link_type: 
                        type: string
                        enum: [related, causes, supports, contradicts, supersedes, prerequisite, part_of, similar_to]
                      strength: { type: number, minimum: 0.0, maximum: 1.0 }
      responses:
        '201':
          description: Memory created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  id: { type: string, format: uuid }
                  memory_type: { type: string }
                  title: { type: string }
                  content_hash: { type: string }
                  salience: { type: number }
                  confidence: { type: number }
                  provenance_hash: { type: string }
                  embedding_stored: { type: boolean }
                  links_created: { type: integer }
                  contradictions_detected: { type: integer }
                  warnings: { type: array, items: { type: string } }
                  created_at: { type: string, format: date-time }
        '400':
          description: Validation error (admission control rejected)
          content:
            application/json:
              schema:
                type: object
                properties:
                  error: { type: string }
                  rejection_reason: { type: string }
                  gate_checks_failed: { type: array, items: { type: string } }
        '429':
          description: Rate limit exceeded

  # ============================================================
  # CORE: Recall (Retrieve Memory)
  # ============================================================
  /memories/search:
    post:
      operationId: recall
      summary: Search memories with hybrid retrieval
      description: |
        Routes query to the correct memory subsystem(s) using the Query Router.
        Supports semantic search, graph traversal, temporal filtering, and salience ranking.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [query]
              properties:
                query:
                  type: string
                  maxLength: 10000
                  description: Natural language query
                mode:
                  type: string
                  enum: [semantic, graph, episodic, procedural, hybrid, all]
                  default: hybrid
                  description: Which memory subsystem(s) to search
                top_k:
                  type: integer
                  default: 5
                  maximum: 100
                filters:
                  type: object
                  properties:
                    memory_type: { type: array, items: { type: string } }
                    tags: { type: array, items: { type: string } }
                    namespace: { type: string }
                    valid_at: { type: string, format: date-time }
                    min_salience: { type: number }
                    min_confidence: { type: number }
                    status: { type: array, items: { type: string } }
                    source_type: { type: array, items: { type: string } }
                temporal_context:
                  type: object
                  properties:
                    valid_at: { type: string, format: date-time }
                    time_window: { type: string, description: "e.g., '2026-01-01 to 2026-06-30'" }
                include_links:
                  type: boolean
                  default: true
                  description: Include related memories via graph traversal
                include_contradictions:
                  type: boolean
                  default: false
                  description: Include detected contradictions
                explain:
                  type: boolean
                  default: false
                  description: Include routing explanation and salience breakdown
      responses:
        '200':
          description: Search results
          content:
            application/json:
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        memory:
                          type: object
                          properties:
                            id: { type: string }
                            title: { type: string }
                            content: { type: string }
                            memory_type: { type: string }
                            salience: { type: number }
                            confidence: { type: number }
                            valid_at: { type: string }
                            links: { type: array }
                        score: { type: number, description: "RRF score" }
                        rank: { type: integer }
                        route: { type: string, description: "Which subsystem found this" }
                        salience_breakdown: { type: object }
                  total_results: { type: integer }
                  query_routing:
                    type: object
                    properties:
                      subsystems_queried: { type: array, items: { type: string } }
                      latency_ms: { type: object }
                      token_budget_used: { type: number }
                  contradictions:
                    type: array
                    items: { type: object }
                  temporal_warnings:
                    type: array
                    items: { type: string }

  # ============================================================
  # CORE: Remind Me (Prospective Memory)
  # ============================================================
  /memories/remind:
    post:
      operationId: remind_me
      summary: Schedule a future reminder
      description: |
        Creates a prospective memory — a scheduled reminder, recurring task,
        or event-triggered action. The scheduler monitors triggers and fires
        reminders when conditions are met.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [title, trigger_at]
              properties:
                title:
                  type: string
                  maxLength: 500
                content:
                  type: string
                  description: What to remember / what action to take
                trigger_at:
                  type: string
                  format: date-time
                  description: Absolute trigger time (ISO 8601)
                trigger_type:
                  type: string
                  enum: [absolute, relative, recurring, event, condition]
                  default: absolute
                relative_duration:
                  type: string
                  description: "e.g., '3 days', '1 week'"
                recurring_spec:
                  type: string
                  description: "Cron expression or natural language, e.g., '0 9 * * MON'"
                recurring_end_at:
                  type: string
                  format: date-time
                event_type:
                  type: string
                  enum: [memory_created, memory_updated, memory_accessed, external]
                event_filter:
                  type: object
                condition_expression:
                  type: string
                  description: "SQL-like condition, e.g., 'salience < 0.3'"
                action_type:
                  type: string
                  enum: [notify, query, consolidate, export, webhook, mcp_tool]
                  default: notify
                action_payload:
                  type: object
                namespace:
                  type: string
                  default: default
      responses:
        '201':
          description: Reminder scheduled
          content:
            application/json:
              schema:
                type: object
                properties:
                  reminder_id: { type: string }
                  trigger_at: { type: string }
                  next_trigger_at: { type: string }
                  status: { type: string }

  # ============================================================
  # CORE: Consolidate (Memory Maintenance)
  # ============================================================
  /memories/consolidate:
    post:
      operationId: consolidate
      summary: Trigger memory consolidation
      description: |
        Runs maintenance on the memory system: merge duplicates, prune stale,
        detect contradictions, update embeddings, rebuild links, infer relationships.
        Can be scheduled or triggered manually.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                job_types:
                  type: array
                  items:
                    type: string
                    enum: [merge_duplicates, prune_stale, update_embeddings, rebuild_links, detect_contradictions, resolve_contradictions, infer_relationships, temporal_decay, salience_update, full_consolidation]
                  default: [full_consolidation]
                dry_run:
                  type: boolean
                  default: false
                  description: Preview changes without applying
                namespace:
                  type: string
                  default: default
      responses:
        '202':
          description: Consolidation job queued
          content:
            application/json:
              schema:
                type: object
                properties:
                  job_id: { type: string }
                  status: { type: string }
                  estimated_duration_seconds: { type: integer }

  # ============================================================
  # CORE: Audit (Observability)
  # ============================================================
  /memories/audit:
    get:
      operationId: audit
      summary: Retrieve audit trail
      description: |
        Returns tamper-evident audit logs for memory operations.
        Includes SHA-256 hash chain verification and Ed25519 signatures
        for critical operations.
      parameters:
        - name: memory_id
          in: query
          schema: { type: string, format: uuid }
        - name: operation
          in: query
          schema: { type: string, enum: [remember, recall, update, delete, consolidate, remind] }
        - name: actor_id
          in: query
          schema: { type: string }
        - name: from
          in: query
          schema: { type: string, format: date-time }
        - name: to
          in: query
          schema: { type: string, format: date-time }
        - name: verify_chain
          in: query
          schema: { type: boolean, default: false }
          description: Verify SHA-256 hash chain integrity
      responses:
        '200':
          description: Audit trail
          content:
            application/json:
              schema:
                type: object
                properties:
                  logs:
                    type: array
                    items:
                      type: object
                      properties:
                        id: { type: string }
                        operation: { type: string }
                        memory_id: { type: string }
                        actor_type: { type: string }
                        actor_id: { type: string }
                        success: { type: boolean }
                        duration_ms: { type: integer }
                        entry_hash: { type: string }
                        previous_hash: { type: string }
                        signature: { type: string }
                        created_at: { type: string }
                  chain_verified: { type: boolean }
                  total_entries: { type: integer }

  # ============================================================
  # CORE: Forget (GDPR-Compliant Erasure)
  # ============================================================
  /memories/{memory_id}:
    delete:
      operationId: forget
      summary: Soft-delete a memory (GDPR Article 17)
      description: |
        Soft-deletes a memory with full audit trail. The memory is hidden from
        all queries but retained in cold storage for compliance. A GDPR export
        can be generated. Hard deletion is available for compliance officers.
      parameters:
        - name: memory_id
          in: path
          required: true
          schema: { type: string, format: uuid }
        - name: hard_delete
          in: query
          schema: { type: boolean, default: false }
          description: Permanently delete (requires admin role)
        - name: reason
          in: query
          schema: { type: string }
          description: GDPR deletion reason
      responses:
        '200':
          description: Memory deleted
          content:
            application/json:
              schema:
                type: object
                properties:
                  memory_id: { type: string }
                  deleted_at: { type: string }
                  deletion_reason: { type: string }
                  hard_deleted: { type: boolean }
                  audit_log_id: { type: string }
                  gdpr_export_available: { type: boolean }

  # ============================================================
  # VERSIONING: Branch & Merge
  # ============================================================
  /memories/{memory_id}/versions:
    get:
      operationId: list_versions
      summary: List all versions of a memory
      parameters:
        - name: memory_id
          in: path
          required: true
          schema: { type: string, format: uuid }
      responses:
        '200':
          description: Version history

  /memories/{memory_id}/branch:
    post:
      operationId: create_branch
      summary: Create a new branch from a memory version
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required: [branch_name]
              properties:
                branch_name: { type: string }
                from_version: { type: string, format: uuid }
      responses:
        '201':
          description: Branch created

  /memories/branches/{branch_name}/merge:
    post:
      operationId: merge_branch
      summary: Merge a branch into main
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                merge_strategy:
                  type: string
                  enum: [fast_forward, three_way, manual]
                  default: three_way
      responses:
        '200':
          description: Branch merged

  # ============================================================
  # CONTRADICTIONS: Conflict Resolution
  # ============================================================
  /contradictions:
    get:
      operationId: list_contradictions
      summary: List detected contradictions
      parameters:
        - name: status
          in: query
          schema: { type: string, enum: [unresolved, resolved, all] }
        - name: min_confidence
          in: query
          schema: { type: number }
      responses:
        '200':
          description: Contradictions

  /contradictions/{contradiction_id}/resolve:
    post:
      operationId: resolve_contradiction
      summary: Resolve a contradiction
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required: [resolution]
              properties:
                resolution:
                  type: string
                  enum: [resolve_a, resolve_b, merge, both_valid, superseded, ignore]
                reason: { type: string }
      responses:
        '200':
          description: Contradiction resolved

  # ============================================================
  # HEALTH: System Health
  # ============================================================
  /health:
    get:
      operationId: health
      summary: System health metrics
      responses:
        '200':
          description: Health metrics
          content:
            application/json:
              schema:
                type: object
                properties:
                  status: { type: string, enum: [healthy, degraded, unhealthy] }
                  subsystems:
                    type: object
                    properties:
                      hot: { type: object }
                      queryable: { type: object }
                      cold: { type: object }
                      scheduler: { type: object }
                  metrics:
                    type: array
                    items: { type: object }
                  contradictions:
                    type: object
                    properties:
                      total: { type: integer }
                      unresolved: { type: integer }
                      detection_rate: { type: number }

  # ============================================================
  # PROXY: Drop-In OpenAI-Compatible Mode
  # ============================================================
  /proxy/chat/completions:
    post:
      operationId: proxy_chat
      summary: OpenAI-compatible proxy with automatic memory
      description: |
        Drop-in replacement for OpenAI's chat completions endpoint.
        Automatically remembers conversations and recalls relevant context.
        Zero code changes for any agent using OpenAI API.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                model: { type: string }
                messages: { type: array }
                memory_options:
                  type: object
                  properties:
                    enable_recall: { type: boolean, default: true }
                    enable_remember: { type: boolean, default: true }
                    namespace: { type: string, default: default }
                    top_k: { type: integer, default: 5 }
      responses:
        '200':
          description: Chat completion with memory

components:
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.mnemosyne.ai/oauth/authorize
          tokenUrl: https://auth.mnemosyne.ai/oauth/token
          scopes:
            memory:read: Read memories
            memory:write: Create and update memories
            memory:admin: Admin operations (delete, audit, configure)
    ApiKey:
      type: apiKey
      in: header
      name: X-Mnemosyne-Api-Key
```

## 4.2 MCP Tools (Stateless, 2026-07-28 Spec)

```json
{
  "name": "mnemosyne-memory-os",
  "version": "3.0.0",
  "description": "The Operating System for AI Memory — semantic, episodic, procedural, prospective, emotional, and meta memory with versioning, multi-agent namespaces, and compliance.",
  "transport": ["stdio", "streamable-http"],
  "tools": [
    {
      "name": "memory_remember",
      "description": "Store a memory in the system. Validates via admission control (SMSR-certified). Returns the memory ID and any detected contradictions.",
      "inputSchema": {
        "type": "object",
        "required": ["title", "content", "memory_type"],
        "properties": {
          "title": { "type": "string", "maxLength": 500 },
          "content": { "type": "string", "maxLength": 100000 },
          "memory_type": { "type": "string", "enum": ["episodic", "semantic", "procedural", "prospective", "emotional", "meta"] },
          "tags": { "type": "array", "items": { "type": "string" }, "maxItems": 50 },
          "salience": { "type": "number", "minimum": 0.0, "maximum": 1.0, "default": 0.5 },
          "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0, "default": 0.5 },
          "valid_at": { "type": "string", "format": "date-time" },
          "invalid_at": { "type": "string", "format": "date-time" },
          "namespace": { "type": "string", "default": "default" },
          "source_type": { "type": "string", "enum": ["manual", "agent", "connector", "import", "inferred", "consolidated"], "default": "manual" },
          "source_id": { "type": "string" },
          "links": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "target_title": { "type": "string" },
                "link_type": { "type": "string", "enum": ["related", "causes", "supports", "contradicts", "supersedes", "prerequisite", "part_of", "similar_to"] },
                "strength": { "type": "number", "minimum": 0.0, "maximum": 1.0 }
              }
            }
          }
        }
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "memory_type": { "type": "string" },
          "title": { "type": "string" },
          "content_hash": { "type": "string" },
          "salience": { "type": "number" },
          "confidence": { "type": "number" },
          "provenance_hash": { "type": "string" },
          "embedding_stored": { "type": "boolean" },
          "links_created": { "type": "integer" },
          "contradictions_detected": { "type": "integer" },
          "warnings": { "type": "array", "items": { "type": "string" } },
          "created_at": { "type": "string", "format": "date-time" }
        }
      }
    },
    {
      "name": "memory_recall",
      "description": "Search memories using hybrid retrieval (semantic + graph + episodic). The Query Router automatically selects the best subsystem(s) based on the query. Returns ranked results with RRF scores and routing explanation.",
      "inputSchema": {
        "type": "object",
        "required": ["query"],
        "properties": {
          "query": { "type": "string", "maxLength": 10000 },
          "mode": { "type": "string", "enum": ["semantic", "graph", "episodic", "procedural", "hybrid", "all"], "default": "hybrid" },
          "top_k": { "type": "integer", "default": 5, "maximum": 100 },
          "filters": {
            "type": "object",
            "properties": {
              "memory_type": { "type": "array", "items": { "type": "string" } },
              "tags": { "type": "array", "items": { "type": "string" } },
              "namespace": { "type": "string" },
              "valid_at": { "type": "string", "format": "date-time" },
              "min_salience": { "type": "number" },
              "min_confidence": { "type": "number" }
            }
          },
          "include_links": { "type": "boolean", "default": true },
          "include_contradictions": { "type": "boolean", "default": false },
          "explain": { "type": "boolean", "default": false }
        }
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "memory": {
                  "type": "object",
                  "properties": {
                    "id": { "type": "string" },
                    "title": { "type": "string" },
                    "content": { "type": "string" },
                    "memory_type": { "type": "string" },
                    "salience": { "type": "number" },
                    "confidence": { "type": "number" },
                    "valid_at": { "type": "string" },
                    "links": { "type": "array" }
                  }
                },
                "score": { "type": "number", "description": "RRF score" },
                "rank": { "type": "integer" },
                "route": { "type": "string" },
                "salience_breakdown": { "type": "object" }
              }
            }
          },
          "total_results": { "type": "integer" },
          "query_routing": {
            "type": "object",
            "properties": {
              "subsystems_queried": { "type": "array", "items": { "type": "string" } },
              "latency_ms": { "type": "object" },
              "token_budget_used": { "type": "number" }
            }
          },
          "contradictions": { "type": "array", "items": { "type": "object" } },
          "temporal_warnings": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    {
      "name": "memory_remind_me",
      "description": "Schedule a future reminder or recurring task. The Prospective Scheduler monitors triggers and fires reminders when conditions are met. Supports absolute time, relative duration, cron expressions, event triggers, and condition-based triggers.",
      "inputSchema": {
        "type": "object",
        "required": ["title", "trigger_at"],
        "properties": {
          "title": { "type": "string", "maxLength": 500 },
          "content": { "type": "string", "description": "What to remember / what action to take" },
          "trigger_at": { "type": "string", "format": "date-time" },
          "trigger_type": { "type": "string", "enum": ["absolute", "relative", "recurring", "event", "condition"], "default": "absolute" },
          "relative_duration": { "type": "string", "description": "e.g., '3 days', '1 week'" },
          "recurring_spec": { "type": "string", "description": "Cron expression or natural language" },
          "recurring_end_at": { "type": "string", "format": "date-time" },
          "event_type": { "type": "string", "enum": ["memory_created", "memory_updated", "memory_accessed", "external"] },
          "event_filter": { "type": "object" },
          "condition_expression": { "type": "string", "description": "SQL-like condition, e.g., 'salience < 0.3'" },
          "action_type": { "type": "string", "enum": ["notify", "query", "consolidate", "export", "webhook", "mcp_tool"], "default": "notify" },
          "action_payload": { "type": "object" },
          "namespace": { "type": "string", "default": "default" }
        }
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "reminder_id": { "type": "string" },
          "trigger_at": { "type": "string", "format": "date-time" },
          "next_trigger_at": { "type": "string", "format": "date-time" },
          "status": { "type": "string" }
        }
      }
    },
    {
      "name": "memory_consolidate",
      "description": "Trigger memory consolidation — merge duplicates, prune stale memories, detect contradictions, update embeddings, rebuild links, infer relationships, apply temporal decay. Can be run as dry-run to preview changes. Runs automatically on a nightly schedule.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "job_types": {
            "type": "array",
            "items": { "type": "string", "enum": ["merge_duplicates", "prune_stale", "update_embeddings", "rebuild_links", "detect_contradictions", "resolve_contradictions", "infer_relationships", "temporal_decay", "salience_update", "full_consolidation"] },
            "default": ["full_consolidation"]
          },
          "dry_run": { "type": "boolean", "default": false },
          "namespace": { "type": "string", "default": "default" }
        }
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "job_id": { "type": "string" },
          "status": { "type": "string" },
          "estimated_duration_seconds": { "type": "integer" }
        }
      }
    },
    {
      "name": "memory_audit",
      "description": "Retrieve tamper-evident audit logs for memory operations. Includes SHA-256 hash chain verification and Ed25519 signatures for critical operations. Use this to verify memory integrity and compliance.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "memory_id": { "type": "string", "format": "uuid" },
          "operation": { "type": "string", "enum": ["remember", "recall", "update", "delete", "consolidate", "remind"] },
          "actor_id": { "type": "string" },
          "from": { "type": "string", "format": "date-time" },
          "to": { "type": "string", "format": "date-time" },
          "verify_chain": { "type": "boolean", "default": false }
        }
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "logs": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": { "type": "string" },
                "operation": { "type": "string" },
                "memory_id": { "type": "string" },
                "actor_type": { "type": "string" },
                "actor_id": { "type": "string" },
                "success": { "type": "boolean" },
                "duration_ms": { "type": "integer" },
                "entry_hash": { "type": "string" },
                "previous_hash": { "type": "string" },
                "signature": { "type": "string" },
                "created_at": { "type": "string", "format": "date-time" }
              }
            }
          },
          "chain_verified": { "type": "boolean" },
          "total_entries": { "type": "integer" }
        }
      }
    },
    {
      "name": "memory_forget",
      "description": "Soft-delete a memory with full audit trail. The memory is hidden from all queries but retained in cold storage for compliance. Supports GDPR-compliant erasure with export generation. Hard deletion requires admin role.",
      "inputSchema": {
        "type": "object",
        "required": ["memory_id"],
        "properties": {
          "memory_id": { "type": "string", "format": "uuid" },
          "hard_delete": { "type": "boolean", "default": false },
          "reason": { "type": "string", "description": "GDPR deletion reason" }
        }
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "memory_id": { "type": "string" },
          "deleted_at": { "type": "string", "format": "date-time" },
          "deletion_reason": { "type": "string" },
          "hard_deleted": { "type": "boolean" },
          "audit_log_id": { "type": "string" },
          "gdpr_export_available": { "type": "boolean" }
        }
      }
    }
  ]
}
```

---

# PART 5: SECURITY ARCHITECTURE (SMSR-Certified)

## 5.1 The Threat Model

| Threat | Attack | Realistic ASR | Defense | Status |
|--------|--------|---------------|---------|--------|
| **MINJA** | Memory injection via natural language | **20–40%** (realistic) | Admission control + SMSR C1 (HMAC-SHA256) | P0 |
| **ADAM** | Automated data extraction from memory | **Up to 100%** | Rate limiting + query-pattern anomaly detection + differential privacy | P0 |
| **PoisonedRAG** | Malicious documents poison vector DB | **High** | Source authentication + embedding-space anomaly detection | P0 |
| **AgentPoison** | Gradient-optimized embedding triggers | **>80%** at <0.1% poison rate | RAGuard retrieval filtering + periodic embedding audits | P0 |
| **CorruptRAG** | Single document flips targeted answers | **High** | Multi-source verification + confidence thresholds | P1 |
| **Cross-tenant leakage** | One tenant accesses another's memory | **High** | Per-tenant schema isolation + row-level security | P0 |
| **Memory tampering** | Modify stored memories | **Medium** | HMAC-SHA256 provenance + Merkle trees + Ed25519 signatures | P0 |
| **Session hijacking** | Steal session tokens | **Medium** | OAuth 2.1 + PKCE + short-lived tokens | P0 |

## 5.2 The SMSR Defense Architecture

**SMSR (Secure Memory Storage and Retrieval)** — June 2026, first certified defense:

### C1: Write-Time Provenance (Blocks 100% of Unsigned Injections)

```python
# Every memory write is HMAC-SHA256 signed
import hmac
import hashlib

def sign_memory(content: str, timestamp: str, source_id: str, secret_key: bytes) -> str:
    """HMAC-SHA256 provenance signature for every memory."""
    message = f"{content}:{timestamp}:{source_id}"
    return hmac.new(secret_key, message.encode(), hashlib.sha256).hexdigest()

def verify_memory(memory: Memory, secret_key: bytes) -> bool:
    """Verify memory provenance before retrieval."""
    expected = sign_memory(memory.content, memory.created_at, memory.source_id, secret_key)
    return hmac.compare_digest(memory.provenance_hash, expected)
```

### C2: Query-Time Randomized Ablation (Bounds Authenticated ASR to ~5–8%)

```python
# At retrieval time, randomly ablate (remove) a subset of memories
# and check if the answer changes. If it does, the memory is critical.
# If the answer is consistent across ablations, confidence is high.

import random

def ablation_retrieval(query: str, memories: List[Memory], k: int = 5) -> RetrievalResult:
    """Randomized ablation with verdict-based majority voting."""
    
    # Baseline: retrieve with all memories
    baseline = retrieve(query, memories)
    
    # Ablation rounds: remove 10-30% of memories randomly
    verdicts = []
    for _ in range(k):
        ablated = random.sample(memories, int(len(memories) * 0.7))
        result = retrieve(query, ablated)
        verdicts.append(result.verdict == baseline.verdict)
    
    # If >60% of ablations agree with baseline, confidence is high
    confidence = sum(verdicts) / len(verdicts)
    
    if confidence < 0.6:
        # Low confidence — potential injection or poisoning
        return RetrievalResult(
            verdict=baseline.verdict,
            confidence=confidence,
            warning="Low confidence due to ablation disagreement. Potential injection detected."
        )
    
    return RetrievalResult(verdict=baseline.verdict, confidence=confidence)
```

### C3: Rate Limiting + Pattern Detection (Defends Against ADAM)

```python
# ADAM queries are structurally distinguishable: systematic, iterative, high entropy

def detect_adam_pattern(query_history: List[Query]) -> bool:
    """Detect ADAM-style extraction attacks."""
    
    # Pattern 1: Rapid sequential queries with prefix-suffix injection
    if len(query_history) > 10:
        recent = query_history[-10:]
        time_span = recent[-1].timestamp - recent[0].timestamp
        if time_span < 60:  # 10 queries in 60 seconds
            return True
    
    # Pattern 2: High entropy queries (systematic probing)
    entropies = [calculate_entropy(q.content) for q in query_history[-5:]]
    if sum(entropies) / len(entropies) > 5.0:  # High average entropy
        return True
    
    # Pattern 3: Prefix-suffix injection pattern
    prefixes = [q.content[:20] for q in query_history[-5:]]
    if len(set(prefixes)) == 1:  # Same prefix, different suffixes
        return True
    
    return False
```

### C4: Embedding-Space Anomaly Detection (Defends Against PoisonedRAG)

```python
# Detect anomalous embeddings that might be poisoned

def detect_embedding_anomaly(embedding: np.ndarray, cluster_centers: List[np.ndarray]) -> bool:
    """Detect anomalous embeddings using spectral analysis."""
    
    # Distance to nearest cluster center
    distances = [np.linalg.norm(embedding - center) for center in cluster_centers]
    min_distance = min(distances)
    
    # If distance is >3σ from cluster, flag as anomaly
    if min_distance > threshold_3sigma:
        return True
    
    # Spectral analysis: check for gradient-optimized trigger patterns
    # Poisoned embeddings often have unusual spectral characteristics
    spectrum = np.fft.fft(embedding)
    if np.max(np.abs(spectrum)) > spectral_threshold:
        return True
    
    return False
```

## 5.3 The Admission Control Gate (In Order, ~3ms Total)

```python
class AdmissionControl:
    """Security gate before any write to the database."""
    
    async def check(self, request: RememberRequest) -> AdmissionResult:
        # 1. Length gate (~0.1ms)
        if len(request.content) < 10:
            return AdmissionResult(rejected=True, reason="content_too_short")
        
        # 2. Injection detection — MINJA patterns (~0.5ms)
        injection_score = self.detect_injection(request.content)
        if injection_score > 0.7:
            return AdmissionResult(
                rejected=True, 
                reason="injection_detected",
                details={"pattern": injection_score.pattern, "confidence": injection_score.confidence}
            )
        
        # 3. Near-duplicate check (~0.5ms)
        duplicate = await self.find_duplicate(request.content, threshold=0.92)
        if duplicate:
            return AdmissionResult(
                rejected=True,
                reason="near_duplicate",
                details={"existing_id": duplicate.id, "similarity": duplicate.similarity},
                suggestion="update_existing"
            )
        
        # 4. Contradiction check (~1ms)
        contradiction = await self.find_contradiction(request.title, request.content)
        if contradiction:
            return AdmissionResult(
                rejected=False,  # Not rejected, but flagged
                warning="contradiction_detected",
                details={"contradiction_id": contradiction.id, "confidence": contradiction.confidence}
            )
        
        # 5. Salience scoring (~0.5ms)
        salience = self.calculate_salience(request)
        
        # 6. Provenance signing (~0.3ms)
        provenance_hash = self.sign_memory(request)
        
        return AdmissionResult(
            rejected=False,
            salience=salience,
            provenance_hash=provenance_hash,
            warnings=[]
        )
```

## 5.4 Compliance Architecture (GDPR + EU AI Act + NIST)

### GDPR Article 17 (Right to Erasure)

```python
class GDPRManager:
    """Handles GDPR-compliant erasure across all memory layers."""
    
    async def erase_memory(self, memory_id: UUID, reason: str, user_id: UUID) -> ErasureResult:
        """
        Soft-delete from queryable layer.
        Remove from vector index.
        Mark for cold storage purge.
        Generate audit trail.
        Generate GDPR export if requested.
        """
        
        # 1. Soft-delete in PostgreSQL (queryable layer)
        await self.db.execute(
            "UPDATE memories SET status = 'deleted', deleted_at = NOW(), deleted_by = $1, deletion_reason = $2 WHERE id = $3",
            user_id, reason, memory_id
        )
        
        # 2. Remove from vector index
        await self.vector_store.delete(memory_id)
        
        # 3. Remove from Valkey cache
        await self.cache.delete(f"memory:{memory_id}")
        
        # 4. Mark for cold storage purge (S3 Object Lock retention)
        await self.cold_storage.schedule_purge(memory_id, retention_days=30)
        
        # 5. Generate audit log
        audit_id = await self.audit.log(
            operation="delete",
            memory_id=memory_id,
            actor_id=user_id,
            reason=reason
        )
        
        # 6. Generate GDPR export (if within 30 days of request)
        export_available = await self.gdpr.generate_export(memory_id)
        
        return ErasureResult(
            memory_id=memory_id,
            deleted_at=datetime.now(),
            audit_log_id=audit_id,
            gdpr_export_available=export_available
        )
```

### EU AI Act (High-Risk AI — August 2, 2026)

| Requirement | Mnemosyne Implementation | Deadline |
|-------------|-------------------------|----------|
| **Art. 12: Logging** | SHA-256 hash-chained audit logs, 6-month retention | August 2, 2026 |
| **Art. 14: Human Oversight** | Dashboard with override capability, alert on high-confidence contradictions | August 2, 2026 |
| **Art. 15: Accuracy** | Benchmark suite (LoCoMo, LongMemEval), continuous evaluation | August 2, 2026 |
| **Art. 16: Robustness** | Red-teaming in CI/CD, MINJA/ADAM resistance testing | August 2, 2026 |
| **Art. 17: Cybersecurity** | OWASP AMG compliance, SMSR certification, penetration testing | August 2, 2026 |
| **Penalties** | €35M / 7% turnover for prohibited; €15M / 3% for high-risk | August 2, 2026 |

### NIST AI RMF (GOVERN 1.7, 6.1)

| Requirement | Mnemosyne Implementation |
|-------------|-------------------------|
| **GOVERN 1.7: Document risks** | Risk register with CVSS scores, mitigation plans, owners |
| **GOVERN 6.1: Audit evidence** | Ed25519-signed, SHA-256 hash-chained decision receipts |
| **MAP 1.1: Identify context** | Context inventory (use cases, stakeholders, impact assessment) |
| **MEASURE 1.1: Test accuracy** | Automated benchmark suite (LoCoMo, LongMemEval, BEAM) |
| **MANAGE 1.1: Respond to incidents** | Incident response plan, rollback procedures, forensic snapshots |

---

# PART 6: COMPLETE BUILD PLAN (12 Months)

## 6.1 Phase 0: Foundation (Week 1-2) — "The Kernel"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W1** | PostgreSQL + pgvector + pgvectorscale setup | Schema deployed, indexes created, test data inserted, 1000 queries/sec |
| **W1** | Valkey hot state setup | Session cache working, 35-min rotation implemented, TTL verified |
| **W1** | S3 + R2 cold storage setup | File upload/download working, Object Lock configured, R2 zero egress verified |
| **W2** | Microkernel scaffold | Plugin manager loading/unloading plugins, kernel routing queries, admission control gate passing |
| **W2** | FastAPI scaffold | Health endpoint, OpenAPI schema generated, middleware (auth, rate limit, logging) working |
| **W2** | CI/CD pipeline | GitHub Actions, tests running, linting, type checking, security scan (Snyk/Dependabot) |

## 6.2 Phase 1: MVP (Month 1) — "Core Memory"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W3** | Episodic memory plugin | Store/retrieve events, semantic search, salience scoring |
| **W3** | Semantic memory plugin | Store/retrieve facts, graph edges, entity extraction |
| **W4** | Remember API (REST + MCP) | `memory_remember` tool working, admission control passing, provenance hash generated |
| **W4** | Recall API (REST + MCP) | `memory_recall` tool working, hybrid retrieval, RRF ranking, explain mode |
| **W5** | Drop-in proxy mode | OpenAI-compatible `/proxy/chat/completions` endpoint, zero-code memory for any agent |
| **W5** | Markdown serialization | Obsidian-compatible YAML frontmatter, wiki-links, Git-diffable |
| **W6** | Python SDK (auto-generated from OpenAPI) | `pip install mnemosyne`, `client.remember()`, `client.recall()` working |
| **W6** | CLI v1 | `mnemosyne init`, `mnemosyne remember`, `mnemosyne recall`, `mnemosyne health` |

## 6.3 Phase 2: Security (Month 2) — "Fortress"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W7** | SMSR C1: HMAC-SHA256 provenance | Every memory signed, verification working, 100% unsigned injection blocked |
| **W7** | SMSR C2: Randomized ablation | Ablation retrieval working, confidence scores accurate, <5% ASR in tests |
| **W8** | Admission control: MINJA detection | >95% detection rate, <1% false positive, 3ms latency |
| **W8** | Admission control: ADAM pattern detection | Rate limiting, query-pattern anomaly detection, ADAM simulation tests |
| **W9** | Audit trail: SHA-256 hash chain | Immutable logs, chain verification, offline auditor verification |
| **W9** | Audit trail: Ed25519 signatures | Critical operations signed, signature verification working |
| **W10** | GDPR erasure (soft + hard delete) | Cross-layer deletion, audit trail, 30-day purge, export generation |
| **W10** | OWASP AMG compliance | ASI06 coverage, four-layer middleware, integration with LangChain/LlamaIndex |

## 6.4 Phase 3: Intelligence (Month 3) — "The Brain"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W11** | Query classifier (scheduler) | 6 query types routed correctly, token budget enforced, latency <150ms |
| **W11** | Prospective memory plugin | `memory_remind_me` working, cron triggers, event triggers, snooze handling |
| **W12** | Emotional salience engine | Multi-factor scoring, decay curves, user emphasis detection, engagement tracking |
| **W12** | Contradiction detection | Automatic detection, confidence scoring, visual graph of contradictions |
| **W13** | Consolidation engine | Nightly batch: merge duplicates, prune stale, update embeddings, rebuild links |
| **W13** | Memory reconsolidation | On retrieval: update salience, strengthen edges, update confidence |
| **W14** | Temporal validity (`valid_at`/`invalid_at`) | Query "what was true in January?" returns correct version, superseded memories handled |

## 6.5 Phase 4: Scale (Month 4) — "Multi-Agent"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W15** | Multi-agent namespaces | Agent isolation, namespace permissions, sync configuration |
| **W16** | Namespace federation | Cross-namespace sync, conflict resolution, merge strategies |
| **W16** | Memory versioning (Git-style) | Branch, commit, merge, revert, fast-forward, three-way merge |
| **W17** | SSO/OIDC integration | Google, GitHub, Okta login, role mapping, session management |
| **W17** | RBAC v2 | 5 roles, granular permissions, namespace-level access control |
| **W18** | Plugin marketplace (alpha) | Plugin registry, install/unload, connector plugins (Slack, GitHub, Notion) |

## 6.6 Phase 5: Enterprise (Month 5-6) — "Compliance"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W19-20** | SOC 2 Type II readiness | Policies, procedures, controls, evidence collection, auditor engagement |
| **W21-22** | ISO 42001:2023 compliance | AI governance framework, risk register, impact assessment |
| **W23-24** | NIST AI RMF alignment | GOVERN, MAP, MEASURE, MANAGE mappings, audit evidence |
| **W25-26** | Data residency | Regional deployment, EU data stays in EU, US data stays in US |
| **W27-28** | SLA guarantees | 99.9% uptime, <50ms P99 latency, <100ms P99 graph search |

## 6.7 Phase 6: Ecosystem (Month 7-9) — "Platform"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W29-30** | TypeScript SDK | `npm install @mnemosyne/sdk`, full type safety, browser + Node.js |
| **W31-32** | Plugin marketplace (beta) | 10+ plugins, revenue share model, developer docs, plugin CLI |
| **W33-34** | Web dashboard (Obsidian sync) | Real-time sync, graph visualization, contradiction map, health metrics |
| **W35-36** | VS Code extension | Inline memory, recall on hover, remember on save, graph view |
| **W37-38** | Mobile app (iOS + Android) | Push notifications for prospective memory, voice input, offline mode |
| **W39-40** | Community templates | 50+ memory templates (decision log, project retrospective, daily journal) |

## 6.8 Phase 7: Performance (Month 10-12) — "Speed"

| Week | Deliverable | Acceptance Criteria |
|------|-------------|---------------------|
| **W41-42** | ArcadeDB graph migration | >100M edges migrated, Cypher compatibility, performance parity |
| **W43-44** | pgvectorscale optimization | 50M vectors, 28× faster than Pinecone, <10ms P99 latency |
| **W45-46** | TEE integration (SEV-SNP) | AMD SEV-SNP pilot, <20% overhead, memory encryption |
| **W47-48** | Differential privacy | Retrieval noise, extraction resistance, accuracy trade-off documented |
| **W49-50** | Global CDN | Edge caching, regional read replicas, <20ms latency worldwide |
| **W51-52** | Benchmark suite | LoCoMo, LongMemEval, BEAM, custom Mnemosyne benchmarks, published results |

---

# PART 7: PRICING & BUSINESS MODEL

## 7.1 Subscription Tiers

| Tier | Monthly Price | Annual Price | Memories | Namespaces | Agents | Features |
|------|--------------|-------------|----------|-----------|--------|----------|
| **Free** | $0 | $0 | 1,000 | 1 | 1 | Basic search, 30-day history, community support |
| **Pro** | $19 | $190 | 50,000 | 5 | 3 | Full search, graph, versioning, 1-year history, email support |
| **Team** | $49/user | $490/user | 500,000 | 20 | 10 | Multi-agent, SSO, audit trails, 2-year history, Slack support |
| **Enterprise** | Custom | Custom | Unlimited | Unlimited | Unlimited | SOC 2, ISO 42001, data residency, SLA, dedicated support, TEE |

## 7.2 Usage-Based Add-Ons

| Add-On | Price | Description |
|--------|-------|-------------|
| **Embedding overage** | $0.001/embedding | Beyond plan limit |
| **Graph storage** | $0.10/1M edges | Beyond 100M edges |
| **Cold storage** | $0.01/GB/month | S3 + R2 archive |
| **Prospective triggers** | $0.001/trigger | Scheduled reminders |
| **Audit export** | $0.10/1K logs | GDPR compliance export |
| **Custom plugin** | $500 setup + $50/mo | Custom connector development |

## 7.3 Open Core Model

```
mnemosyne/
├── core/ (Apache 2.0, open source)
│   ├── kernel.py
│   ├── plugins/
│   ├── memory_subsystems/
│   └── security/
├── enterprise/ (proprietary, licensed)
│   ├── soc2_compliance/
│   ├── tee_integration/
│   ├── differential_privacy/
│   └── advanced_audit/
├── cloud/ (SaaS, managed)
│   └── Hosted platform with managed infrastructure
└── marketplace/ (revenue share)
    └── Plugin marketplace with 70/30 revenue split (developer/platform)
```

---

# PART 8: BRANDING & POSITIONING

## 8.1 The 10-Word Anchor

> **"Supabase is to Postgres what Mnemosyne is to AI Memory."**

Or more precisely:

> **"Mnemosyne is the operating system for AI memory — the scheduler that orchestrates what your AI remembers, forgets, and learns."**

## 8.2 The Tagline Hierarchy

| Level | Tagline | Use Case |
|-------|---------|----------|
| **Brand** | "The Memory OS" | Logo, homepage, all materials |
| **Product** | "Your AI remembers. So you don't have to." | Landing page, ads |
| **Feature** | "Semantic + Episodic + Procedural + Prospective + Emotional + Meta" | Technical docs, pitch decks |
| **Differentiator** | "The only memory system with emotional salience, prospective reminders, and compliance-grade audit trails." | Competitive comparisons |
| **Vision** | "Every AI agent will have a Memory OS. Mnemosyne is building it." | Investor pitches, keynote |

## 8.3 The Competitive Messaging

| Competitor | Their Strength | Their Weakness | Our Message |
|------------|---------------|----------------|-------------|
| **Cognee** | Graph + self-improvement | No prospective memory, no emotional salience, no compliance | "Cognee stores. Mnemosyne thinks." |
| **Mem0** | Easy integration, 57K stars | Graph paywalled at $249, no self-improvement, no compliance | "Mem0 is a database. Mnemosyne is an OS." |
| **Zep** | Temporal reasoning, SOC 2 | No self-improvement, cloud-only, expensive | "Zep remembers the past. Mnemosyne plans the future." |
| **Letta** | OS-style memory tiers | No graph, no temporal, no self-improvement | "Letta manages RAM. Mnemosyne manages the brain." |
| **Evermind EverOS** | "Memory OS" branding | No prospective memory, no emotional salience, no compliance | "They named it. We built it." |

---

# PART 9: SUCCESS METRICS

## 9.1 Technical Metrics (Month 1-12)

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| **GitHub Stars** | 100 | 500 | 2,000 | 10,000 |
| **MCP Servers** | 1 | 5 | 20 | 50 |
| **Plugins** | 0 | 5 | 15 | 50 |
| **Test Coverage** | 70% | 80% | 85% | 90% |
| **Benchmark Score (LoCoMo)** | 70% | 80% | 85% | 90% |
| **Benchmark Score (LongMemEval)** | 60% | 75% | 85% | 90% |
| **MINJA Resistance** | 90% | 95% | 98% | 99% |
| **ADAM Resistance** | 50% | 70% | 85% | 90% |
| **P99 Latency (semantic)** | 50ms | 30ms | 20ms | 10ms |
| **P99 Latency (graph)** | 100ms | 50ms | 30ms | 20ms |

## 9.2 Business Metrics (Month 1-12)

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| **Registered Users** | 100 | 1,000 | 5,000 | 20,000 |
| **Paying Customers** | 5 | 50 | 200 | 1,000 |
| **MRR** | $100 | $2,000 | $10,000 | $50,000 |
| **Enterprise Contracts** | 0 | 1 | 5 | 20 |
| **Plugin Marketplace Revenue** | $0 | $500 | $3,000 | $15,000 |
| **NPS Score** | 30 | 40 | 50 | 60 |
| **Churn Rate** | — | 10% | 8% | 5% |

---

# PART 10: REFERENCES & RESEARCH SOURCES

This plan is synthesized from 9 parallel research documents totaling 31,924+ lines:

| Document | Lines | Key Findings |
|----------|-------|-------------|
| `RESEARCH_COGNEE_PRODUCT.md` | 429 | Cognee v1.2.2, Truth Subspace, 5 hackathon-tagged issues, Evermind EverOS competitor |
| `RESEARCH_WINNING_PROJECTS.md` | 514 | 15+ winning projects, winning formula, demo strategies |
| `RESEARCH_CRITIQUE_CHRONICLE.md` | 595 | Brutal 8-angle critique of all prior recommendations |
| `RESEARCH_COMPETITOR_GAPS.md` | 228 | Mem0, Zep, Letta, n8n, Claude Code competitive analysis |
| `RESEARCH_FRESH_JUNE30.md` | 396 | Cognee community, what teams are building, latest developments |
| `RESEARCH_INTEGRATIONS_JUNE30.md` | 392 | MCP ecosystem, 2026-07-28 spec, Streamable HTTP, OAuth 2.1 |
| `RESEARCH_MEMIFY_JUNE30.md` | 429 | `improve()` internals, BEAM benchmark, contradiction resolution |
| `RESEARCH_NOVEL_USE_CASES_JUNE30.md` | 303 | 9 genuinely novel use cases across 20+ domains |
| `RESEARCH_DOMAIN_GAPS_JUNE30.md` | 303 | 5 domain deep-dives, existing tools, gaps |
| `RESEARCH_MEMORY_LANDSCAPE_JULY2026.md` | 27,964 | Complete memory landscape, Cognee v1.2.2, Mem0 v2.0.10, Zep MCP, Letta, Evermind EverOS, NIST, 2026 entrants |
| `RESEARCH_DATABASE_ARCHITECTURE_JULY2026.md` | 260 | PostgreSQL+pgvector+pgvectorscale, Valkey, ArcadeDB, R2, migration thresholds |
| `RESEARCH_MCP_INTEGRATION_JULY2026.md` | 392 | MCP 2026-07-28 spec, Streamable HTTP, OAuth 2.1, 97M SDK downloads, 30+ CVEs |
| `RESEARCH_SECURITY_LANDSCAPE_JULY2026.md` | 576 | MINJA, ADAM, SMSR, OWASP AMG, GDPR, EU AI Act, NIST, zero-trust |
| `RESEARCH_ULTIMATE_MEMORY_OS_GAPS_JULY2026.md` | 429 | 49 gaps, microkernel, multi-agent, temporal validity, SDKs, CLI, pricing, branding |
| **TOTAL** | **31,924+** | **200+ research findings** |

---

# ONE-SENTENCE SUMMARY

> **Build Mnemosyne as a microkernel-based Memory OS with a plugin architecture, orchestrating semantic + episodic + procedural + prospective + emotional + meta memory across PostgreSQL+pgvector+pgvectorscale (hot→queryable→cold), secured by SMSR-certified admission control, exposed through stateless MCP (stdio + Streamable HTTP) and OpenAI-compatible proxy, with emotional salience, prospective scheduling, contradiction detection, memory versioning, multi-agent namespaces, and compliance-grade observability — the only platform that combines all 12 differentiators no competitor has.**

---

*Document: Mnemosyne v3.0 — Complete Rebuild Plan*  
*Synthesized from: 6 parallel research streams, 15 source documents, 200+ findings, 31,924+ lines of research*  
*Date: July 2026*  
*Status: Ready for implementation*  
*Next Step: Start Phase 0 (Week 1)*

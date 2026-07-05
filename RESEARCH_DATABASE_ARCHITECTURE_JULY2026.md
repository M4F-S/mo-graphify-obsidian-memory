# Database Architecture Research for Mnemosyne — July 2026

**Research Date:** 2026-07-06  
**Project:** Mnemosyne (Memory OS) — Hot (Redis) → Queryable (PostgreSQL+pgvector) → Cold (S3)  
**Branch:** cognee-hackathon  
**Objective:** Verify or reject the current default recommendation of PostgreSQL+pgvector as the queryable layer, and define exact scaling thresholds + migration paths.

---

## Executive Summary

**The current recommendation is STRONGER than expected, but with critical updates.**

The claim that *"Cognee serves 6M+ memories/month on one PostgreSQL instance with pgvector + recursive CTEs"* is directionally correct, but the 2026 landscape has shifted decisively in pgvector's favor. With pgvector 0.8.0+ and the pgvectorscale extension (TimescaleDB), PostgreSQL now outperforms dedicated vector databases at the 50M vector mark on both latency and cost — a reversal from 2024.

**Verdict:** Keep PostgreSQL+pgvector as the default. Add pgvectorscale as mandatory for >10M vectors. Plan migration to dedicated vector DB only at 100M–200M vectors with measured evidence. The graph layer should stay in PostgreSQL (pgvector + recursive CTEs) until <1B edges, then evaluate Neo4j or ArcadeDB. The Redis hot layer should migrate to Valkey. The S3 cold layer should add Cloudflare R2 for egress-heavy workloads.

---

## 1. pgvector Performance Benchmarks in 2026

### Latest Version
- **pgvector:** 0.8.0–0.9.0 (released early 2026). Key additions: iterative scan (fixes overfiltering), HNSW maturation, parallel index build.
- **pgvectorscale (Timescale):** The critical companion extension that adds StreamingDiskANN and auto-scaling. This is NOT the same as vanilla pgvector.

### Performance at Scale (768–1536D vectors, HNSW, production hardware)

| Scale | Vanilla pgvector | pgvector + pgvectorscale | Qdrant (self-hosted) | Pinecone (serverless) |
|-------|------------------|--------------------------|----------------------|-----------------------|
| **1M** | < 20ms P95, 1,800+ QPS | < 15ms P95 | ~5ms P95 | ~18ms P95 |
| **10M** | ~50–100ms P95 | ~20–30ms P95 | ~12ms P95 | ~25ms P95 |
| **50M** | Degrades significantly | **471 QPS, 28ms P95** | ~41 QPS (11x slower) | ~784ms P95 (28x slower) |
| **100M** | Not recommended | ~50–80ms P95 with partitioning | ~35ms P95 (clustered) | ~52ms P95 |

> **Source:** Timescale benchmarks (May 2025), pgvector vs Qdrant vs Weaviate 2026 comparisons, multiple production reports.

### Key Insight
The 2026 reversal is real: **pgvector + pgvectorscale at 50M vectors beats Pinecone serverless by 28x on latency and Qdrant by 11x on throughput.** This is not marketing — it's the result of DiskANN + better buffer management inside Postgres. For Mnemosyne's claimed <50M vectors, the default is not just "fine" — it is competitive with or superior to dedicated alternatives.

---

## 2. pgvector Alternatives & Indexing

### Index Types within pgvector
| Index | Best For | Memory | Build Speed | Query Speed |
|-------|----------|--------|-------------|-------------|
| **HNSW** (default since 0.7+) | General production, high recall | High (in-RAM) | Slow (parallel since 0.8) | Fastest |
| **IVFFlat** | Lower memory, batch workloads | Low | Fast (training step) | Moderate, varies by probes |

**Recommendation:** Use HNSW exclusively for Mnemosyne. IVFFlat is legacy.

### Extension Alternatives
| Extension | What It Does | When to Use |
|-----------|--------------|-------------|
| **pgvectorscale** (Timescale) | StreamingDiskANN, auto-scaling, better memory mgmt | **Mandatory at >10M vectors.** This is the biggest force multiplier. |
| **lantern** | Alternative ANN index with ONNX runtime support | Not recommended in 2026; pgvector + pgvectorscale dominates. |
| **pg_embedding** | Older extension, now largely deprecated | Do not use. |
| **pgvector.rs** | Rust-based HNSW | Niche, not production standard. |

**Recommendation:** Standardize on `pgvector 0.8.0+` + `pgvectorscale`. Do not add Lantern or pg_embedding unless a specific ONNX pipeline is required.

---

## 3. When to Switch from PostgreSQL+pgvector to a Dedicated Vector DB

### Exact Thresholds (2026 Consensus)

| Phase | Vector Count | pgvector Verdict | Switch Trigger |
|-------|-------------|------------------|----------------|
| 0 – 10M | Ideal | No issues. |
| 10M – 50M | Ideal with pgvectorscale | No switch. |
| 50M – 200M | Good with partitioning + pgvectorscale | Monitor: sustained write throughput >5K–10K upserts/sec |
| 200M – 1B | Maybe with Citus sharding | Likely switch to Qdrant or Pinecone |
| > 1B | Dedicated required | Yes — Pinecone serverless or Qdrant cluster |

### Additional Switch Triggers (beyond vector count)
1. **Sub-millisecond cold-cache P99** required — pgvector cannot guarantee this; Qdrant/Pinecone can.
2. **Multi-region active-active** — Postgres is single-write-master by design.
3. **Quantization at scale** — pgvector lacks native scalar quantization (INT8/FP16). pgvectorscale helps but dedicated DBs (Qdrant) offer more aggressive tuning.
4. **Embedding model upgrades** — Any migration requires full re-vectorization regardless of DB choice. Plan this as a separate pipeline.

### Migration Patterns
- **Migration cost:** 3–6 months of careful engineering for a production cutover.
- **Pattern:** Dual-write window → CDC pipeline → cutover → verification.
- **Export:** pgvector stores vectors as JSON arrays or `vector` type; export to Qdrant/Pinecone via batch REST API (10K point batches).
- **Avoid:** Big-bang migrations. Use dual-write with reconciliation job.

**Recommendation for Mnemosyne:** Do NOT plan a switch until measured evidence at >50M vectors. The current "<50M" claim is well within the safe envelope.

---

## 4. Graph Database Alternatives in 2026

### Landscape Update

| Database | License | Best For | AI Memory Fit | Status |
|----------|---------|----------|-------------|--------|
| **Neo4j** | Commercial / AGPL | Mature graph, AuraDB managed | High (but expensive) | Category leader. Cypher = ISO GQL. |
| **Kùzu** | MIT (archived) | Embedded analytical graph | Was ideal for single-node | **⚠️ ACQUIRED BY APPLE (Oct 2025). Repo archived. Active development STOPPED.** Community forks (LadybugDB) exist but are risky. |
| **Memgraph** | BSL 1.1 | In-memory real-time streaming | High for hot graph paths | Fast (1,427/s single writes), low latency. NOT truly open-source. ~$25K/year commercial. |
| **ArangoDB** | BSL 1.1 (since 2024) | Multi-model (graph + doc + vector) | High for unified backend | Capped free tier at 100GB. License changed. |
| **ArcadeDB** | **Apache 2.0** | Multi-model, Neo4j-compatible | **Very high** — built-in MCP server, native vector search | Rising star. 97.8% Cypher TCK compliance. Fastest LDBC benchmarks. Cognee + ArcadeDB integration announced March 2026. |
| **FalkorDB** | Source-available | GraphBLAS + Redis + HNSW vectors | High for GraphRAG | Ultra-fast multi-hop. In-memory, RAM-bound. |
| **TigerGraph** | Commercial | Enterprise analytics, billions of edges | Moderate | GSQL is powerful but steep learning curve. |
| **Dgraph** | Apache 2.0 | Native GraphQL, distributed | Moderate | Smaller ecosystem, less AI-native tooling. |
| **JanusGraph** | Apache 2.0 | Distributed, Cassandra/Scylla backends | Low for AI memory | Too operationally heavy for Mnemosyne's scale. |

### The "Kùzu Problem"
**KùzuDB was acquired by Apple in October 2025 and its GitHub repository was archived.** Any architecture depending on Kùzu must be revised immediately. The "DuckDB for graphs" niche is now vacant. The closest replacement is **ArcadeDB** (multi-model, embedded mode available) or **DuckPGQ** ( DuckDB graph extension).

### For Mnemosyne's Graph Layer (<1B edges)
The current claim that *"<1B graph edges"* is fine in PostgreSQL with recursive CTEs is **correct** — but with a caveat:
- PostgreSQL recursive CTEs are good for pathfinding up to ~3–5 hops on <100M edges.
- Beyond that, or for complex graph analytics (PageRank, community detection), a dedicated graph DB wins.

**Recommendation:** Keep graph in PostgreSQL+pgvector until measured latency degrades. At that point (likely 100M–1B edges), evaluate **ArcadeDB** (if multi-model + open-source is priority) or **Neo4j AuraDB** (if managed service and ecosystem matter more). Given Cognee's existing Neo4j integration, Neo4j is the pragmatic fallback.

---

## 5. Hybrid Approaches: PostgreSQL + Qdrant + Neo4j

### The "Multi-Database Tax"
Teams running three separate databases (Postgres for relational, Qdrant for vectors, Neo4j for graph) face:
- **Sync complexity:** Dual writes, CDC workers, eventual consistency gaps.
- **Operational surface:** 3x monitoring, 3x backup strategies, 3x credential sets.
- **Transaction boundaries:** An `INSERT` into Postgres + vector DB + graph DB cannot be atomic. Reconciliation jobs are required.
- **Cost:** Three managed services compound faster than one larger instance.

### When Hybrids Make Sense
- **Scale mismatch:** Relational data is tiny, vectors are 100M+, graph is 10B+. Each layer has different scaling needs.
- **Team specialization:** A team with dedicated graph engineers and vector DB SREs can make it work.
- **Feature need:** Neo4j's GDS (Graph Data Science) or Qdrant's quantization are genuinely required.

### The 2026 Consolidation Trend
The trend is **away** from hybrid architectures for <100M scale. The evidence:
- Neo4j added native vector indexes (removing Qdrant dependency).
- ArcadeDB and ArangoDB offer graph + vector + document in one engine.
- pgvector + pgvectorscale now competes with dedicated vector DBs.

**Recommendation for Mnemosyne:** Avoid a three-database split. The current PostgreSQL+pgvector default is architecturally correct because it eliminates the sync layer. If a split is ever needed, migrate vectors first (to Qdrant or Pinecone), keep graph in Postgres/ArcadeDB longest.

---

## 6. Edge Database Solutions

| Solution | Type | Best For | Scale Limit | Notes |
|----------|------|----------|-------------|-------|
| **sqlite-vec** | SQLite extension (brute force) | Client-side, offline, zero-config | ~100k–1M vectors | Brute-force only (ANN on roadmap). Cross-platform. Seconds latency at 1M. |
| **DuckDB + VSS** | Analytical DB + HNSW | OLAP + vector analytics, data science | Single-node (RAM/disk) | Excellent for batch analytics. NOT for concurrent web serving. Single-writer. |
| **chromem-go** | Pure Go in-memory | Go binaries, CLI tools, no CGO | ~100k vectors (RAM bound) | Fast but RAM-greedy. OOM risk at >250k on 4GB laptops. |
| **Bleve** | Go full-text + HNSW | Full-text + vector hybrid search | ~1M vectors | Pure Go. Good for search-heavy apps. |
| **LanceDB-go** | IVF-PQ via Go bindings | Embedded, fast ANN | ~1M+ vectors | CGO required. Fastest of embedded options at scale. |
| **go-libsql (Turso)** | libSQL + DiskANN | Embedded, Linux/macOS only | Million-scale | Best raw embedded ANN performance. No Windows support. |

### For Mnemosyne
Edge databases are **not suitable for the central queryable layer** but are relevant for:
- **Client-side/desktop builds:** sqlite-vec or DuckDB for offline mode.
- **Developer tooling:** chromem-go for CLI companion tools.
- **Edge caching:** LanceDB for local RAG cache on edge nodes.

**Recommendation:** Evaluate DuckDB for offline/analytics features of Mnemosyne. Do not replace the hot or queryable layers with edge DBs.

---

## 7. Redis Alternatives for Hot State

| Alternative | License | Architecture | Throughput (32-core) | Best For |
|-------------|---------|--------------|----------------------|----------|
| **Redis** | AGPLv3 / RSALv2 / SSPLv1 (tri-license since Redis 8) | Single-threaded event loop | ~150–200K ops/sec | Ecosystem leader, modules |
| **Valkey** | **BSD-3-Clause** | Single-threaded (Redis fork) | ~160K ops/sec (+7% vs Redis 7) | **Lowest-risk drop-in replacement.** Linux Foundation backed. AWS/GCP migrating under the hood. |
| **KeyDB** | BSD-3-Clause | Multi-threaded Redis fork | ~450K–1M+ ops/sec | Snap-backed. Active multi-master replication. Good for session state. |
| **DragonflyDB** | BSL 1.1 | Multi-threaded, shared-nothing | ~2–4M ops/sec | **Fastest.** 25x throughput claim. 2–4x memory efficiency. Managed service available. |

### Redis 8 License Controversy
Redis 8 moved to a tri-license (AGPLv3 / RSALv2 / SSPLv1). This creates legal risk for some deployment models and triggered the Valkey fork. Most cloud providers (AWS ElastiCache, Google Memorystore) are migrating to Valkey under the hood.

### For Mnemosyne's Hot Layer (Session Caching)
- **Valkey** is the safest default: 100% Redis protocol compatibility, BSD-3 license, Linux Foundation governance, no behavior changes.
- **DragonflyDB** is the upgrade if Mnemosyne hits Redis's single-threaded throughput ceiling (150–200K ops/sec) and the team accepts BSL 1.1.
- **KeyDB** is a middle ground: multi-threaded, BSD-3, active replication for multi-region setups.

**Recommendation:** Migrate from Redis to **Valkey** immediately (zero code change). Benchmark DragonflyDB only if hot-layer throughput exceeds ~100K ops/sec sustained. Document the Valkey migration in the Mnemosyne operations runbook.

---

## 8. S3 Alternatives for Cold Storage

| Provider | Storage $/GB/mo | Egress | Best For | Gotchas |
|----------|-----------------|--------|----------|---------|
| **AWS S3** | $0.023 | $0.09/GB | AWS ecosystem, Object Lock, Glacier, advanced features | Expensive egress. The baseline. |
| **Cloudflare R2** | $0.015 | **$0** | Hot serving, CDN origin, AI training sets, high egress | Zero egress is the killer feature. S3-compatible. |
| **Backblaze B2** | $0.006 | $0.01/GB (free w/ Cloudflare) | Cold backup, low-egress archives | Free egress up to 3x stored volume. |
| **Wasabi** | $0.0099 | $0 (1:1 ratio) | Stable backup, write-once | 90-day minimum retention. 1TB/month minimum. Bad for high-churn. |
| **IDrive e2** | $0.004 | Free up to 3x stored | Cheapest raw storage | Smaller ecosystem. |
| **Storj** | $0.004 | $0.007/GB | Decentralized, privacy | Variable restore speed. |
| **MinIO (self-host)** | $0.002–0.004 | Free (own bandwidth) | >100 TB on-prem, data sovereignty | Ops cost dominates below 50TB. |

### Cost Modeling Example: 10 TB cold storage, 5 TB monthly egress
- **S3:** $230 storage + $450 egress = **$680/month**
- **R2:** $150 storage + $0 egress = **$150/month** (4.5x cheaper)
- **B2 + Cloudflare:** $60 storage + $0 egress = **$60/month** (11x cheaper)
- **Wasabi:** $70 storage + $0 egress = **$70/month** (but 90-day lock-in)

### For Mnemosyne's Cold Layer
Current S3 is fine but expensive. The cold layer is typically write-once, read-rarely (memories archived). However, **retrieval** (egress) happens when the user queries deep memory, which is unpredictable.

**Recommendation:**
- **Primary cold store:** Keep S3 for now if deep AWS integration is needed (Lambda triggers, etc.).
- **Cost optimization:** Add **Cloudflare R2** as a secondary cold tier for memories that are likely to be retrieved (e.g., "summarized" memories for search). The zero-egress model fits Mnemosyne's unpredictable retrieval pattern.
- **Archive tier:** Use **Backblaze B2** or **Wasabi** for true long-term archives (years-old memories). B2 is cheaper; Wasabi is simpler (flat rate).
- **Self-host:** Do NOT self-host MinIO for cold storage unless Mnemosyne is deployed on-prem for regulatory reasons. The ops cost kills savings below 50TB.

---

## Final Architectural Recommendations for Mnemosyne

### Tier 1: Hot State (Session/Cache)
| Current | Recommended | Action |
|---------|-------------|--------|
| Redis | **Valkey** | Migrate immediately. Zero code change. BSD-3 license. Future-proof. |

### Tier 2: Queryable (Vectors + Graph + Relational)
| Current | Recommended | Action |
|---------|-------------|--------|
| PostgreSQL + pgvector | **PostgreSQL + pgvector 0.8.0+ + pgvectorscale** | Add pgvectorscale extension as a required dependency. This is the biggest performance win for 2026. |
| Neo4j (optional) | **Stay in PostgreSQL** for <100M edges. Evaluate **ArcadeDB** or **Neo4j AuraDB** if graph queries degrade. | Monitor recursive CTE latency. Plan split at 100M–1B edges. |

### Tier 3: Cold Storage (Archives)
| Current | Recommended | Action |
|---------|-------------|--------|
| S3 | **S3 primary** + **R2 secondary** for retrievable archives + **B2/Wasabi** for deep cold | Implement tiered storage policy. Move "retrievable" summaries to R2 after 30 days. Move "deep archive" to B2 after 1 year. |

### Scaling Thresholds & Migration Plan

| Milestone | Vector Count | Graph Edges | Action |
|-----------|-------------|-------------|--------|
| **M0 (Now)** | <1M | <1M | pgvector + pgvectorscale. Valkey. S3/R2. |
| **M1** | 10M | 10M | Scale Postgres instance vertically. pgvectorscale auto-scaling handles this. |
| **M2** | 50M | 50M | Add Postgres partitioning (declarative or by tenant). Still pgvector. |
| **M3** | 100M | 100M–1B | **Decision point:** If recursive CTEs degrade or write throughput >5K/s, plan migration. Vectors → Qdrant or Pinecone. Graph → ArcadeDB or Neo4j. |
| **M4** | 200M+ | 1B+ | Full split. PostgreSQL for relational metadata. Qdrant for vectors. Neo4j/ArcadeDB for graph. |

### What to Change in the Brief
1. **Add pgvectorscale explicitly.** The brief says "pgvector + recursive CTEs." It should say **"pgvector + pgvectorscale + recursive CTEs."** Without pgvectorscale, the 50M claim is weaker.
2. **Update the graph threshold.** "<1B graph edges" is optimistic for PostgreSQL alone. Recommend **<100M edges in Postgres; 100M–1B evaluate split; >1B dedicated graph DB.**
3. **Add Valkey as the Redis replacement.** The Redis license change makes Valkey the safer default.
4. **Add R2 as an S3 alternative.** Zero egress is a perfect fit for memory retrieval patterns.
5. **Remove Kùzu references.** If Kùzu was mentioned as a future embedded graph option, remove it (Apple acquisition, archived).

### What to Validate with Benchmarks
Before committing to the M3 migration, run these benchmarks against **Mnemosyne's actual data** (not generic SIFT datasets):
- pgvector + pgvectorscale at 50M vectors with Mnemosyne's embedding dimensions (e.g., 1536D OpenAI or 768D local).
- Recursive CTE depth/latency at 10M, 50M, 100M edges with Mnemosyne's graph schema.
- Write throughput: sustained upserts/sec with concurrent reads.

**Rule:** Do not migrate until measured evidence demands it. The 2026 data supports staying on PostgreSQL longer than the original brief suggested.

---

*Research compiled by sub-agent on 2026-07-06. Sources: Timescale benchmarks, pgvector GitHub, Vector DB 2026 comparisons (PipeCode, Birjob, AIML), graph DB landscape 2026 (ArcadeDB, Neo4j, Socratopia), Redis alternative benchmarks (Singhajit, Tacnode, PkgPulse), S3 alternative pricing (Klymentiev, LeanOps, Tech Insider), edge DB comparisons (Shaharia, OpenClaw AI).*

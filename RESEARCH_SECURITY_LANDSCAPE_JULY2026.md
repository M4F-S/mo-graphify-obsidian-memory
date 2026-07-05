# Security Landscape for AI Memory Systems — Research Brief
**Date:** July 2026  
**Project:** Mnemosyne (Memory OS)  
**Classification:** Internal — Security Architecture Roadmap  
**Analyst:** Research Sub-Agent (Kimi Work)

---

## Executive Summary

AI memory systems have become the primary attack surface for agentic AI in 2026. The shift from stateless prompt injection to persistent memory poisoning represents a structural threat escalation: a single successful injection can corrupt behavior across all future sessions. The research landscape converges on several critical findings:

- **MINJA** achieves >95% injection success in idealized settings; real-world rates fall to 20–40% but remain an unacceptable systemic risk.
- **ADAM** extracts sensitive memories with up to 100% attack success rate via adaptive entropy-guided querying.
- **SMSR** (arXiv:2606.12703, June 2026) is the **first certified defense** against multi-session memory poisoning, combining HMAC-SHA256 provenance with randomized memory ablation and verdict-based majority voting.
- **OWASP Agent Memory Guard** provides a four-layer runtime middleware (cryptographic baselines, anomaly detection, trust scoring, forensic snapshots) but lacks formal certification.
- The **EU AI Act** becomes fully enforceable for high-risk systems on **August 2, 2026**, carrying penalties up to €35M or 7% global turnover. GDPR Article 17 erasure in vector stores remains technically unsolved by most commercial platforms.
- **Zero-trust memory architectures** (e.g., MemTrust) are emerging, using TEEs (AMD SEV-SNP, Intel TDX, SGX, Nitro Enclaves) to protect the entire memory lifecycle with <20% performance overhead.

This document provides threat intelligence, defense recommendations, and a phased implementation roadmap for Mnemosyne.

---

## Table of Contents

1. [MINJA: Memory Injection Attacks](#1-minja-memory-injection-attacks)
2. [ADAM: Automated Data Extraction](#2-adam-automated-data-extraction-from-memory)
3. [OWASP Agent Memory Guard](#3-owasp-agent-memory-guard)
4. [Prompt Injection Defenses for Memory Systems](#4-prompt-injection-defenses-for-memory-systems)
5. [Data Poisoning on Vector Databases & Knowledge Graphs](#5-data-poisoning-on-vector-databases--knowledge-graphs)
6. [Memory Tampering & Integrity](#6-memory-tampering--integrity)
7. [GDPR Art.17 & EU AI Act Compliance](#7-gdpr-article-17--eu-ai-act-compliance)
8. [Audit Trail Requirements & Standards](#8-audit-trail-requirements--standards)
9. [Red Teaming for AI Memory Systems](#9-red-teaming-for-ai-memory-systems)
10. [Zero-Trust Architecture for AI Memory](#10-zero-trust-architecture-for-ai-memory)
11. [Security Roadmap & Phased Recommendations](#11-security-roadmap--phased-recommendations)

---

## 1. MINJA: Memory Injection Attacks

### Latest Research

- **MINJA** (Memory INJection Attack) — Dong et al., NeurIPS 2025; arXiv:2601.05504 (Jan 2026 follow-up).  
- **InjecMEM** — ICLR 2026 submission. Single-interaction targeted poisoning via retriever-agnostic anchor + gradient-optimized trigger.

### Attack Vectors

MINJA operates through **query-only interaction** — no elevated privileges, no API access, no direct writes to the memory store. The attacker crafts seemingly benign conversational queries that cause the agent to autonomously generate and store malicious reasoning steps.

| Technique | Description |
|---|---|
| **Bridging Steps** | Intermediate logical steps that appear reasonable individually but chain toward a malicious goal. |
| **Indication Prompts** | Carefully crafted additions that induce the agent to generate memorizable content serving the attacker. |
| **Progressive Shortening** | Gradually removes explicit attack prompts while preserving malicious logic, leaving only plausible poisoned entries. |
| **Indirect Injection (e.g., Unit 42, Oct 2025)** | Malicious payloads embedded in web pages/documents fetched by the agent; forged XML tags trick the agent into treating content as system instructions. |

### Success Rates

- **Laboratory/idealized:** >95% injection success rate; 70–84% attack success rate across ReAct shopping, healthcare (EHR), and QA agents on GPT-4/GPT-4o.
- **Realistic deployments** (pre-existing legitimate memories, varied retrieval parameters): drops to **~28–38% on GPT-4o-mini**, **~20–40% on frontier models** under production-representative conditions.
- **Critical insight:** Even 28% ASR against a production agent is a systemic risk. The attack surface exists wherever persistent memory feeds the agent decision loop.

### Defense Mechanisms

From arXiv:2601.05504 (Memory Poisoning Attack and Defense on Memory Based LLM-Agents):

1. **Input/Output Moderation** — composite trust scoring across multiple orthogonal signals (syntax, semantic drift, behavioral consistency).
2. **Memory Sanitization with Trust-Aware Retrieval** — temporal decay (older entries weighted down) + pattern-based filtering.
3. **Careful threshold calibration** — overly conservative thresholds block all entries; insufficient thresholds miss subtle attacks.

### Recommendation for Mnemosyne

- **Priority: P0 (Critical)** — Implement **composite trust scoring** at the ingestion gate. Every memory write must pass multi-signal validation before persistence.
- **Priority: P1** — Deploy **temporal decay** on memory entries so unverified or older entries carry less retrieval weight.
- **Priority: P1** — Maintain a **high-quality seed corpus** of legitimate memories. The presence of competing valid records dramatically reduces MINJA effectiveness.

---

## 2. ADAM: Automated Data Extraction from Memory

### Latest Research

- **ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying** — Xingyu Lyu et al., arXiv:2604.09747 (April 2026). Under review at ICLR.

### Extraction Techniques

ADAM treats memory extraction as an **adaptive, iterative optimization problem** rather than a brute-force query bombardment.

| Step | Mechanism |
|---|---|
| **Initialization** | Seed with high-level domain topics (e.g., diagnosis, medication, patient for healthcare) with uniform priors. |
| **Anchor Extraction** | From each agent response, extract candidate anchors (entities, facts) that reveal memory contents. |
| **Probability Update** | Update selection probabilities for next-query anchors based on retrieved information. |
| **Entropy-Guided Query Generation** | Construct next query to maximize information leakage using prefix-suffix injection + alignment commands. |

### Success Rates

- **Up to 100% ASR** (Attack Success Rate) on tested agents, substantially outperforming prior state-of-the-art extraction attacks.
- Validated across real-world agent domains: healthcare EHR agents, e-commerce assistants, general knowledge agents.
- The attack is **query-only** — no model access, no training data access, no side channels.

### Defenses

- **Rate-limiting + query-pattern anomaly detection** — ADAM’s adaptive nature generates distinctive query sequences (entropy-seeking, iterative refinement).
- **Memory access quantization** — return only k memory entries per query; do not expose full retrieval metadata.
- **Differential privacy** on retrieved memory summaries — add calibrated noise to prevent precise inference of stored records.
- **Access logging + behavioral drift detection** — flag users who issue systematically information-seeking query chains.

### Recommendation for Mnemosyne

- **Priority: P0** — Implement **per-user query-rate limiting and query-pattern anomaly detection**. ADAM queries are structurally distinguishable from benign user interaction.
- **Priority: P1** — Cap retrieval **metadata exposure** — never return raw memory IDs, embedding distances, or full corpus statistics to the user.
- **Priority: P2** — Evaluate **differential privacy** on memory retrieval outputs for high-sensitivity domains (healthcare, finance).

---

## 3. OWASP Agent Memory Guard

### Latest Version & Coverage

- **OWASP Top 10 for Agentic Applications 2026** — released December 2025.  
  - **ASI06: Memory and Context Poisoning** — ranked threat category.
  - **ASI01: Prompt Injection** — related but distinct; session-scoped vs. persistent.
- **OWASP Agent Memory Guard Project** — open-source middleware for LangChain, LlamaIndex, CrewAI.

### Four Defense Layers

| Layer | Control | What It Catches |
|---|---|---|
| **1. Cryptographic Baselines** | SHA-256 hashes of memory blobs at rest; continuous validation | Tampering between writes (file-level, disk-level) |
| **2. Real-Time Anomaly Detection** | Rapid state-change detection, protected key modification, unusual blob size expansion | Injection-payload signatures (classic pattern) |
| **3. Composite Trust Scoring + Temporal Decay** | Older + unverified entries receive less retrieval weight | Dormant poisoned entries that activate later |
| **4. Forensic State Snapshots** | Automatic capture of pre-poisoning state | Enables rollback to known-good cognitive state |

### Gaps

- **No formal certification** — OWASP AMG is a practical middleware, not a mathematically certified defense. SMSR (June 2026) closes this gap.
- **SHA-256 catches tampering between snapshots but not adversarial writes flowing through legitimate channels** — e.g., a MINJA-class attack where the agent itself writes the poison via signed path.
- **Anomaly detection misses subtle poisoning** that mimics normal user-edit patterns (e.g., InjecMEM-style sleeper triggers).
- **Trust scoring alone** lets a recent, cleverly-authenticated injection through if it scores high on freshness and source reliability.
- **No native coverage for ADAM-style extraction** — the defense stack is write/integrity focused, not read/exfiltration focused.
- **No vector-store-specific** embedding-poisoning defenses (LLM08 gap).

### Recommendation for Mnemosyne

- **Priority: P0** — Adopt OWASP AMG as the **baseline runtime defense layer**, but do not treat it as sufficient.
- **Priority: P0** — Augment with **SMSR** (certified defense) for the memory-write path and **retrieval-time ablation** for the read path.
- **Priority: P1** — Extend the stack with **ADAM-specific extraction detection** (query entropy monitoring, rate-limiting).

---

## 4. Prompt Injection Defenses for Memory Systems

### Current State

Traditional prompt-injection defenses treat the **input channel** as the primary threat vector. They generally fail against memory poisoning because once malicious content is accepted as a benign memory entry, it bypasses instruction filters by originating from the agent’s **trusted internal state**.

| Defense | Mechanism | Limitation |
|---|---|---|
| **Sandwich Defense** | Enclose untrusted data between user goal statements | Fails when poisoned memory is retrieved as "trusted context" |
| **Spotlighting** | Delimit data boundaries with markers | Same — trusted internal state bypasses boundary markers |
| **Instructional Reminders** | System prompt reiterates instructions | Memory entries can override or shadow system prompts |
| **CaMeL / FIDES / Progent** | Out-of-band integrity checks | Gains validated only against static benchmarks; adaptive attacks erode them |
| **SMSR (Jun 2026)** | HMAC-SHA256 provenance + randomized ablation + verdict-based majority voting | **First certified defense** — works at memory layer, not prompt layer |

### Why Memory-Layer Defense Is Different

The critical insight from SMSR (arXiv:2606.12703):

> *"We prove an impossibility result showing that no provenance-free retrieval-time filter can certify against adaptive injection."*

Any defense that does not cryptographically bind memory provenance at **write time** and statistically ablate at **read time** cannot provide certified robustness.

### SMSR Deep Dive

- **Component 1 — HMAC-SHA256 Provenance at Write Time:** Every memory entry is signed by an authorized writer. Unsigned entries are blocked at ingestion.  
  - Result: cuts ASR from 93–100% to **0%** for all unsigned variants.
- **Component 2 — Randomized Memory Ablation + Verdict-Based Majority Voting at Query Time:** Randomly subset retrieved memories and aggregate model verdicts (not string outputs).  
  - Result: authenticated-adversary single-injection ASR held to **8.0%** (95% CI [5.8%, 10.9%]), below the certified worst-case δ=10.4%.
  - End-to-end query-only MINJA attack: SMSR reduces ASR from 65.3% to **5.3%**.
- **Consistent Minority Effect:** String-based majority voting is gamed by adversaries generating consistent but wrong answers. Verdict-based aggregation removes this effect.
- **Utility:** 90% under Component 1 alone; 85% under combined defense.

### Recommendation for Mnemosyne

- **Priority: P0** — Implement **SMSR Component 1** (HMAC-SHA256 provenance) for all memory writes. This is the single highest-impact security control available in 2026.
- **Priority: P0** — Implement **SMSR Component 2** (randomized ablation + verdict-based voting) for all memory retrievals feeding agent context windows.
- **Priority: P1** — Add **retrieval-layer injection detection** (regex + semantic boundary checks) between vector DB query and context assembly, as a defense-in-depth layer.
- **Priority: P2** — Evaluate **out-of-band integrity checks** (FIDES, CaMeL) as supplementary, not primary, defenses.

---

## 5. Data Poisoning on Vector Databases & Knowledge Graphs

### Attack Landscape

| Attack | Mechanism | Impact |
|---|---|---|
| **PoisonedRAG** (Zou et al., USENIX Security 2025) | Poison fraction of corpus to induce targeted behaviors | ~250 malicious docs sufficient to backdoor LLMs of any size |
| **AgentPoison** (Chen et al., NeurIPS 2024) | Constrained optimization to generate trigger phrases mapping malicious docs into unique embedding clusters | >80% ASR at <0.1% poison rate; <1% benign performance degradation |
| **CorruptRAG** (2026) | Single injected text flips answers for targeted query | One bad document is enough |
| **Knowledge Graph Embedding Poisoning** (Zhang et al.) | Poison training data of KGE to add/forget facts | Manipulates recommendation systems, QA |
| **MCP Tool Poisoning** (2026 CVEs) | Payload hides inside tool description metadata | Invisible to retrieval-layer defenses |
| **Spring AI CVEs (Apr 2026)** | Filter-expression injection, document-ID injection, cross-tenant memory leakage | Direct vector-store exploitation |

### How Attackers Poison Embeddings

1. **Embedding-collision attacks** — adversarially crafted inputs appear semantically similar to legitimate queries but retrieve poisoned content.
2. **Gradient-optimized triggers** — AgentPoison uses constrained optimization to find trigger phrases that create a unique embedding cluster for malicious documents.
3. **Multi-hop query manipulation** — optimized single-document attacks that chain across multiple retrieval steps.
4. **Clean-label poisoning** — correctly labeled but strategically placed nodes that mislead decision boundaries without appearing anomalous.

### Detection & Cleanup

| Technique | Coverage | Limitation |
|---|---|---|
| **Data Sanitization / Outlier Removal** | Removes obvious statistical outliers | Clever adversaries place poison close to clean data |
| **Spectral Anomaly Detection** | Detects structural anomalies in graph embeddings | Requires full-graph observability; impractical in distributed systems |
| **RAGuard** | Retrieval-time detection filter | Complementary; not sufficient alone |
| **Robust Training Pipelines** | Evaluate perturbation sensitivity across clusters | Training-time cost; runtime benefit |
| **Provenance-Based Filtering (SMSR)** | Cryptographic attestation of source | Strongest guarantee; only trusted sources enter store |
| **Periodic Embedding Space Audit** | Cluster analysis, drift detection | Requires baseline "clean" reference distribution |

### Recommendation for Mnemosyne

- **Priority: P0** — **Source authentication** before any document enters the vector store or KG. Untrusted documents must be quarantined until provenance is verified.
- **Priority: P0** — Implement **embedding-space anomaly detection** at ingestion time (cluster distance checks, outlier scoring).
- **Priority: P1** — Deploy **RAGuard-style retrieval filtering** to detect poisoned chunks at query time.
- **Priority: P1** — Run **periodic embedding-space audits** (weekly/monthly) to detect drift and clustering anomalies.
- **Priority: P2** — Evaluate **robust training objectives** for any custom embedding models.

---

## 6. Memory Tampering & Integrity

### Threat Model

Memory tampering attacks target the **storage and transport layers** of the memory pipeline:

- **Spoofing** — replace a value directly with attacker-controlled data.
- **Splicing** — exchange a value with data from a different location.
- **Replay** — roll back to an older version of the same memory entry.
- **Swap/disk tampering** — tamper with memory offloaded to disk (classic Merkle tree gap).
- **Cross-tenant leakage** — CVE-2026-40966 demonstrated cross-tenant memory leakage through conversation IDs in vector stores.

### Integrity Mechanisms

| Mechanism | What It Protects | Trade-off |
|---|---|---|
| **SHA-256 / HMAC per memory blob** | Tampering at rest; integrity between writes | No protection against adversarial writes through legitimate channels |
| **Merkle Trees** | Log-scale tamper evidence; O(log n) verification | Storage overhead (up to 50% of L2 cache in some implementations); swap/disk gap |
| **Ed25519 Signed Decision Receipts** | Tamper-evident audit trail; offline auditor verification | Key management complexity; performance overhead for high-throughput systems |
| **Hash-Chained Logs** | Sequential tamper detection; replay resistance | Requires append-only log design; compaction conflicts with chain integrity |
| **TEE-Based Memory Encryption** (AMD SEV-SNP, Intel TDX, SGX, Nitro) | Full memory lifecycle protection in use, at rest, and in transit | 10–20% performance overhead; vendor lock-in risk; attestation complexity |
| **Sealed Segments (MemTrust)** | Hot segments in TEE RAM; cold segments encrypted offloaded | Balances latency and security; requires TEE hardware |

### Merkle Tree Implementation for Memory Logs

For tamper-evident audit logging of memory operations:
- **Leaf nodes:** SHA-256 of individual memory operation records (write, read, update, delete).
- **Internal nodes:** Hash of child concatenations.
- **Root anchor:** Stored in tamper-resistant hardware (TPM, secure enclave).
- **Inclusion proofs:** O(log n) verification that a specific operation is in the log.
- **Adaptive chunking:** Resource-aware batch sizing for IoT/edge-scale deployments (130K logs/s, 22ms per entry in 2026 benchmarks).

### Recommendation for Mnemosyne

- **Priority: P0** — **HMAC-SHA256 on every memory entry** at write time (part of SMSR Component 1). Bind the HMAC to the writer identity, timestamp, and content hash.
- **Priority: P1** — **Merkle-tree-backed operation log** for all memory CRUD events. Root stored in a hardware-backed trust anchor (TPM or cloud HSM).
- **Priority: P1** — **Encryption at rest** for all vector stores, graph DBs, and conversation logs with tenant-specific keys.
- **Priority: P2** — Evaluate **TEE integration** (AMD SEV-SNP or Intel TDX) for the memory extraction and retrieval layers, following the MemTrust five-layer model. Start with a pilot on the retrieval pipeline.
- **Priority: P2** — Implement **forensic state snapshots** (OWASP AMG Layer 4) for point-in-time rollback.

---

## 7. GDPR Article 17 & EU AI Act Compliance

### GDPR Requirements for AI Memory

| Article | Requirement | Memory-Specific Implication |
|---|---|---|
| **Art. 5(1)(e)** | Storage limitation — keep data no longer than necessary | Memory TTL policies; automatic pruning of stale entries |
| **Art. 17** | Right to erasure ("right to be forgotten") | Must delete personal data across **all** memory layers: vector index, source systems, backup snapshots, query caches, agent notes, conversation history |
| **Art. 15** | Right of access | Users must be able to request what the agent remembers about them |
| **Art. 16** | Right to rectification | Users must be able to correct inaccurate memories |
| **Art. 30** | Records of Processing Activities (ROPA) | Document memory pipeline: purposes, categories, retention, third-country transfers |

### The Vector Erasure Problem

Vector databases make Article 17 erasure operationally complex:
- **Copy-on-write / append-only storage:** "Deleted" records may persist in on-disk segments until compaction.
- **Backup snapshots:** S3 backups contain deleted data until they age out.
- **Cached query results:** LLM response caches may hold retrieved chunks referencing the deleted individual.
- **Derived embeddings:** Summaries, agent notes, synthesized profiles that incorporate the user’s data also require deletion.
- **Model weights:** If embeddings are fine-tuned into model weights, selective removal is technically impossible without retraining.

**Implementation pattern (from sota.io, 2026):**
```python
async def handle_erasure_request(subject_id: str) -> ErasureReport:
    layers = [
        vector_store.delete_by_subject(subject_id),
        vector_store.purge_segments(subject_id),
        backup_manager.invalidate_snapshots(subject_id),
        cache_layer.flush_subject(subject_id),
        agent_notes.delete_subject_notes(subject_id),
        conversation_store.delete_subject(subject_id),
    ]
    results = await asyncio.gather(*layers, return_exceptions=True)
    return ErasureReport(...)
```

### EU AI Act (Regulation 2024/1689)

**Enforcement timeline:**
- **August 2, 2026** — Full applicability for high-risk AI systems (employment, credit, education, law enforcement, critical infrastructure).
- **Already in force:** Prohibited practices (social scoring, manipulative AI) since Feb 2025; governance/penalties since Aug 2025.

| Article | Requirement | Penalty for Non-Compliance |
|---|---|---|
| **Art. 9** | Risk management system | Up to €15M or 3% turnover |
| **Art. 10** | Data governance (quality, bias) | Up to €15M or 3% turnover |
| **Art. 11** | Technical documentation | Up to €15M or 3% turnover |
| **Art. 12** | **Automatic record-keeping** — logs of operation, reference database, input data, identity of persons involved | **Up to €15M or 3% turnover** |
| **Art. 13** | Transparency | Up to €15M or 3% turnover |
| **Art. 14** | Human oversight | Up to €15M or 3% turnover |
| **Art. 71** | Prohibited AI practices | **Up to €35M or 7% turnover** |

### Key Insight: GDPR Says Delete, EU AI Act Says Keep

- GDPR Art. 17 mandates erasure of personal data.
- EU AI Act Art. 12 mandates retention of operational logs for at least 6 months (high-risk systems), with some interpretations requiring 10-year audit trails for substantial modifications.
- **Resolution:** Separate **personal data memory** from **audit telemetry**. Audit logs must be pseudonymized and stored in a separate, access-controlled system with longer retention. Memory stores must support complete erasure.

### Recommendation for Mnemosyne

- **Priority: P0** — Implement a **cross-layer erasure protocol** that executes deletion across vector index, graph DB, backups, caches, and conversation stores atomically.
- **Priority: P0** — **Pseudonymize audit logs** — store operational telemetry in a separate namespace with subject identifiers hashed/salted, not in raw form alongside memories.
- **Priority: P0** — Build **user-facing inspect, correct, and delete tooling** before memories accumulate. Retrofitting is exponentially more expensive.
- **Priority: P1** — Document **ROPA** for the memory pipeline (Art. 30) including: lawful basis, data categories, retention schedule, third-country transfers, and DPIA if required.
- **Priority: P1** — Ensure **EU-native or SCC-compliant hosting** for vector databases and embedding APIs to avoid CLOUD Act / data-transfer compliance gaps.
- **Priority: P2** — Prepare **Art. 12 logging infrastructure** (6-month retention, reconstructable decision state) before August 2, 2026.

---

## 8. Audit Trail Requirements & Standards

### Standards Landscape (2026)

| Standard / Framework | Relevance to Memory Systems | Key Requirements |
|---|---|---|
| **ISO/IEC 42001:2023** | The only **certifiable** international AI governance standard | A.6.2.8 (Logging), A.7.5 (Provenance), A.6.2.6 (Performance), A.8.4 (Output), A.5.3 (Risk) |
| **NIST AI RMF 1.0** | Voluntary but increasingly referenced in procurement | GOVERN 1.7 (regular assessments), GOVERN 6.1 (transparent policies), MAP 1.1 (system inventory), MEASURE 2.6 (adversarial robustness) |
| **EU AI Act Art. 12** | Mandatory for high-risk AI | Automatic event logging, period of use, reference database, input data, identity verification, 6-month minimum retention |
| **FedRAMP AU-2 / AU-12** | US federal cloud AI deployments | Define auditable events; generate records with sufficient detail; protect logs from unauthorized access/modification/deletion |
| **SOC 2 CC7.2** | Enterprise SaaS / AI platform trust | Automated monitoring for anomalies; alerting on security events; documented investigation procedures |
| **GDPR Art. 5(2)** | Accountability principle | Demonstrate lawful, fair, transparent processing; purpose limitation; data minimization — all require logs |

### Best Practices for AI Memory Audit Trails

1. **Cryptographic Receipts** — Ed25519-signed, SHA-256 hash-chained decision receipts that auditors can verify offline without system access (GitHub: `sundsoffice-tech/ai-audit-trail`, 2026).
2. **Immutable Append-Only Logs** — Write-once storage (WAL, object storage with object lock) for memory operation records.
3. **Crosswalk Mapping** — Map receipt data directly to ISO 42001 / NIST AI RMF controls with quantitative coverage scores.
4. **Evidence Package Export** — Self-contained signed ZIP bundles for external auditors: receipts + chain metadata + public key + manifest + verify script.
5. **Memory-Specific Events to Log:**
   - Memory write (content hash, writer identity, HMAC signature, timestamp, TTL)
   - Memory retrieval (query hash, retrieved entries, trust scores, retrieval latency)
   - Memory update / deletion (old hash, new hash, operation type, authorization)
   - Anomaly detection flags (trigger, severity, action taken)
   - Erasure request execution (subject ID, layers cleared, errors, timestamp)

### Recommendation for Mnemosyne

- **Priority: P0** — Implement **Ed25519-signed, SHA-256 hash-chained** audit receipts for every memory operation. Design for offline auditor verification from day one.
- **Priority: P0** — Store audit logs in an **append-only, immutable** namespace separate from operational memory data.
- **Priority: P1** — Build **ISO 42001 / NIST AI RMF crosswalk** automation into the audit pipeline.
- **Priority: P1** — Implement **evidence package export** (signed ZIP) for regulatory audits and customer security reviews.
- **Priority: P2** — Map controls to **FedRAMP AU-2** event categories if targeting US federal customers.

---

## 9. Red Teaming for AI Memory Systems

### Benchmarks & Tools (2026)

| Resource | What It Evaluates | Coverage |
|---|---|---|
| **Agent Security Bench (ASB)** | 10 scenarios, 10 agents, 400+ tools, 27 attack/defense combinations | 84.30% average ASR baseline; e-commerce, healthcare, finance |
| **BEAM** | Memory at 1M and 10M token scales | 10 capabilities: facts, entities, updates, contradictions, temporal, multi-hop, summarization, abstention |
| **LoCoMo** | Very long-term multi-session memory | 1,540 questions across 300+ turn conversations; single/multi-hop, open-domain, temporal |
| **LongMemEval** | Chat-assistant memory with knowledge updates | 500 questions; abstention task (correctly decline when event never happened) |
| **MIRROR** | Cross-surface red-teaming for multimodal agentic RAG | Memory-guided MCTS; text poisoning, image injection, direct-query, orchestrator-level tool manipulation |
| **PyRIT** | Microsoft open-source red-teaming automation | 70+ converters; multi-turn attacks (Crescendo, TAP); how practitioners run adversarial evals at scale |
| **JailbreakBench** | Standardized jailbreak evaluation | Baseline for prompt-injection robustness |
| **HarmBench** | CAIS automated red-teaming | Broad adversarial behavior coverage |
| **AgentDojo** | ETH Zurich agent prompt injection benchmark | Tool-using agents |
| **SkillVetBench / SkillSafetyBench** | Community-contributed agent skills | Instruction-layer and multi-agent risks |
| **MCPTox** | Tool poisoning on real-world MCP servers | MCP-specific attack surface |

### Red-Teaming Methodology for Memory Platforms

1. **Static Benchmarking** — Run ASB, BEAM, LoCoMo, LongMemEval against Mnemosyne to establish baseline memory robustness and accuracy.
2. **Adversarial Injection Campaigns** —
   - MINJA-style bridging-step injection via normal queries.
   - InjecMEM-style single-interaction sleeper triggers.
   - Indirect injection via poisoned documents fed to RAG pipeline.
3. **Extraction Campaigns** —
   - ADAM-style entropy-guided adaptive querying.
   - Brute-force knowledge-extraction benchmarks.
4. **Cross-Tenant Contamination Tests** — Verify that User A’s memories cannot be retrieved in User B’s context.
5. **Integrity Tampering Tests** — Modify stored memory blobs, backup snapshots, and log entries; verify detection by HMAC/Merkle checks.
6. **Rollback & Recovery Tests** — Inject poison, detect via anomaly detection, execute forensic rollback to snapshot, verify clean state restoration.
7. **Erasure Verification Tests** — Insert synthetic PII, execute Art. 17 erasure, verify irreversible removal across all layers (including embeddings and derived summaries).
8. **Continuous Campaigns** — Red-teaming should not be a one-time event. The threat landscape evolves (new attack papers every 2–4 months in 2026).

### Recommendation for Mnemosyne

- **Priority: P0** — Establish a **continuous red-teaming program** with quarterly full campaigns and monthly automated regression tests.
- **Priority: P0** — Integrate **ASB, BEAM, and LoCoMo** into CI/CD for memory pipeline changes. Any regression in benchmark scores blocks release.
- **Priority: P1** — Build an **internal ADAM simulator** to continuously test extraction resistance.
- **Priority: P1** — Automate **cross-tenant contamination tests** and **integrity tampering tests** as part of the deployment pipeline.
- **Priority: P2** — Commission **third-party penetration testing** annually by a firm with AI-specific expertise (e.g., using PyRIT or MIRROR frameworks).

---

## 10. Zero-Trust Architecture for AI Memory

### The Trust Crisis in Centralized Memory

AI memory systems centralize sensitive personal data (preferences, health records, financial history, conversation transcripts) to enable cross-agent collaboration. This creates a **trust crisis**: users must entrust cloud providers with plaintext access to their digital memories. The core tension is between **personalization demands** (requiring centralized context) and **data sovereignty** (requiring local control).

### MemTrust: The Leading Zero-Trust Memory Architecture (Jan 2026)

**MemTrust** (arXiv:2601.07004) proposes a **hardware-backed zero-trust architecture** using Trusted Execution Environments (TEEs) to protect the entire AI memory lifecycle.

#### Five-Layer Abstraction

| Layer | Function | TEE Protection |
|---|---|---|
| **L1: Secure Unified Storage** | Vector DB, Graph DB, SQL DB | Sealed segments; encrypted pages; hot segments in TEE RAM, cold segments encrypted offloaded |
| **L2: Extraction & Update** | LLM-based fact extraction, entity recognition, embedding generation | All processing inside TEE; PII sanitization; TEE-native embedding |
| **L3: Learning & Evolution** | Memory consolidation, summarization, profile updating | Secure consolidation workers; encrypted GPU-TEE channels (TDISP/IDE) |
| **L4: Retrieval** | Query processing, access control, result aggregation | Fusion ranking, vector recall, graph traversal all inside TEE; k-anonymity for access patterns |
| **L5: Governance** | Policy engine, attestation, audit, key management | OPA/Wasm policy engine; attestation-bound OIDC tokens; tamper-evident audit log |

#### Core Design Choices

1. **Zero-trust principle:** Cloud infrastructure providers, service operators, and privileged insiders cannot access plaintext context data.
2. **Multi-TEE support:** AMD SEV-SNP (VM-level), Intel SGX (process-level), Intel TDX (VM-level), AWS Nitro Enclaves (cloud-native), ARM CCA (mobile/edge).
3. **Hold-Your-Own-Key (HYOK):** Master keys remain under user control; data encryption keys are hierarchically derived and sealed using hardware keys.
4. **Context from MemTrust protocol:** OAuth-like cross-application context sharing with attestation-bound tokens and fine-grained permissions.
5. **Secure consolidation:** Qwen3 8B and similar models run inside TEE on NVIDIA TEE GPUs with encrypted PCIe channels; batched inference maintains cross-user isolation.

#### Performance

- <20% overhead on enterprise workloads (10K documents, 50K emails, 1M knowledge triples) for SEV-SNP vs. non-TEE baseline.
- Near-linear horizontal scaling.
- ~17K lines Rust + Python implementation.

### Other Zero-Trust Patterns for Memory

| Pattern | Mechanism | Use Case |
|---|---|---|
| **Per-User Memory Isolation** | `user_id` scoped namespaces at storage level | Prevent cross-tenant contamination; foundational for multi-tenant SaaS |
| **Role-Based Access Control (RBAC)** | Read/write/delete permissions scoped to agent/user/app/org combinations | Multi-agent fleets with shared organizational memory |
| **Cryptographic Attestation** | Remote attestation of TEE + code measurement before releasing decryption keys | Verify that only authorized, unmodified code processes memories |
| **Memory Segmentation** | Hot/warm/cold tiering with different encryption and access policies | Cost optimization + security: sensitive recent data in highest-protection tier |
| **K-Anonymity / Oblivious RAM** | Obfuscate access patterns to prevent hypervisor-level inference of which user queried what | Side-channel hardened retrieval |

### Recommendation for Mnemosyne

- **Priority: P0** — Implement **strict per-user memory isolation** at the storage layer (not just retrieval filtering). This is the foundational zero-trust control.
- **Priority: P0** — Enforce **RBAC on all memory operations** — who can read, write, update, delete which memory scopes. Fail closed (deny by default).
- **Priority: P1** — Design architecture for **TEE migration** (AMD SEV-SNP or Intel TDX) on the extraction and retrieval layers. Begin with a threat-model and feasibility study.
- **Priority: P1** — Implement **cryptographic attestation** for the memory service itself — clients verify the memory service's integrity before sending sensitive context.
- **Priority: P2** — Evaluate **HYOK (Hold-Your-Own-Key)** models for enterprise customers who require full data sovereignty.
- **Priority: P2** — Research **oblivious RAM / k-anonymity** for retrieval access-pattern hiding if deploying in untrusted cloud environments.

---

## 11. Security Roadmap & Phased Recommendations

### Phase 1: Foundation (0–3 months) — Hackathon / MVP

| Control | Priority | Effort | Rationale |
|---|---|---|---|
| **Per-user memory isolation** | P0 | Low | Prevents cross-tenant contamination; required for any multi-user deployment. |
| **RBAC on memory operations** | P0 | Low | Fail-closed access control; deny-by-default. |
| **HMAC-SHA256 provenance (SMSR C1)** | P0 | Medium | Blocks 100% of unsigned injection variants; the single most effective defense available. |
| **Input validation + composite trust scoring** | P0 | Medium | Catches obvious injection payloads before they reach the memory store. |
| **Append-only audit log with SHA-256 chaining** | P0 | Low | Satisfies EU AI Act Art. 12 baseline and GDPR accountability. |
| **Query-rate limiting + pattern detection** | P0 | Low | Defends against ADAM-style extraction; structurally simple. |
| **Source authentication for RAG documents** | P0 | Medium | Prevents PoisonedRAG/AgentPoison at the ingestion gate. |
| **User-facing inspect/delete tooling** | P0 | Medium | GDPR Art. 17 compliance; must exist before data accumulates. |

### Phase 2: Hardening (3–6 months) — Production Readiness

| Control | Priority | Effort | Rationale |
|---|---|---|---|
| **Randomized memory ablation + verdict voting (SMSR C2)** | P0 | High | First certified defense; reduces authenticated-adversary ASR to ~5–8%. |
| **Retrieval-layer injection detector** | P1 | Medium | Defense-in-depth between vector DB and context assembly. |
| **Temporal decay + TTL policies** | P1 | Low | Limits poison persistence window; satisfies GDPR storage limitation. |
| **Merkle-tree-backed operation log** | P1 | Medium | Tamper-evident memory governance; enables forensic rollback. |
| **Embedding-space anomaly detection** | P1 | Medium | Catches poisoning at ingestion time via cluster drift. |
| **Cross-layer erasure protocol** | P1 | Medium | GDPR Art. 17 operational compliance across vector, graph, cache, backup, conversation layers. |
| **Ed25519-signed audit receipts** | P1 | Medium | Cryptographically verifiable evidence for auditors and customers. |
| **Automated red-teaming in CI/CD** (ASB, LoCoMo, BEAM) | P1 | Medium | Prevents regression; catches issues before production. |
| **Forensic state snapshots** | P1 | Medium | Rollback to known-good state upon anomaly detection. |
| **Anomaly detection on write patterns** | P1 | Medium | Flags unusual memory growth, protected-key modification, rapid state changes. |

### Phase 3: Enterprise & Certification (6–12 months) — Scale

| Control | Priority | Effort | Rationale |
|---|---|---|---|
| **TEE integration pilot** (AMD SEV-SNP / Intel TDX) | P2 | High | Zero-trust memory lifecycle; <20% overhead proven feasible. |
| **ISO 42001 / NIST AI RMF crosswalk automation** | P2 | Medium | Certifiable governance; procurement requirement for enterprise customers. |
| **Differential privacy on retrieval outputs** | P2 | High | Defense against ADAM and other extraction attacks in high-sensitivity domains. |
| **Oblivious RAM / k-anonymity for retrieval** | P2 | High | Side-channel protection in untrusted cloud environments. |
| **Hold-Your-Own-Key (HYOK) for enterprise tenants** | P2 | High | Full data sovereignty for regulated customers. |
| **Evidence package export (signed ZIP)** | P2 | Low | Customer audit readiness; competitive differentiation. |
| **Third-party penetration testing** | P2 | Medium | Annual independent validation. |
| **Post-quantum cryptography (PQC) readiness** | P3 | High | NIST mandates PQC-ready algorithms by Q4 2027 for new systems. |

### Deferrable to Later Phases (>12 months)

| Control | Rationale |
|---|---|
| **GPU-TEE integration for inference** | Only needed if running LLM inference inside the memory pipeline (extraction/consolidation). If using external LLM APIs, not required. |
| **Context markets / data sovereignty guarantees** | Advanced commercial model; depends on customer demand. |
| **Formal verification of security protocols** | Research-grade; valuable but not blocking for production. |
| **Multi-modal memory poisoning defenses** (image, audio) | Only relevant if memory system ingests non-text media. |

---

## Risk Priority Matrix

| Threat | Current Risk | Defense Maturity | Recommended Action |
|---|---|---|---|
| **MINJA (memory injection)** | Critical | SMSR (June 2026) provides certified defense | **Implement SMSR C1+C2 immediately.** |
| **ADAM (memory extraction)** | Critical | Rate-limiting + entropy detection available | Implement query anomaly detection + rate limiting now. Evaluate differential privacy later. |
| **Vector DB poisoning** | High | Source auth + embedding audits proven | Implement source auth + anomaly detection at ingestion. |
| **Memory tampering (at rest)** | High | HMAC + Merkle trees mature | HMAC every entry now; Merkle-tree logs in Phase 2. |
| **Cross-tenant leakage** | High | Per-user isolation standard practice | Enforce storage-level isolation immediately. |
| **GDPR Art. 17 non-compliance** | High | Cross-layer erasure protocols exist but are custom-built | Build erasure protocol before first EU user. |
| **EU AI Act Art. 12 non-compliance** | High | Append-only logs + signed receipts solve this | Implement tamper-evident audit log now. |
| **Insider threat / cloud provider** | Medium | TEE architectures emerging (MemTrust) | Pilot TEE in Phase 3; not blocking for MVP. |
| **Post-quantum compromise** | Low | NIST PQC standards published (FIPS 203/204/205) | Plan migration by 2027; not urgent today. |

---

## Key Sources & References

1. **MINJA / Memory Poisoning Defense** — arXiv:2601.05504 (Devarangadi Sunil et al., Jan 2026); arXiv:2503.03704 (Dong et al., 2025).
2. **ADAM** — arXiv:2604.09747 (Xingyu Lyu et al., Apr 2026).
3. **SMSR (Certified Defense)** — arXiv:2606.12703 (Tarun Kumar Sharma, Jun 2026).
4. **OWASP Agent Memory Guard / ASI06** — OWASP Top 10 for Agentic Applications 2026 (Dec 2025); `genai.owasp.org`.
5. **PoisonedRAG** — Zou et al., USENIX Security 2025; arXiv:2402.07867.
6. **AgentPoison** — Chen et al., NeurIPS 2024; arXiv:2407.12784.
7. **MemTrust (Zero-Trust TEE Architecture)** — arXiv:2601.07004 (Jan 2026).
8. **Eywa (Provenance-Grounded Memory)** — arXiv:2605.30771 (May 2026).
9. **BEAM Benchmark** — ICLR 2026; Tavakoli et al.
10. **ASB (Agent Security Bench)** — Zhang et al., ICLR 2025; arXiv:2410.02644.
11. **EU AI Act** — Regulation (EU) 2024/1689; full high-risk applicability Aug 2, 2026.
12. **GDPR** — Regulation (EU) 2016/679; Art. 17 right to erasure.
13. **ISO/IEC 42001:2023** — AI management system standard.
14. **NIST AI RMF 1.0** — January 2023.
15. **AI Audit Trail (Ed25519 + SHA-256)** — `github.com/sundsoffice-tech/ai-audit-trail` (May 2026).
16. **Mem0 / OpenMemory** — Memory isolation and security best practices (Feb 2026).
17. **A-MemGuard** — Defense framework released Oct 2025.
18. **AgeMem (RL-driven memory CRUD)** — arXiv:2601.01885 (Jan 2026).
19. **MIRROR (Red-teaming)** — Singh et al., 2026.
20. **PyRIT** — Microsoft AI Red Team; `github.com/Azure/PyRIT`.

---

*Document compiled by Kimi Work research sub-agent on 2026-07-06. All findings are sourced from published research, industry disclosures, and regulatory texts as of July 2026. Recommendations reflect current best available evidence and should be reviewed quarterly as the threat landscape evolves.*

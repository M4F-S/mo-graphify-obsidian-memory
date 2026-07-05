# Deep Research: Cognee `improve()` / `memify()` for The Hangover Part AI Hackathon

**Research date:** June 30, 2026, 23:34 CEST  
**Hackathon:** The Hangover Part AI: Where's My Context? (WeMakeDevs + Cognee)  
**Dates:** June 29 – July 5, 2026  
**Prize pool:** $10,000 + MacBook Neo / iPhone 17 per team member + job interviews  
**Branch context:** `cognee-hackathon` on `M4F-S/unified-memory`

---

## 1. What `improve()` and `memify()` Actually Do

### 1.1 The Big Picture

Cognee's core memory API is four verbs: `remember`, `recall`, `improve`, `forget`.

- **`improve()`** is the **user-facing** API for self-improvement. It enriches an existing graph after data has already been ingested.
- **`memify()`** is the **underlying engine** that `improve()` calls for its enrichment stage. Memify runs ordered `extraction_tasks` + `enrichment_tasks` pipelines on an existing knowledge graph.

> Key insight: `remember(..., self_improvement=True)` already calls `improve()` for you after permanent ingestion. But calling `improve()` explicitly gives you control over session bridging, feedback weights, and custom enrichment.

### 1.2 The 5 Stages of `improve()` (when `session_ids` provided)

Source: `cognee/api/v1/improve/improve.py:36-232` (per akitaonrails research)

| Stage | What it does | Key files |
|-------|-------------|-----------|
| **1. Apply feedback weights** | Session thumbs-up/down ratings adjust `feedback_weight` on the **specific graph nodes/edges** that were used to answer. Tracked via `used_graph_element_ids` recorded at retrieval time. Higher-rated answers boost their source nodes; lower-rated ones decrease them. | `apply_feedback_weights_pipeline` (L284-299) |
| **2. Persist session Q&A** | Cognifies session transcripts into the permanent graph, tagged under `node_set="user_sessions_from_cache"`. | `persist_sessions_in_knowledge_graph_pipeline` |
| **3. Triplet enrichment / memify** | Builds and embeds new triplet datapoints (`source -> relationship -> target`). | `cognee/memify_pipelines/create_triplet_embeddings.py` |
| **4. Global context index** | Builds semantic bucket summaries + a root dataset summary over all `TextSummary` nodes. | `global_context_index_pipeline` |
| **5. Sync graph → session** | Copies recently-added graph edges back into session caches as JSON-lines so live agents pick up new knowledge without re-query. | `_sync_graph_to_sessions` |

Without `session_ids`, `improve()` skips stages 1-2 and only runs enrichment + optional global context index.

### 1.3 Memify Pipeline Architecture

Every memify pipeline is two stages:

1. **Extraction** — selects/prepares data from the existing graph (e.g., pull document chunks, load graph triplets, read cached sessions)
2. **Enrichment** — processes extracted data and writes new/updated nodes and edges back

Built-in memify pipelines:

| Pipeline | Extraction | Enrichment | Output |
|----------|-----------|------------|--------|
| **Default enrichment** | `get_triplet_datapoints` (when enabled) | `index_data_points` | Indexed triplet datapoints for triplet retrieval |
| **Triplet embeddings** | `get_triplet_datapoints` | `index_data_points` | `Triplet_text` vector collection; enables `SearchType.TRIPLET_COMPLETION` |
| **Session persistence** | `extract_user_sessions` | `cognify_session` (add + cognify) | New graph nodes from session content, tagged `user_sessions_from_cache` |
| **Entity consolidation** | `get_entities_with_neighborhood` | `generate_consolidated_entities` → `add_data_points` | Updated `Entity` descriptions rewritten by LLM |
| **Coding rules** | `extract_subgraph_chunks` | `add_rule_associations` | `Rule` nodes under `coding_agent_rules` node set |

### 1.4 `improve()` Parameters

**Basic:**
- `dataset` (str, default `"main_dataset"`) — target dataset
- `session_ids` (List[str]) — sessions to bridge into permanent graph
- `run_in_background` (bool) — async execution
- `build_global_context_index` (bool) — builds bucket+root summaries
- `node_name` (List[str]) — restricts to specific nodes
- `feedback_alpha` (float) — controls feedback weight strength

**Advanced:**
- `extraction_tasks` / `enrichment_tasks` — override default task set for domain-specific behavior
- `data` — explicit data for advanced pipelines
- `node_type` — target specific node types
- `user` — user context for access control
- `vector_db_config` / `graph_db_config` — override backend config

### 1.5 What `improve()` Produces

- Enriched graph structures on the target dataset
- Triplet-embedding retrieval artifacts (when enabled)
- Optional `GlobalContextSummary` bucket + root summaries
- Optional persistence of session Q&A into permanent graph
- Optional feedback-based weighting updates on graph elements
- Optional sync of enriched graph context back into session cache

---

## 2. Comparison: Cognee vs Mem0 vs Zep vs Letta

This is Cognee's **#1 differentiator** — the only framework with built-in self-improvement.

| Dimension | Cognee | Mem0 | Zep | Letta |
|-----------|--------|------|-----|-------|
| **Storage** | Graph + Vector + Relational (hybrid) | Vector + Graph + KV | Temporal knowledge graph (Graphiti) | In-context + archival vector |
| **Self-improvement** | ✅ **YES** — `improve()` / `memify()` pipelines | ❌ No | ❌ No | ❌ No |
| **Feedback loop** | ✅ Graph element weights updated from session feedback | ❌ No | ❌ No | ❌ No |
| **Session bridging** | ✅ Short-term → long-term automatically | Partial | Partial | Manual agent-managed |
| **Temporal accuracy** | Structural (not time-windowed) | 49.0% LongMemEval | **63.8%** LongMemEval (best) | Variable |
| **Entity consolidation** | ✅ `consolidate_entity_descriptions` | ❌ No | ❌ No | ❌ No |
| **Retrieval modes** | 16 search types | Moderate | Graph + vector | Limited |
| **License** | Apache 2.0 | Apache 2.0 | Apache 2.0 (engine only) | Apache 2.0 |
| **Best for** | Typed knowledge graphs, custom ontologies | Fast setup, personalization | Temporal facts that change | Long-running stateful agents |

**Source:** Multiple 2026 comparison reviews (evermind.ai, particula.tech, mcp.directory, tryxlr8.ai)

**The key competitive claim:** Cognee is the only framework combining full hybrid store, 14+ retrieval modes, automated ECL pipeline, **and** a self-improving memify abstraction under a single open-source package. All others have tradeoffs that matter at production scale.

---

## 3. The Cognee-Daytona-MOSS Hackathon (April 2026) — What Won

**Repo:** `topoteretes/cognee-daytona-moss-hackathon`  
**Theme:** PR Rescue Arena — Build a self-improving agent skill that rescues broken pull requests  
**Date:** April 25, 2026, San Francisco

### 3.1 Winning Criteria ("Best Self-Improvement Loop")

Judges wanted **evidence**, not claims:

1. Baseline score before improvement
2. `SkillRunEntry` feedback stored in Cognee
3. Meaningful `SKILL.md` diff
4. Improved second run
5. Clear explanation of what changed and why

### 3.2 The Required Loop

```
starter skill
→ agent run on PR #1
→ score and feedback recorded in Cognee (SkillRunEntry)
→ skill improves (SKILL.md amended)
→ agent run on PR #2
→ better result
```

**Tagline:** "Do not just fix the PR. Teach the agent to fix the next one."

### 3.3 Awards Given

- **Best PR Rescue Skill** — correct bug identification, concrete file references, small practical fix, useful test plan, reusable skill design
- **Best Self-Improvement Loop** — the evidence-based before/after
- **Best Agent Team** — multi-agent workflow (scout, fixer, critic, editor, verifier)

### 3.4 Lessons for This Hackathon

The winning formula was **measurability + auditability**:
- Don't say "the agent learned" — show before score, feedback, skill diff, and after score
- Make improvement easy to inspect
- Use `SkillRunEntry` with `success_score`, `feedback`, `error_type`, `error_message`

---

## 4. The Hangover Part AI Hackathon — Judging Criteria & Opportunities

**Source:** https://www.wemakedevs.org/hackathons/cognee  
**Dates:** June 29 – July 5, 2026  
**Prizes:**
- Best Use of Open Source Track: Apple MacBook Neo per team member
- Best Use of Cognee Cloud Track: Apple iPhone 17 per team member
- Open Source GitHub Contribution Track: **$100 per accepted PR** (top 20, max 5 per person)
- Best blogs: Keychron mechanical keyboard ($120)
- Top 10 social posts: exclusive swag

### 4.1 Judging Criteria (6 dimensions)

1. **Potential Impact** — does it solve a meaningful problem with persistent AI memory?
2. **Creativity & Innovation** — does it push boundaries of "agent never forgets"?
3. **Technical Excellence** — strong engineering, clean maintainable code
4. **Best Use of Cognee** — how deeply does it leverage the memory lifecycle APIs?
5. **User Experience** — intuitive, polished, adoptable
6. **Presentation Quality** — clear demo, README, submission

### 4.2 What Cognee Wants to See

The official marketing literally describes the core lifecycle:

```python
import cognee

# 1. Give your agent a memory
await cognee.remember("Doug is the groom. The wedding is Sunday.")
await cognee.remember(file="vegas_receipts.pdf")

# 2. Ask it anything, across infinite sessions
answer = await cognee.recall("Where is Doug?")

# 3. Let the memory get smarter over time
await cognee.improve()   # a.k.a. memify

# 4. Surgically forget what no longer matters
await cognee.forget(dataset="last_nights_mistakes")
```

**Key theme:** "Your AI woke up in Vegas with no memory of last night. Build AI that doesn't forget."

---

## 5. Current Limitations & Open Issues (Hackathon Opportunities)

### 5.1 Confirmed Bugs (Good PR candidates — $100 each)

| Issue | Description | Status |
|-------|-------------|--------|
| **#3313** | `improve()` leaks session lock when memify/sync stages fail. Lock acquired at stage 1, but stages 3-5 have no exception handling → permanent lock starvation until server restart. | **Open** — community member said "I will be working on this issue" |
| **#2809** | CLI `--api-url` mode doesn't support `remember`/`recall`/`improve`/`forget`. Only legacy `add`/`cognify`/`search`/`memify`/`datasets`/`delete` are dispatched. Breaks multi-process Backend mode. | **Open** — fix: add 4 dispatchers to `cognee/cli/api_dispatch.py` |

### 5.2 Feature Gaps (Major hackathon opportunities)

#### A. No Progress Callback / Visualization for `improve()`

**Finding:** There is NO explicit progress callback, progress bar, or real-time visualization for the `improve()` pipeline. 

- `cognify()` has status tracking via `cognee.datasets.get_status()` and `cognify_status` MCP tool
- `improve()` runs a 5-stage pipeline that can take significant time (LLM calls for triplet enrichment, entity consolidation, global context indexing) but provides **no visibility** into which stage is running
- The only "progress" is: start → finish (or silent failure with leaked lock, per #3313)
- v1.2.0 (June 21, 2026) added "indexing status indicator" in the UI and "distilled nodes marked in visualization" — but this is for `cognify`, not `improve`

**This is a HIGH-VALUE hackathon PR.** Adding a progress callback or status endpoint for `improve()` would:
- Fix a genuine UX pain point
- Make the self-improvement loop visible and debuggable
- Be a compelling demo component ("Watch your memory reorganize itself in real-time")
- Fit the $100 PR track perfectly

#### B. Memory-Maintenance Repertoire is Thin (Umbrella #3389)

**Source:** https://github.com/topoteretes/cognee/issues/3389 (opened June 24, 2026 — explicitly tagged `[hackathon]`)

Cognee's memify today only has 5 real transformations:
1. Embed triplets
2. Apply feedback weights
3. Persist/distill sessions
4. Consolidate entity descriptions
5. Build global context index

The maintainers opened an **umbrella hackathon issue** tracking 5 biologically-inspired memory tasks:

| Issue | Task | Description |
|-------|------|-------------|
| **#3390** | **FORGET / decay** | Time- and usage-based weight decay + prune of stale/low-weight nodes |
| **#3391** | **RE-WEIGHT / reinforce** | Make `frequency_weight` functional; boost frequently-recalled / positively-fed-back memory, demote the rest. Currently `frequency_weight` stubs raise `NotImplementedError` in adapters. |
| **#3392** | **CROSS-CONNECT / link prediction** | Infer and add edges between related-but-unlinked entities |
| **#3393** | **CONSOLIDATE / merge** | Semantically dedupe near-duplicate entities/summaries (not just rewrite descriptions) |
| **#3394** | **RECONCILE / supersede** | Detect contradictions, add `supersedes` edges, demote stale claims |

**Template guidance:** Follow `memify_pipelines/consolidate_entity_descriptions.py` (cleanest whole-graph template) or `memify_pipelines/apply_feedback_weights.py` (weighting template). Register in `memify_pipelines/memify_default_tasks.py` and document in `modules/visualization/operations_catalog.py`.

#### C. No Automatic Decay / TTL

There's no automatic decay/TTL mechanism. `feedback_weight` and `frequency_weight` exist as levers but frequency is not yet implemented end-to-end. A hackathon project implementing **biological memory decay** (e.g., Ebbinghaus forgetting curve) would be highly novel.

#### D. Feedback Influence Defaults to 0

`feedback_influence` defaults to 0.0, meaning feedback weights are computed but **ignored in ranking** unless explicitly requested. A hackathon fix to turn on a small default would make the feedback loop actually functional out of the box.

---

## 6. What Would Be the MOST COMPELLING Demo?

### 6.1 The Winning Demo Formula (from Daytona-MOSS)

The most compelling `improve()` / `memify()` demo must show:

**BEFORE → FEEDBACK → IMPROVEMENT → AFTER**

With **quantified evidence** at each step.

### 6.2 Recommended Demo Architecture

**Title:** "Mnemosyne: Memory That Forgets to Remember Better"

**The narrative:**
1. **Ingest a messy corpus** (e.g., 20 documents about a fictional Vegas trip with contradictions, duplicates, and irrelevance)
2. **Show the initial graph** — noisy, redundant, disconnected
3. **Run a simulated agent session** with recall queries
4. **Capture feedback** (thumbs up/down on answers, with `used_graph_element_ids` traced)
5. **Call `improve()` with `session_ids` and `build_global_context_index=True`**
6. **Show the improved graph** — deduplicated entities, consolidated descriptions, cross-connected relationships, feedback-boosted important nodes, decayed irrelevant nodes
7. **Re-run the same queries** — show measurably better answers
8. **Visualize the improvement delta** — nodes added, edges added, weights changed, contradictions resolved

### 6.3 Specific Before/After Metrics to Show

| Metric | Before | After | How to measure |
|--------|--------|-------|---------------|
| **Query accuracy** | Score on test questions | Higher score after improve | Custom eval script |
| **Entity count** | N redundant entities | N - M consolidated entities | Graph query |
| **Edge density** | Sparse connections | Richer cross-connections | Graph analytics |
| **Average feedback weight** | Uniform / ignored | High-value nodes boosted | `feedback_weight` field |
| **Session bridging** | Session-only facts lost | Session facts in permanent graph | `recall()` with/without session_id |
| **Global context coverage** | No dataset summaries | Bucket + root summaries | `GlobalContextSummary` nodes |
| **Contradictions resolved** | Conflicting facts coexist | `supersedes` edges added | Custom task (if implemented) |

### 6.4 The "Self-Improvement Loop" Visualization

A real-time or step-by-step visualization of `improve()` running its 5 stages would be incredibly impressive:

```
Stage 1/5: Applying feedback weights... ████████░░ 78% (147 nodes boosted, 23 demoted)
Stage 2/5: Bridging session memory...    ██████████ 100% (3 sessions → 42 new facts)
Stage 3/5: Enriching triplets...         ██████░░░░ 54% (1,234 triplets indexed)
Stage 4/5: Building global context...    ███░░░░░░░ 30% (7 semantic buckets)
Stage 5/5: Syncing to sessions...        ██████████ 100% (89 edges synced)

✅ Memory improved. 42 new facts integrated. 3 contradictions resolved.
```

This is **not currently in Cognee** and would be a genuine, valuable contribution.

---

## 7. The Most Valuable Hackathon PR: `improve()` Progress Callback

### 7.1 Why This PR is Perfect

1. **Addresses a real gap** — no progress visibility for a 5-stage LLM-heavy pipeline
2. **Demo-friendly** — makes the self-improvement loop tangible and visual
3. **Fits the $100 PR track** — fixing a verified, user-facing issue
4. **Technically scoped** — doesn't require redesigning core architecture
5. **Universal benefit** — every Cognee user running `improve()` would benefit

### 7.2 Implementation Approach

The `improve()` function in `cognee/api/v1/improve/improve.py` currently runs stages sequentially with no instrumentation. A clean implementation would:

1. Add an optional `progress_callback` parameter (callable receiving stage name, progress fraction, metadata dict)
2. Instrument each of the 5 stages with granular updates
3. Add a `GET /api/v1/improve/status/{pipeline_run_id}` endpoint for async (`run_in_background=True`) tracking
4. Surface the progress in the MCP `cognify_status`-style tool
5. Include a CLI progress bar using `tqdm` or `rich`

**Key files to modify:**
- `cognee/api/v1/improve/improve.py` (main logic)
- `cognee/api/v1/improve/improve.py` stages 1-5 instrumentation
- `cognee/api/v1/client.py` or FastAPI router (status endpoint)
- `cognee/cli/api_dispatch.py` (if CLI integration desired)
- `cognee-mcp/src/server.py` (status tool)

---

## 8. Key Source Code References

| File | Lines | What it does |
|------|-------|-------------|
| `cognee/api/v1/improve/improve.py` | 36-411 | Main improve() logic, 5 stages |
| `cognee/memify_pipelines/` | — | All enrichment pipelines |
| `cognee/memify_pipelines/create_triplet_embeddings.py` | — | Triplet indexing |
| `cognee/memify_pipelines/consolidate_entity_descriptions.py` | — | Entity description LLM rewrite |
| `cognee/memify_pipelines/apply_feedback_weights.py` | — | Feedback weight application template |
| `cognee/tasks/storage/add_data_points.py` | 62-149, 184-265 | Triple-store write path + triplet embeddings |
| `cognee/modules/retrieval/utils/brute_force_triplet_search.py` | 216-355 | Multi-collection vector search + triplet scoring |
| `cognee/modules/retrieval/graph_completion_retriever.py` | — | Flagship graph+vector retriever |
| `cognee/api/v1/recall/recall.py` | 314-513 | Recall + auto-router |
| `cognee/api/v1/recall/query_router.py` | — | SearchType classifier |
| `cognee/infrastructure/databases/graph/get_graph_engine.py` | 241-457 | Graph backend factory |
| `cognee/infrastructure/databases/unified/unified_store_engine.py` | 11-66 | Triple-store facade |

---

## 9. Recommended Hackathon Strategy

### Option A: "The Memory Evolution Dashboard" (Best Demo)

Build a web dashboard that:
1. Ingests a corpus and shows the initial graph
2. Runs an agent with session memory
3. Captures user feedback on answers
4. Triggers `improve()` with **real-time progress streaming**
5. Visualizes the before/after graph diff (nodes added, edges added, weights changed)
6. Re-runs queries to show improved answers
7. **Quantifies improvement** with a score

**Why it wins:** Directly hits "Best Use of Cognee", "Creativity & Innovation", "Presentation Quality", and "Potential Impact".

### Option B: "Biological Memory Maintenance" (Best Technical)

Implement one or more of the hackathon-tagged memory tasks from #3389:
- #3390: FORGET / decay — time-based weight decay with visualization
- #3391: RE-WEIGHT / reinforce — finish the `frequency_weight` implementation (currently `NotImplementedError`)
- #3392: CROSS-CONNECT — link prediction between related entities
- #3393: CONSOLIDATE — semantic deduplication with merge operations
- #3394: RECONCILE — contradiction detection with `supersedes` edges

**Why it wins:** Hits "Technical Excellence", "Best Use of Cognee", and qualifies for the $100 PR track.

### Option C: "The Fix-It-And-Track-It PR" (Safest PR track)

Fix one of the open issues:
- **#3313:** Add `try/finally` around stages 3-5 in `improve()` to prevent lock leaks
- **#2809:** Add CLI dispatchers for `remember`/`recall`/`improve`/`forget` in `--api-url` mode
- **#3391:** Finish `frequency_weight` adapter methods (Ladybug + Neo4j)

**Why it wins:** Guaranteed $100 if accepted, builds credibility, and leaves time for the main demo.

### Option D: "Amendify for Skills" (Most Ambitious)

Build on the Cognee blog's vision (March 2026) of skills that evolve:
1. Store agent skills in Cognee as DataPoints
2. Record every skill execution as a `SkillRunEntry` with feedback
3. Use `improve()` to analyze failure patterns
4. Propose `SKILL.md` amendments via LLM
5. Evaluate amendments before applying

This is the exact pattern that won the Daytona-MOSS hackathon.

---

## 10. Summary of Key Findings

| # | Finding | Implication |
|---|---------|-------------|
| 1 | `improve()` runs 5 stages: feedback weights → session persistence → memify enrichment → global context index → session sync | The pipeline is rich but opaque — no progress visibility |
| 2 | `memify()` is the engine with extraction + enrichment tasks; fully customizable | You can build domain-specific memory maintenance |
| 3 | **Cognee is the ONLY open-source memory framework with built-in self-improvement** Mem0, Zep, Letta have none | This is the core competitive advantage to highlight |
| 4 | The April 2026 Daytona-MOSS hackathon was won by **measurable before/after improvement loops** with `SkillRunEntry` + `SKILL.md` diffs | Judges need evidence, not claims |
| 5 | **There is NO progress callback or visualization for `improve()`** | A high-value, demo-friendly PR opportunity |
| 6 | **5 hackathon-tagged memory transformation issues** were opened June 24, 2026 (#3390-3394) | The maintainers are actively inviting these contributions |
| 7 | `frequency_weight` adapters raise `NotImplementedError` | Another ready-to-implement PR |
| 8 | `feedback_influence` defaults to 0.0, so feedback weights are ignored unless explicitly requested | A one-line fix with big UX impact |
| 9 | `improve()` has a known lock leak bug (#3313) when stages 3-5 fail | A straightforward, high-impact bug fix |
| 10 | The Hangover Part AI judging criteria weight "Best Use of Cognee" heavily | Deep integration with `improve()` / `memify()` is the winning strategy |

---

## 11. Actionable Next Steps

1. **File a claim on Issue #3389** (umbrella) or one of its children (#3390-3394) to reserve the work
2. **Comment on Issue #3313** or #2809 to claim the $100 PR track fix
3. **Design the demo around a visible `improve()` delta** — graph before/after, query scores, weight heatmaps
4. **Add a progress callback** as a standalone PR or as part of the demo — this is the most visible gap
5. **Use session bridging as the demo narrative** — "session memory becomes permanent memory" is the most intuitive self-improvement story
6. **Quantify everything** — the Daytona-MOSS winners showed scores, diffs, and logs

---

*Research compiled from: Cognee official docs, GitHub issues (topoteretes/cognee #2809, #3313, #3389-3394), Cognee blog (March 2026), Daytona-MOSS hackathon repo, WeMakeDevs hackathon page, and multiple 2026 comparison reviews (evermind.ai, particula.tech, mcp.directory, tryxlr8.ai, akitaonrails research).*

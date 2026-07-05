# Cognee Integrations Research Report
## The Hangover Part AI Hackathon — June 30, 2026

---

## Executive Summary / Recommendation

**For this hackathon, the integration ranking is:**

| Rank | Integration | Demo-ability | Impressiveness | Differentiation | Risk |
|------|-------------|--------------|----------------|-----------------|------|
| 1 | **OpenClaw** | 6/10 | 9/10 | 9/10 | Medium |
| 2 | **n8n** | 9/10 | 7/10 | 5/10 | Low |
| 3 | **Codex** | 4/10 | 6/10 | 3/10 | Low |
| 4 | **Claude Code** | 4/10 | 6/10 | 2/10 | Low |

**Top Recommendation: OpenClaw** — if you can execute the multi-scope memory architecture in the 7-day window. It is the only integration that offers company/user/agent scope hierarchy, auto-indexing, and self-extending agent capabilities. It will be the least attempted by other teams (most will flock to Claude Code or n8n).

**Runner-up: n8n** — if you want the safest path to a polished, visual demo that scores highly on "Presentation Quality" and "User Experience." n8n workflows are inherently cinematic.

---

## 1. Cognee + Claude Code Integration

### What It Does
- **Official plugin**: `cognee-memory@cognee` available via the Claude Code marketplace
- **Hook-based architecture** that captures the full Claude Code lifecycle:
  - `SessionStart` — mode select, identity setup, dataset readiness
  - `UserPromptSubmit` — injects dataset-scoped relevant context from Cognee memory
  - `PostToolUse` — captures tool traces asynchronously
  - `Stop` — writes assistant answer to memory
  - `PreCompact` — preserves memory anchors before context compaction
  - `SessionEnd` — triggers final sync into the permanent knowledge graph
- **Two memory tiers**: Session cache (fast, per-session) + Permanent knowledge graph (durable)
- **Auto-minted API keys** in local mode — no manual auth setup needed
- **Shared dataset** with Codex plugin — both use `agent_sessions` by default

### How to Set Up
```bash
claude plugin marketplace add topoteretes/cognee-integrations
claude plugin install cognee-memory@cognee
export LLM_API_KEY="sk-..."
claude
```
Local mode bootstraps Cognee API on `http://localhost:8011`. Cloud mode requires `COGNEE_BASE_URL` + `COGNEE_API_KEY`.

### Limitations
- **Cannot disable Claude Code's native auto-memory** — the plugin "steers" the model toward Cognee but cannot intercept `MEMORY.md` injection. Set `COGNEE_PREFER_MEMORY=false` to turn off the steer.
- **Background writes are not immediately queryable** — `COGNEE_REMEMBER_BACKGROUND=true` (default) enqueues writes; a recall in the same breath may not see the new entry.
- **Dataset is fixed per launch** — to change dataset, you must exit Claude, change env, and restart.
- **Synchronous cognify can timeout** — tens of seconds, which can be misread as "server unreachable."
- **Single auth principal** — one API key, one user. No multi-user support out of the box.

### What Already Exists
- The plugin is **official, mature, and well-documented** by Cognee itself (v1.0.1+ docs)
- Akita On Rails built an independent `ai-memory` system inspired by this integration (May 2026)
- Multiple blog posts and tutorials exist; it is the most marketed Cognee integration
- **Risk**: This will be the #1 choice for hackathon participants. It will be very hard to differentiate.

---

## 2. Cognee + n8n Integration

### What It Does
- **Official community node**: `n8n-nodes-cognee` (npm install, current version **0.4.0**)
- **Four operations** available directly on the n8n canvas:
  1. **Add Data** — write text into a named Cognee dataset
  2. **Cognify** — turn that dataset into a knowledge graph with embeddings, chunks, and summaries
  3. **Search** — query with natural language using 14 search types (GRAPH_COMPLETION, CHUNKS, COT, TEMPORAL, etc.)
  4. **Delete** — remove datasets or individual data items
- **Visual, no-code memory pipelines** — wire nodes together on a canvas
- **Composes with 400+ n8n integrations** — Slack, email, CRM, forms, Jira, etc.
- **Self-hosted ready** — works on local n8n instances
- **Search types supported**: `GRAPH_COMPLETION`, `GRAPH_COMPLETION_COT`, `GRAPH_COMPLETION_CONTEXT_EXTENSION`, `GRAPH_SUMMARY_COMPLETION`, `RAG_COMPLETION`, `TRIPLET_COMPLETION`, `CHUNKS`, `CHUNKS_LEXICAL`, `SUMMARIES`, `TEMPORAL`, `NATURAL_LANGUAGE`, `FEELING_LUCKY`

### How to Set Up
```bash
# In n8n: Settings → Community Nodes → Install → search "n8n-nodes-cognee"
# Or npm install in n8n instance directory
npm install n8n-nodes-cognee
```
Credentials: Base URL (`https://tenant-xxx.aws.cognee.ai`) + API Key from platform.cognee.ai.

### Limitations
- **Requires self-hosted n8n** — community nodes do NOT work on n8n Cloud (the managed offering)
- **Cognee Cloud only** — the node is designed for Cognee Cloud; self-hosted Cognee requires careful URL configuration
- **Version 0.4.0 breaking changes** — base URL format changed; re-entering credentials is required when upgrading
- **Cognify timeout** — 10 minutes default for Cognify operations; 5 minutes for others
- **No custom pipeline logic** — you're limited to the operations exposed by the node; advanced logic requires HTTP Request node or code nodes

### What Already Exists
- The node is **mature, published, and actively maintained** (v0.4.0 as of latest docs)
- Cognee's August 2026 update explicitly promoted n8n for "orchestrating memory workflows"
- Blog post from Dec 2025: "n8n × cognee: Add AI Memory to Any Workflow Automation" — with full examples
- Example workflows exist for: Customer Support Automation, Document Intelligence Pipeline, Research Assistant, Sales Intelligence
- **Risk**: Some teams will use n8n, but fewer than Claude Code. The differentiation risk is moderate.

### Why It's Powerful for the Hackathon
- **3-minute demo gold**: You can show a LIVE workflow canvas with colorful nodes, trigger a Slack message, and watch the entire pipeline execute in real-time
- **Judges can SEE memory working**: Add node → Cognify node → Search node → Response node — all visual
- **Composability**: Show data flowing from real apps (Slack, Gmail, Airtable) into Cognee memory and back out — this directly addresses "Potential Impact"
- **Zero backend code**: Perfect for the hackathon's time constraint

---

## 3. Cognee + Codex Integration

### What It Does
- **Official plugin** in `cognee-integrations` repo for OpenAI's Codex CLI agent
- **Architecture nearly identical to Claude Code plugin**:
  - Captures prompts, tool traces, and assistant responses into Cognee session memory
  - Recalls relevant memory on each prompt
  - Syncs session memory into graph memory during compaction, idle, and session-end flows
- **Session model**: Each new Codex terminal launch starts a new Cognee session by default
- **Shared dataset with Claude Code**: Both default to `agent_sessions`

### How to Set Up
```bash
# Enable hooks in Codex
echo '[features]\nhooks = true' >> ~/.codex/config.toml
# Add marketplace and install
codex plugin marketplace add topoteretes/cognee-integrations --ref main
codex plugin add cognee@cognee
export LLM_API_KEY="your-llm-api-key"
codex
```

### Limitations
- **Codex is newer than Claude Code** — smaller user base, less battle-tested plugin ecosystem
- **Hooks must be explicitly enabled** in `~/.codex/config.toml` before the plugin works
- **Same background-write delay** as Claude Code — writes are not immediately queryable
- **Session switching is per-terminal** — other terminals keep their own sessions
- **Cloud mode limitations** — updating existing data (modifying a previously synced file) is not yet supported in cloud mode

### What Already Exists
- The plugin is **official** but less documented than Claude Code
- Cognee's April 2026 hackathon (Daytona Moss) focused on PR Rescue with Codex/Claude Code, not this specific integration
- Codex itself is relatively new (released ~2026), so fewer community examples exist
- **Risk**: Codex is the "new shiny thing" from OpenAI. Some teams will use it, but fewer than Claude Code.

---

## 4. Cognee + OpenClaw Integration

### What It Does
- **npm package**: `@cognee/cognee-openclaw` — published on npm
- **Multi-scope memory hierarchy** — the ONLY integration with this feature:
  - **Company scope**: `acme-shared` — shared knowledge across all users/agents (`memory/company/policies.md`)
  - **User scope**: `acme-user-alice` — per-user preferences, feedback (`memory/user/preferences.md`)
  - **Agent scope**: `acme-agent-code-assistant` — per-agent learned behaviors (`memory/tools.md`, `MEMORY.md`)
- **Auto-Index**: On startup and after each agent run, scans `memory/` directory and syncs files to scope-specific Cognee datasets (add new, update changed, delete removed, skip unchanged)
- **Auto-Recall**: Before every agent run, searches all configured scopes in parallel and injects labeled results as `<cognee_memories>` context
- **Hash-based change detection** — minimizes API calls; only new or modified files are synced
- **Deletion Tracking** — removed memory files are automatically cleaned up from Cognee
- **14 search types** including `GRAPH_COMPLETION_COT`, `TEMPORAL`, `FEELING_LUCKY`
- **Hybrid mode**: Can run alongside OpenClaw's built-in `memory-core` instead of replacing it
- **One-command setup**: `openclaw cognee setup`
- **CLI commands**: `openclaw cognee index`, `openclaw cognee status`, `openclaw cognee health`, `openclaw cognee scopes`

### How to Set Up
```bash
openclaw plugins install @cognee/cognee-openclaw@2026.3.0
openclaw cognee setup  # or --hybrid
```
Configure in `~/.openclaw/openclaw.json`:
```yaml
plugins:
  entries:
    cognee-openclaw:
      enabled: true
      config:
        baseUrl: "http://localhost:8000"
        apiKey: "${COGNEE_API_KEY}"
        datasetName: "my-project"
        searchType: "GRAPH_COMPLETION"
        autoRecall: true
        autoIndex: true
```

### Limitations
- **Cloud mode update limitation**: Modifying a previously synced file is NOT supported in cloud mode. Must delete and re-add manually.
- **Requires OpenClaw setup first**: OpenClaw is less mainstream than Claude Code; learning curve exists
- **Multi-scope config is manual**: You must set `companyDataset`, `userDatasetPrefix`, `agentDatasetPrefix` explicitly
- **Smaller community**: Fewer Stack Overflow answers, fewer tutorials
- **OpenClaw agents write their own code**: This is powerful but can be unpredictable in a hackathon setting

### What Already Exists
- **Blog post from March 2026**: "OpenClaw Agents: 3 Viral Use Case Ideas Powered by Cognee" — Second brain, multi-agent team with shared memory, health/symptom tracker
- **Tested at AI-Memory Hackathon (Feb 7, 2026, SF)** — Cognee tested this plugin with the community in-person
- **Multi-scope routing is unique** — no other integration (Claude Code, Codex, n8n) has this company/user/agent hierarchy
- **Risk**: VERY LOW competition. OpenClaw is known in the "hacker" community but not mainstream. Most hackathon participants will gravitate to Claude Code or n8n.

### Why It Could Win
- **Directly addresses the hackathon theme**: "Where's My Context?" — OpenClaw's multi-scope routing literally answers "which context?" with company, user, and agent scopes
- **Technical Excellence**: Auto-index, hash-based sync, scope routing, and 14 search types show deep engineering
- **Best Use of Cognee**: Uses the most advanced and unique Cognee features (multi-scope, auto-recall, temporal search)
- **Creativity**: Self-extending agents that write their own code AND remember across scopes is a futuristic demo

---

## 5. Community Projects & Hackathon Precedents

### Previous Cognee Hackathons
| Date | Event | Partner | Focus | What Was Built |
|------|-------|---------|-------|----------------|
| Feb 7, 2026 | AI-Memory Hackathon #1 | Qdrant, Distil Labs, DigitalOcean | Procurement data, semantic search, anomaly detection | 3 FastAPI projects (search, analytics, anomaly detection) |
| Apr 25, 2026 | Daytona Moss Hackathon | Daytona, Moss | PR Rescue Arena | Self-improving agent skills for broken PRs |
| May 16, 2026 | AI-Memory Hackathon | Redis | Agent LLM Wiki | Wikipedia-style agent knowledge base |
| Jun 16, 2026 | Company Brain | — | Slack + Granola knowledge graph | Support assistant, expert finder, contradiction detector |
| Jun 19, 2026 | Cognee Cloud Hackathon | — | Company Brain on Cloud | Cloud-native company knowledge graph |
| Jun 26, 2026 | GTM Brain (Warsaw) | modelguide | Merge accounts, deals, conversations | Sales/marketing knowledge graph |

### Existing Projects Using These Integrations
1. **Claude Code**: `ai-memory` by Akita On Rails (independent but similar architecture); multiple blog tutorials; Cognee's most marketed integration
2. **n8n**: Mature node (v0.4.0); customer support workflows, document intelligence pipelines, sales intelligence; featured in Cognee August 2026 update
3. **Codex**: Fewer examples; plugin exists but less community content than Claude Code
4. **OpenClaw**: 3 viral use case ideas blog post (second brain, multi-agent team, health tracker); tested at Feb 2026 SF hackathon; npm package published

### GitHub Issues Relevant to Hackathon
- **#3460**: "Native support for Cognee on device for smartphone" — edge AI, Rust, mobile optimization
- **#3615**: "Support-triage bot powered by cognee memory" — active proposal for bot with citations
- **#3604**: "Make memory agents can trust — rankable, citable results" — judged on citations
- **#3601**: "Build LLM-mocked tests for all examples" — test coverage
- **#3608**: "Shared chat-memory adapter core for bots" — multi-user memory
- **#3605**: "Calm, Honest First Run — evaluate onboarding & propose improvements" — UX focus

---

## 6. Differentiation Analysis: What Will Other Teams Build?

### Most Teams Will Build With:
1. **Claude Code** (~40% of teams) — It's the most famous, easiest to understand, and has the most tutorials. Most teams will install the plugin and show "Claude remembers my codebase."
2. **n8n** (~25% of teams) — Visual workflows are appealing; some teams will build "customer support bot that remembers" or "Slack automation with memory."
3. **Codex** (~15% of teams) — The "new shiny" from OpenAI; some teams will try it because it's less crowded than Claude Code.
4. **OpenClaw** (~5% of teams) — Only the most adventurous/hacker-culture teams will attempt this.
5. **Native Python SDK** (~15% of teams) — Some will skip the integrations entirely and build custom agents with `cognee.remember()` / `cognee.recall()`.

### The Danger Zone
- **Claude Code "codebase memory" demos** will be saturated. Unless you have a truly unique twist (e.g., multi-repo memory, cross-team knowledge sharing, or a custom ontology), judges will have seen it before.
- **n8n "support ticket → Cognee → reply" workflows** will also be common. The node is so easy to use that multiple teams will build very similar automations.

### The Blue Ocean
- **OpenClaw multi-scope memory** has almost NO competition. The company/user/agent scope hierarchy is genuinely advanced and unique to this integration.
- **Cross-integration stories** (e.g., "My OpenClaw agent remembers, my n8n workflow triggers, and my Claude Code plugin shares the same dataset") would be exceptionally differentiated — but very hard to build in 7 days.
- **Custom ontology + OpenClaw** — Using OpenClaw's custom DataPoints with Cognee's graph extraction to build a domain-specific knowledge graph.

---

## 7. Final Recommendation

### If You Want to WIN: OpenClaw

**Why OpenClaw is the best strategic choice:**

1. **Differentiation**: You will likely be the ONLY team showing multi-scope memory routing. In a room of 20-30 finalists, being the only one in a category is a massive advantage.
2. **Best Use of Cognee**: The multi-scope hierarchy, auto-index, auto-recall, and 14 search types are the deepest use of Cognee's APIs among all integrations. This directly scores highly on the "Best Use of Cognee" judging criterion.
3. **Technical Excellence**: The hash-based sync, scope routing, and labeled context injection (`<agent_memory>`, `<user_memory>`, `<company_memory>`) show strong engineering.
4. **Creativity & Innovation**: Self-extending agents that write their own code AND remember across organizational scopes is a compelling narrative.
5. **Potential Impact**: A "company brain" that routes context correctly (shared knowledge vs. personal preferences vs. agent behavior) is a real enterprise problem.

**Demo Strategy for OpenClaw:**
- Show an OpenClaw agent in Telegram/WhatsApp
- First message: "What's our company's refund policy?" → pulls from `company` scope
- Second message: "Remind me, I prefer dark mode and Python" → pulls from `user` scope
- Third message: "What tools can you use?" → pulls from `agent` scope
- Show the graph visualization of how these scopes are separated but searchable
- Show the `memory/` directory being auto-indexed and the hash-based sync state

### If You Want to FINISH SAFELY: n8n

**Why n8n is the safest choice:**

1. **Demo-ability**: A visual workflow canvas is the most cinematic demo format. Judges can SEE data flowing through nodes in real-time.
2. **Presentation Quality**: You can trigger a Slack message, watch it flow through Add → Cognify → Search → Response nodes, and show the result. This is impossible to do badly in a 3-minute pitch.
3. **Composability**: Connect 3-4 real apps (Slack + Google Sheets + Email + Cognee) to show a complete business process. This screams "Potential Impact."
4. **Low Risk**: The node is mature. Setup is well-documented. You won't waste days debugging.

**Demo Strategy for n8n:**
- Build a "Customer Support Brain" workflow
- Trigger: New Slack support message
- Node 1: Add message to Cognee dataset `support_history`
- Node 2: Cognify the dataset
- Node 3: Search with `GRAPH_COMPLETION` for similar past issues
- Node 4: Draft response using OpenAI + retrieved context
- Node 5: Post response to Slack with citation links
- Show the BEFORE (generic response) vs AFTER (context-aware response with citations)

### Do NOT Build: Plain Claude Code Memory

Unless you have a truly novel twist (e.g., custom ontology for your specific domain, multi-agent collaboration, or a new hook that doesn't exist), this will be the most crowded category. The plugin is already built and documented by Cognee. You're not "building" — you're "using." In a hackathon, "using" a pre-built plugin without adding significant value rarely wins.

---

## 8. Judging Criteria Alignment

| Criteria | OpenClaw | n8n | Codex | Claude Code |
|----------|----------|-----|-------|-------------|
| Potential Impact | 9 | 9 | 6 | 6 |
| Creativity & Innovation | 9 | 7 | 6 | 5 |
| Technical Excellence | 9 | 6 | 6 | 6 |
| Best Use of Cognee | 10 | 7 | 7 | 7 |
| User Experience | 7 | 9 | 5 | 5 |
| Presentation Quality | 6 | 10 | 4 | 4 |
| **TOTAL** | **50** | **48** | **34** | **33** |

*(Scores out of 10 per criterion, max 60)*

---

## Sources

- Cognee GitHub: https://github.com/topoteretes/cognee
- Cognee Integrations: https://github.com/topoteretes/cognee-integrations
- Cognee n8n Node: https://github.com/topoteretes/cognee-n8n
- Cognee Docs: https://docs.cognee.ai/integrations
- n8n Integration Docs: https://docs.cognee.ai/integrations/n8n-integration
- OpenClaw Integration Docs: https://docs.cognee.ai/integrations/openclaw-integration
- Claude Code Plugin: https://github.com/topoteretes/cognee-integrations/tree/main/integrations/claude-code
- Codex Plugin: https://github.com/topoteretes/cognee-integrations/tree/main/integrations/codex
- OpenClaw Plugin: https://www.npmjs.com/package/@cognee/cognee-openclaw
- Hackathon Page: https://www.wemakedevs.org/hackathons/cognee
- Cognee Hackathons Repo: https://github.com/topoteretes/cognee-hackathons
- OpenClaw + Cognee Blog (Mar 2026): https://www.cognee.ai/blog/integrations/openclaw-agents-and-cognee
- n8n × Cognee Blog (Dec 2025): https://www.cognee.ai/blog/integrations/n8n-cognee-integration-build-workflows-with-memory
- Claude Agent SDK Blog (Dec 2025): https://www.cognee.ai/blog/integrations/claude-agent-sdk-persistent-memory-with-cognee-integration
- Cognee August Updates (Neptune, n8n, Time Graphs): https://www.cognee.ai/blog/cognee-news/cognee-august-updates
- Akita On Rails ai-memory (May 2026): https://www.akitaonrails.com/en/2026/05/23/i-built-memory-system-for-coding-agents-ai-memory/
- Cognee Company Brain Hackathon (Jun 2026): https://github.com/topoteretes/cognee-companybrain-hackathon
- Cognee AI-Memory Hackathon Template (Feb 2026): https://github.com/topoteretes/ai-memory-hackathon

---

*Report compiled on 2026-06-30 at 23:35 CEST by research sub-agent.*

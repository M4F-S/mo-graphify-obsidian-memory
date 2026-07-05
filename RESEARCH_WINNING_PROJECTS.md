# 🏆 Research: What Wins Hackathons — A Comprehensive Guide

**Research Date:** 2025-06-30
**Focus:** AI/Memory/Agent Hackathons, WeMakeDevs Events, Cognee Hackathon, Integration & Graph DB Projects
**Prepared For:** The Hangover Part AI — Cognee x WeMakeDevs Hackathon (June 29 – July 5, 2026)

---

## 1. WeMakeDevs Hackathon Winners (2024–2026)

### 1.1 FutureStack GenAI Hackathon (October 2025)
**Sponsors:** Cerebras, Meta, Docker | **Prize Pool:** $15,000+

| Project | Winner | Track | What They Built |
|---------|--------|-------|-----------------|
| **VoiceGraph** | Honey Paptan | **Best Use of Cerebras** | Multimodal RAG system with voice interaction, graph memory, and Cerebras-powered fast inference |
| **Sure AI** | Adithya Vardhan Reddy | **Best Use of Llama (Meta)** | AI agent platform for customer support, recruiting, and marketing with multi-agent CrewAI architecture + embeddable widget |
| **SRE Sentinel** | Aryan Kumar | **Best Use of Docker** | AI-powered incident response tool with memory of past incidents |
| **Objective Email** | Unknown | General | Privacy-first email assistant with local ML summarization, Gmail API integration, and smart prioritization |
| **Bengaluru Infra AI Agent** | Akshaya Parida | General | Civic reporting platform: citizens report potholes/garbage with GPS + photo, AI classifies via Cerebras Llama, auto-tweets/emails authorities |
| **FlowSprint.AI** | NUHASHROXME | General | Converts ideas into PRDs, mind maps, and starter code using Meta Llama via MCP Gateway |

**Key WeMakeDevs Stats:**
- 5,500+ participants, 7,000+ API signups in one hackathon
- WeMakeDevs hackathons consistently attract high-tier talent
- Sponsors report 3,000–7,000+ GitHub stars gained per event

### 1.2 AgentHack 2025 (Portia AI)
- **Winner:** Team Dark Mode (Anuj Upadhyay)
- **Duration:** 5 days of intensive building
- **Focus:** AI agent workflows with Portia AI guidance

### 1.3 Automate Me If You Can (Accomplish, Feb 2026)
- **Goal:** Use Accomplish (open-source AI coworker) to automate real tasks
- **Two tracks:** Highlight demo + Open-source contribution
- **Prizes:** $3,000 total, 30 winners ($100 each)
- **Key insight:** Building something that solves a real personal/business problem is highly valued

### 1.4 Kestra Hackathon (2025)
- Kestra hit 25,000 GitHub stars during the event
- Massive wave of developers building agentic and event-driven orchestration
- **Pattern:** Winning projects leveraged workflow automation + AI agents

---

## 2. AI Memory Hackathon Winners & Notable Projects

### 2.1 Convolve 4.0 — IIT Madras AI/ML Hackathon (Feb 2026)
**Sponsor:** Qdrant | **Prize Pool:** ~₹2 lakh (~$2,300)

| Place | Project | Builder | What They Built |
|-------|---------|---------|-----------------|
| 🥇 1st | **Masthishq** | Krishna Koushik Padigala | Multimodal AI agent as **cognitive prosthesis** for dementia patients. Uses FaceNet, YOLO, Qdrant vector search, and Llama 3 via Groq. Identifies people/objects, retrieves long-term memories ("This is Jill, your sister"), empathetic conversations. Patient app with animated avatar + caregiver dashboard. |
| 🥈 2nd | **SignalWeave** | T Mohamed Yaser | **Temporal AI memory system** for detecting emerging trends from weak signals. Continuous ingestion → vector embeddings → clustering → temporal merging. Qdrant as persistent vector memory layer. |
| 🥉 3rd | **Demeter** | Debarghya Das | Autonomous multi-agent hydroponic farm management. Creates **digital twin** with Farm Memory Unit (FMU) stored in Qdrant. Specialized agents (Water, Atmospheric, Doctor, Supervisor) retrieve historical cases for grounded decisions. |

**Key Insight:** All three winners treated **memory and retrieval as foundational infrastructure**, not add-ons. They built systems that remember, reason over history, and improve over time.

### 2.2 AI-Memory Hackathon by Cognee (Feb 2024, San Francisco)
- **Prize Pool:** $4,500+
- **Main prizes:** $1,200 / $900 / $500 cash
- **Special prizes:** $1,000 SLM training credits (Distil Labs), $1,000 Qdrant prize
- **Challenge:** Turn question-answering into useful agents/tools/workflows using local model + prebuilt knowledge graph over realistic finance/operations data
- **Winning approach:** Built systems that combine memory, retrieval, and inference locally — not chatbots

### 2.3 Memory Over Models — HiDevs × Qdrant × Lamatic (Nov 2025)
- **Themes:**
  - Unstructured Data RAG Challenge
  - **AI Second Brain:** Persistent memory OS for users (notes, chats, files, tasks as vectors)
  - Domain-Specific AI Systems (health, finance, HR, law, travel, education)
- **Goal:** Build retrieval-first, memory-driven AI systems — **not chatbots**
- **Key lesson:** Memory must be the **core of the product**, not a wrapper around an LLM

### 2.4 Notable Persistent Memory Projects

| Project | Event | Description |
|---------|-------|-------------|
| **Anamnesis** | Circle OpenClaw USDC Hackathon | Permanent, private, immutable AI memory. Encrypt → IPFS → Base blockchain. Won "Most Novel Smart Contract" + "Best OpenClaw Skill". Built entirely by AI agents. |
| **FlowState QMD** | Hermes 2026 Hackathon | Anticipatory memory for AI agents. SQLite + FTS5 + sqlite-vec. Multi-agent idempotency via cosine similarity dedup. Cache telemetry. |
| **Freak AI** | UMT Techverse AI Hackathon 2025 | Graph-Based Cognitive Agent using Neo4j + D3.js to model complex human memory systems. **Winner.** |

---

## 3. Graph Database (Neo4j) Hackathon Winners

### 3.1 Winning Projects Using Neo4j

| Project | Event | Result | What They Built |
|---------|-------|--------|-----------------|
| **Clinical Trial Recommender** | NEST 2025 (Novartis) | **Semifinalist** | AI-powered system with Knowledge Graphs, FAISS, NLP embeddings. 450K+ clinical trials. Neo4j for scalable graph + Jaccard similarity GDS ranking. |
| **VPBank Customer 360** | VPBank Tech Hackathon 2024 | **Top 18** (did not win) | Full AWS + Neo4j architecture for retail banking customer 360° view. 4-person team, 24 days. Used RDS, PostgreSQL, **Neo4j on EC2**, React, Django. |
| **Deloitte RAG** | Deloitte Vancouver Hackathon 2025 | **3rd Place** | Semantic search engine with RAG. Extracted triples (subject-predicate-object) from PDFs, loaded into Neo4j for graph visualization. $62 token budget. |
| **HopHacks Social Network** | HopHacks 2019 | **1st Place — Social Good** | Graph database-driven social network with Neo4j + Python. Recommendation and search features. |
| **BrowserBuddy** | Neo4j GraphConnect 2018 | **Best Graph Visualization** | Website domain + sub-path visualization using yFiles + Neo4j. Custom layout algorithm. |
| **Spatial Graph Apps** | Neo4j GraphConnect 2018 | **Special Prize — Perseverance** | Manhattan routing graph with geo-spatial Cypher queries. Won despite rendering bug (fixed with 2 lines of code after presentation). |

### 3.2 Neo4j Hackathon Patterns
- **Graph visualization wins:** Interactive, explorable graphs are highly demo-able
- **Knowledge graph + RAG is a proven winning combo**
- **Cypher code golf** rewards clever, concise queries
- **Real-world domain data** (clinical trials, banking, infrastructure) impresses judges
- **Key failure:** Teams often spend too much time on React toolchain issues and not enough on the actual graph/visualization

---

## 4. Integration-Focused Winners (Claude Code, n8n, MCP, etc.)

### 4.1 Winning Integration Patterns

| Project | Integration | Result | Approach |
|---------|-------------|--------|----------|
| **Sure AI** | Meta Llama + Cerebras + CrewAI + Tavus + Stripe MCP + Slack + Cal.com | **Meta Track Winner** ($5,000) | Multi-agent platform with embeddable widget. 3 core agent systems: customer support, email marketing, recruiting. |
| **Bengaluru Infra AI** | Cerebras LLaMA + Docker MCP Gateway + Twitter API | FutureStack submission | Full civic stack: PWA, real-time Leaflet map, AI classification, smart notifications, rate limiting |
| **FlowSprint.AI** | Meta Llama + MCP Gateway | FutureStack submission | Idea → PRD → mind map → starter code pipeline |
| **Anamnesis** | OpenClaw + IPFS + Base blockchain | **OpenClaw Skill Winner** | AI agent memory stored on-chain with AES-256 encryption |
| **Nutritional Tracking System** | Claude Code + n8n MCP + Telegram + Whisper + Supabase | Demo/tutorial | Full automation: voice → text → nutrition analysis → database → confirmation |

### 4.2 Integration Best Practices from Winners
- **MCP (Model Context Protocol) is a major winning pattern** in 2025–2026
- **Claude Code + n8n** combination enables zero-backend visual automation loops
- **Embedding widgets** into existing tools (websites, VS Code, etc.) shows immediate value
- **Multi-integration projects** demonstrate breadth and real-world applicability
- **Sponsor tech stack alignment** matters — using sponsor APIs deeply improves track chances

---

## 5. Cognee's Own Hackathons & Competitions

### 5.1 AI-Memory Hackathon #1 (Feb 2024, San Francisco)
- **Organizer:** Cognee
- **Partners:** Distil Labs, Qdrant, DigitalOcean, Pebblebed Ventures, Vermillion Ventures
- **Judges:** Vasilije Markovic (CEO, Cognee), Daniel Scott (Principal AI Researcher, Cognee), Thierry Damiba (Qdrant), Lizzie Siegle (DigitalOcean)
- **Format:** 9 AM – 6 PM single-day event
- **Challenge:** Local model + prebuilt knowledge graph over finance/ops data → build agents/tools/workflows
- **Example architectures provided:**
  - Project 1: Procurement Semantic Search (port 7777)
  - Project 2: Spend Analytics Dashboard (port 5553)
  - Project 3: Anomaly Detective (port 6971)
- **Stack:** Cognee + Qdrant Cloud + Distil Labs SLM + DigitalOcean

### 5.2 Cognee-Daytona-MOSS Hackathon (April 2026, San Francisco)
- **Theme:** PR Rescue Arena — Self-improving agent skills
- **Awards:**
  - Best PR Rescue Skill
  - Best Self-Improvement Loop (SkillRunEntry feedback stored in Cognee → skill improves)
  - Best Agent Team (multi-agent workflow: scout, fixer, critic, editor, verifier)
- **Key requirement:** Show the loop working — baseline → run → feedback → improvement → better run
- **Evidence required:** Before score, after score, feedback records, skill diff, run output

### 5.3 The Hangover Part AI (June 29 – July 5, 2026)
**Current Event — Organized by WeMakeDevs, sponsored by Cognee**

- **Prize Pool:** $10,000 unified
- **Team Size:** 1–4 members (max 4)
- **Duration:** 7 days (100% virtual)
- **Grand Prizes:**
  - **Best Use of Open Source Track:** Apple MacBook Neo per team member
  - **Best Use of Cognee Cloud Track:** Apple iPhone 17 per team member
  - **Job Interview Pipeline:** Top winners → technical interviews with Cognee core engineering team
- **Open Source Track:** $100 per accepted PR (top 20 submissions, max 5 PRs per person)
- **Blog Track:** Best blogs win Keychron mechanical keyboard ($120)
- **Social Track:** Top 10 social posts → exclusive swag
- **Integrations explicitly allowed:** Claude Code, Codex, n8n, OpenClaw
- **Core API:** `remember()` → `recall()` → `improve()`/`memify` → `forget()`

### 5.4 Current Cognee GitHub Competition (June 2026)
- **Issue #3652:** Dataset versioning / snapshots / undo-forget
- **Format:** 3 competing approaches, best wins
- **Judging criteria:** Fidelity, storage/perf overhead, query ergonomics, test quality
- **Active development:** Provenance/ledger-based delete model, graph-native delete/rollback

---

## 6. "The Hangover" Themed & Playful Hackathons

### 6.1 The Hangover Part AI (Current Event)
- **Theme:** "Your AI woke up in Vegas with no memory"
- **Tagline:** "Where's My Context?"
- **Tone:** Fun, playful, but technically serious
- **Playful elements:**
  - Vegas/casino metaphors ("The house always remembers")
  - `wheres_my_context.py` starter code
  - `forget(dataset="last_nights_mistakes")` example
- **Judging:** Strictly professional on 6 criteria (Impact, Creativity, Technical Excellence, Cognee Use, UX, Presentation)

### 6.2 Other Playful/Themed Hackathons
- **Boston Stupid Shit No One Needs & Terrible Ideas Hackathon:** Deliberately builds useless, terrible things. Winners judged on humor/terribleness.
- **Neo4j GraphConnect Buzzword Bingo:** Teams must use graph-related buzzwords in a "bingo" card. Prize for "Most Buzzword Technologies Used."
- **Key insight:** Playful themes **lower the barrier** and encourage creative risk-taking, but **winning projects still demonstrate technical depth** underneath the fun.

---

## 7. Common Patterns Among Winning Projects

### 7.1 What Winners Consistently Do

| Pattern | Evidence | Why It Works |
|---------|----------|--------------|
| **Solve a real, relatable problem** | Masthishq (dementia care), SRE Sentinel (3 AM pages), Objective Email (inbox overload), Bengaluru Infra (potholes) | Judges feel the pain. Real problems = real impact. |
| **Treat memory as infrastructure, not a feature** | Masthishq, SignalWeave, Demeter, Sure AI | Shows architectural thinking. Memory is the foundation, not an afterthought. |
| **Multi-agent or multi-modal architecture** | Sure AI (3 agent systems), Demeter (4 specialized agents), Masthishq (CV + LLM + vector) | Demonstrates technical depth and scalability. |
| **Fast, visible demo with a "golden path"** | All winners | Judges see 3 minutes. One flawless user story beats 10 features. |
| **Deep sponsor tech integration** | Sure AI (Meta Llama + Cerebras), VoiceGraph (Cerebras), SRE Sentinel (Docker) | Track prizes depend on sponsor alignment. Shows you did the homework. |
| **Production-ready framing** | Bengaluru Infra ("production-ready, full-stack"), Sure AI (SaaS platform vision) | Judges invest in potential. Show where this goes. |
| **Clear narrative: Problem → Solution → Demo → Impact** | All documented winners | Structured thinking = structured pitch. |
| **Visual dashboards, maps, or graph visualizations** | Bengaluru Infra (Leaflet map), Demeter (digital twin), Neo4j projects (interactive graphs) | Visuals create "wow" in seconds. |

### 7.2 Technical Depth vs. Visual Demo
- **The winners have both.** Technical depth is necessary for credibility; visual polish is necessary for memorability.
- **A common mistake:** Teams build impressive backends but show nothing visual. Judges cannot see your architecture in 3 minutes.
- **Another mistake:** Teams build flashy UIs with no real technical innovation. Judges will ask hard questions.
- **Sweet spot:** One technically impressive, well-explained component + one beautiful, demoable interface.

---

## 8. What Makes a Project "Demo Well" in 3 Minutes

### 8.1 The 3-Minute Structure (Proven by Winners)

```
0:00–0:30  HOOK
           Start with a story, shocking stat, or question.
           "What if I told you 60% of hackathon projects never get demoed
            because teams run out of time?"
           "Every AI session starts from zero — like waking up with amnesia."

0:30–1:30  SOLUTION DEMO
           Show, don't tell. Walk the "golden path" — one perfect user story.
           Example: "Let me show you how Anamnesis remembers everything
           across sessions... [live demo]"
           Show the "wow" moment FIRST. Click through the main flow.

1:30–2:30  THE "HOW" (ONE SLIDE)
           Architecture diagram (1 slide max).
           Key technologies.
           What makes your approach UNIQUE.
           Briefly mention: "Hybrid graph-vector memory via Cognee"

2:30–3:00  VISION & IMPACT
           Who benefits? How many people? What's the 6-month roadmap?
           Call to action: "This is just the beginning."
```

### 8.2 Demo Best Practices

1. **Script the "golden path"** — know exactly which buttons to click in which order
2. **Pre-load everything** — have data, accounts, and pages already set up
3. **Rehearse the exact sequence 5+ times** — even at 3 AM
4. **Have a backup video** — record a working demo. Live demo failures are deadly
5. **Narrate while clicking** — explain what is happening and WHY it matters
6. **Don't apologize** — if something is rough, don't draw attention to it
7. **Make eye contact with judges** — not your screen
8. **Fail gracefully** — know what to say if something breaks (then show the backup)

### 8.3 What Kills a Demo

- Starting with "Hi, we're Team XYZ and we built..." (BORING — judges have heard this 20 times)
- Spending 2 minutes on slides before showing the product
- Apologizing for bugs or incomplete features
- Going over time (strictly enforced)
- Live demo of untested features (Murphy's Law is undefeated)
- Too many features — show ONE thing perfectly

---

## 9. Most Common Mistakes That Cause Projects to Lose

### 9.1 Fatal Mistakes

| Mistake | Why It Kills You | How to Avoid |
|---------|------------------|--------------|
| **No time spent on presentation** | "About half an hour before hacking ends, stop everything and plan your pitch." | Assign a pitch lead from hour one. Allocate 20% of total time to presentation. |
| **Unrealistic scope** | Trying to build 10 features in 7 days. | Scope for your DEMO, not a real product. One killer feature. Golden path only. |
| **Live demo of untested features** | "Demo failures are almost always preventable." | Rehearse 5+. Have backup video. Pre-load all data. |
| **Vague problem statement** | Judges don't understand why it matters. | Start with a specific pain point. Quantify it if possible. |
| **Ignoring judging criteria** | You built something great... but not what they asked for. | Study criteria. Weight effort toward what's measured. |
| **No visuals** | Judges cannot see your backend architecture. | Add a dashboard, map, graph visualization, or animated UI. |
| **Team too large** | "Beyond 4 people, communication and integration issues become a major hindrance." | Max 4 for this hackathon (WeMakeDevs limit). Ideal is 2–3. |
| **Learning new tools during the hackathon** | "This is not the time to learn a new framework." | Use boring, familiar tools. Managed services (Firebase, Supabase, Vercel). |
| **Incomplete submission** | Missing fields, broken links, no README. | Checklist before submit. Test every link. |
| **AI-generated spam PRs** | WeMakeDevs explicitly bans this. | "Anyone who opens more than 5 PRs will be banned." |

### 9.2 Subtle Mistakes

- **Not researching the judges** — Tailor your pitch to their backgrounds (technical vs. business vs. design)
- **No differentiation from other teams** — "Just add AI" is not a strategy. What's your unique angle?
- **Over-engineering the wrong parts** — Teams spend 3 hours fighting React builds instead of showing the graph
- **No backup plan** — If your API key expires, your demo dies. Have fallbacks.
- **Forgetting to show the "why"** — "What changes if this exists?" must be answered.

---

## 10. Integration/Demo Approach with the Most "Wow" Factor

### 10.1 Highest-Wow Approaches (Ranked)

1. **Live multi-agent workflow** — Show 2+ agents collaborating in real-time with memory persistence. Example: "Agent A researched this yesterday. Agent B is now using that memory to make a decision."

2. **Interactive graph visualization** — Click a node in a knowledge graph, watch the AI recall and reason. Neo4j + D3.js or Cytoscape.js creates instant visual impact.

3. **Embeddable widget/live integration** — "Here's our AI memory layer running INSIDE Claude Code / n8n / VS Code." Showing your tool inside another tool judges already know is powerful.

4. **Before/after comparison** — Show the AI with NO memory (failing) vs. WITH memory (succeeding). The contrast is instantly understandable.

5. **Real-time civic/social impact** — Map with live pins, dashboard with live metrics, or a bot that just tweeted/emailed something real. Tangible evidence beats promises.

6. **Cross-session memory demo** — Start a session, have a conversation, end it, start a NEW session, and show the AI remembers. This directly addresses the "hangover" theme.

### 10.2 Recommended Stack for Maximum Wow

Given the Cognee hackathon constraints, the highest-wow stack would be:

```
Frontend:          Next.js + Tailwind + shadcn/ui (fast, modern, demo-ready)
Backend:           FastAPI (Python) or Next.js API routes
Memory Layer:      Cognee (open source or cloud) — hybrid graph-vector
Visualization:     D3.js / Cytoscape.js / React Force Graph for knowledge graph
Integration:       Claude Code extension OR n8n workflow OR OpenClaw skill
Deployment:        Vercel (frontend) + Railway/Render (backend) or Docker
Demo Data:         Pre-seeded with realistic, relatable content (emails, notes, code)
```

---

## 11. WeMakeDevs Judging Patterns — What They Consistently Favor

### 11.1 Evidence from Past Winners

1. **Open-source alignment** — WeMakeDevs is a community-first organization. Projects that contribute to or deeply use open-source tools win tracks. The "Best Use of Open Source" track prizes a MacBook Neo per person — this is NOT a minor prize.

2. **Production-ready mindset** — Winners frame their projects as "production-ready, full-stack platforms" (Bengaluru Infra) or "SaaS platforms" (Sure AI). Even if MVP, the vision is enterprise-grade.

3. **Sponsor technology depth** — Winners don't just "use" Cerebras or Llama; they explain WHY that choice matters ("lightning-fast inference," "open-source and developer-friendly"). They name-drop the sponsor's product and explain its value.

4. **Real-world problem + real data** — Civic issues (Bengaluru), email overload (Objective Email), 3 AM pages (SRE Sentinel), dementia care (Masthishq). All touch real human pain.

5. **Technical blog writeups** — WeMakeDevs winners consistently write detailed dev.to / blog posts explaining their architecture. This is a separate prize category (Keychron keyboard) AND builds community credibility.

6. **Social media engagement** — Winners tag @wemakedevs and sponsors. Top 10 social posts get swag. This is free marketing and shows community participation.

7. **GitHub stars + engagement** — WeMakeDevs hackathons generate 3,000–7,000 GitHub stars for sponsors. A well-documented, star-worthy repo is a signal of quality.

### 11.2 Cognee-Specific Favor Signals

Based on the current hackathon criteria and Cognee's past events:

| Cognee Priority | How to Demonstrate |
|-----------------|-------------------|
| **Deep Cognee API use** | Use all 4 lifecycle methods: `remember()`, `recall()`, `improve()`, `forget()` |
| **Graph-vector hybrid** | Show the knowledge graph visualization. Don't hide it. |
| **Self-hosted / open source** | The MacBook Neo track REWARDS open-source Cognee use. Run it locally. |
| **Real memory persistence** | Demo cross-session memory. Close browser, reopen, show recall. |
| **Integration with allowed tools** | Claude Code, n8n, Codex, or OpenClaw integration is explicitly encouraged |
| **Technical excellence** | Clean code, tests, README, architecture documentation |
| **GitHub contributions** | $100/PR for top 20 submissions. Start NOW. |

---

## 12. Optimal Team Size & Division for a 6-Day Hackathon

### 12.1 Recommended Team Size: 2–3 People

**Evidence:**
- WeMakeDevs max: 4 members
- "For a two-day hackathon, a team size of three seems to be ideal; four is the maximum. Beyond that, the speed of communication and integration issues become a major hindrance." — Hackathon veteran analysis
- "Ideal team size is 4–6 people: large enough for division of labor, small enough for decision-making." — For longer events
- Convolve 4.0 winners: Solo builders (1st and 2nd place were solo!)

**For a 7-day virtual hackathon:**
- **Solo:** Possible if you are a full-stack generalist. Risk: burnout, no one to debug with.
- **2 people:** **Ideal.** One frontend/demo + one backend/memory. Pair on architecture decisions.
- **3 people:** Good if you have a dedicated pitch/design person. Risk: coordination overhead.
- **4 people:** Maximum. Need clear role separation. Risk: integration conflicts, merge hell.

### 12.2 Recommended Role Division (2-Person Team)

**Person A: The Builder (Backend + Memory)**
- Owns Cognee integration (`remember`, `recall`, `improve`, `forget`)
- Builds the core data pipeline
- Handles deployment and infrastructure
- Ensures the memory layer actually works

**Person B: The Demo Maker (Frontend + Presentation)**
- Owns the UI/UX and visualization
- Scripts the demo path and records backup video
- Writes the README and blog post
- Prepares the pitch and architecture slide

### 12.3 Recommended Role Division (3-Person Team)

**Person A: Backend + Cognee Memory**
**Person B: Frontend + Visualization**
**Person C: Demo Script + Pitch + Blog + Social Media**

### 12.4 Timeline for 7-Day Hackathon

| Day | Focus | Activities |
|-----|-------|------------|
| **Day 1 (Mon)** | Planning & Setup | Define problem, sketch architecture, set up repos, Cognee local dev environment, deploy empty app to Vercel |
| **Day 2 (Tue)** | Core Memory | Implement `remember()` + `recall()` with Cognee. Test with sample data. |
| **Day 3 (Wed)** | Frontend Skeleton | Build UI shell, graph visualization placeholder, dashboard layout |
| **Day 4 (Thu)** | Integration | Wire frontend to backend. Implement `improve()` + `forget()`. Integration with Claude Code/n8n/OpenClaw if applicable. |
| **Day 5 (Fri)** | Demo Polish | Seed realistic data. Script golden path. Record backup video. Fix UI polish. |
| **Day 6 (Sat)** | Pitch & Docs | Write README, architecture doc, blog post. Rehearse pitch 5+. Prepare architecture slide. |
| **Day 7 (Sun)** | Submit & Social | Submit to Devpost/hackathon portal. Publish blog. Post on X/LinkedIn tagging @wemakedevs and @cognee. Make last-minute PRs if doing open-source track. |

---

## 13. Specific Recommendations for a Winning Cognee Project

### 13.1 Problem Selection (Pick ONE)

Choose a problem that is:
- **Relatable to judges:** Personal knowledge management, developer workflow, or AI agent continuity
- **Demonstrates memory failure clearly:** Show the AI forgetting, then show it remembering with Cognee
- **Has visual potential:** Dashboards, knowledge graphs, timeline views, or interactive maps

**Top 3 recommended angles for this hackathon:**

1. **"The AI Personal Historian"** — Cognee remembers every conversation, file, and project across sessions. Demo: start a coding session on Monday, continue on Wednesday, AI remembers your architecture decisions and bugs you were fixing.

2. **"Multi-Agent Council with Collective Memory"** — 3 agents (researcher, writer, critic) share a Cognee knowledge graph. Each agent remembers what the others did. Demo: show agent A's research being recalled by agent B 2 hours later.

3. **"The Hangover Recovery Agent"** — Playful but functional. An AI that "remembers what happened last night" across your tools: emails, code commits, meeting notes, all stored in Cognee's graph. Demo: "I lost context after 3 days away. Let me recall everything." → Graph visualization shows all connections.

### 13.2 Technical Architecture Recommendation

```
┌─────────────────────────────────────────┐
│         NEXT.JS FRONTEND                │
│  • Interactive Knowledge Graph (D3.js)  │
│  • Memory Timeline / Session History    │
│  • Chat Interface with Recall           │
│  • "Before/After Amnesia" Toggle        │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│         FASTAPI BACKEND                 │
│  • Cognee Integration Layer             │
│    - remember() / recall()              │
│    - improve() / forget()               │
│  • Data Ingestion (files, URLs, text)    │
│  • Vector + Graph Query Router           │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│         COGNEE MEMORY LAYER             │
│  • Hybrid Graph-Vector Storage         │
│  • Knowledge Graph (Neo4j/NetworkX)      │
│  • Vector Embeddings (Qdrant/Chroma)   │
│  • Provenance / Source Tracking        │
└─────────────────────────────────────────┘
```

### 13.3 Demo Script Recommendation (3 Minutes)

**0:00–0:30 — Hook:**
> "Every AI session starts like a hangover. You open ChatGPT, and it has no idea what you were working on yesterday. I'm going to show you what happens when AI actually remembers."

**0:30–1:30 — The Amnesia Problem (Live):**
> Open a generic chatbot. Ask: "What bug was I fixing in my auth module last Tuesday?" → Generic, unhelpful response. "See? Amnesia."

**1:30–2:15 — The Solution (Live):**
> Switch to your app. Same question. Watch Cognee `recall()` traverse the knowledge graph. Show the graph visualization lighting up connections. AI responds: "You were fixing a JWT refresh bug in `auth.py` on Tuesday. You also noted it relates to Issue #247."

**2:15–2:45 — The Architecture (One Slide):**
> "Cognee's hybrid graph-vector memory. `remember()` ingests my code and notes. `recall()` routes between semantic similarity and graph traversal. `improve()` prunes stale nodes. This is self-hosted, open-source, and integrates with Claude Code and n8n."

**2:45–3:00 — Vision:**
> "This isn't just a chatbot upgrade. It's a new layer of infrastructure. The MacBook Neo track is right there — but what we're really building is AI that doesn't forget."

### 13.4 Critical Success Factors

| Factor | Action | Priority |
|--------|--------|----------|
| **Deep Cognee use** | Use all 4 APIs. Show graph traversal. | MUST |
| **Visual graph** | Interactive knowledge graph in UI | MUST |
| **Backup demo video** | Recorded by Day 5 | MUST |
| **Open-source track** | Submit 1–2 quality PRs before/during | HIGH |
| **Blog post** | Publish on dev.to / Hashnode | HIGH |
| **Social posts** | Tag @wemakedevs, @cognee, use #HangoverPartAI | MEDIUM |
| **Integration** | Claude Code extension or n8n workflow | HIGH (for differentiation) |
| **Tests** | At least basic integration tests | MEDIUM |
| **Clean README** | Setup instructions, architecture diagram, demo GIF | HIGH |
| **Pitch rehearsal** | 5+ times with timer | MUST |

---

## 14. Summary: The Winning Formula

```
WIN = Real Problem × Deep Cognee Integration × Visual Demo × Polished Pitch × Open Source Contribution
```

**The 5-Point Checklist:**

1. ✅ **Real problem** — Judges feel it personally. Dementia, email overload, 3 AM pages, lost context.
2. ✅ **Memory as infrastructure** — Cognee is not a wrapper. It's the foundation. Show graph-vector hybrid.
3. ✅ **Golden path demo** — One flawless 90-second user story. Pre-loaded data. Backup video ready.
4. ✅ **Pitch from Day 1** — 20% of time on presentation. Rehearse 5+. Architecture on one slide.
5. ✅ **Contribute to open source** — 1–2 accepted PRs on Cognee. $100/PR. Shows community investment.

**Final Advice:**
> "The teams that think 'just add AI' is a strategy are focused on technology. What separates winning projects is tactical execution focused on real problems and clear communication. Technology is just the enabler — strategy is everything else." — Klaviyo hackathon winner analysis

> "A mediocre project with an amazing pitch beats an amazing project with a mediocre pitch. This isn't fair, but it's reality." — Hackathon pitch guide

> "Build a demo, not software. Scope accordingly." — Ainna hackathon guide

---

*Sources: WeMakeDevs official site, Devpost winner pages, Cognee blog and GitHub, dev.to winner writeups, Qdrant blog, Neo4j blog, multiple hackathon strategy guides, and winner repositories analyzed June 2026.*

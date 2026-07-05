# Deep Research: Novel Cognee Use Cases for The Hangover Part AI Hackathon

**Date:** July 1, 2026  
**Hackathon:** The Hangover Part AI (Cognee x WeMakeDevs, June 29 – July 5, 2026)  
**Research Goal:** Identify 5-10 genuinely novel use cases that NO ONE has built with AI memory/knowledge graphs, leveraging Cognee's unique features.

---

## Executive Summary

After exhaustive research across 20+ domains, analysis of Cognee's architecture, competitor landscape, and the hackathon's previous builds, **9 genuinely novel use cases** emerged that:
- Have **NO existing AI-powered memory solution** in production
- **Explicitly use Cognee's unique features** (graph + self-improvement + temporal + ontology + multi-tenant) — not just "vector search + memory"
- Have **real adoption potential** with clear user pain points
- Are **demoable in 3 minutes** with compelling visual output
- Are **feasible in 6 days** with focused scope

**What the Cognee community is ALREADY building (AVOID):**
- Company brains (Slack + Granola) — *Cognee's own hackathon produced this*
- Support ticket memory — *Cognee's canonical tutorial*
- GTM/sales knowledge graphs — *June 2026 hackathon*
- Agent wikis / simple chatbot memory — *Redis hackathon, May 2026*
- Regulatory compliance / document RAG — *APAC GraphRAG guide uses Cognee*

**What NO ONE is building yet:** Personal life archaeology, contradiction-aware memory, and temporal reasoning in domains where human memory is fallible and relationships matter.

---

## Cognee's Unique Feature Stack (What Competitors CANNOT Do)

| Feature | Cognee | Mem0 | Zep | GraphRAG | Letta |
|---------|--------|------|-----|----------|-------|
| Hybrid Graph + Vector | ✅ Native | ⚡ Partial | ⚡ Partial | ✅ Yes | ❌ No |
| Self-Improvement (memify) | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No |
| Temporal Reasoning | ✅ temporal_cognify | ❌ No | ⚡ Partial | ❌ No | ❌ No |
| Ontology Grounding | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No |
| Multi-Tenant Isolation | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | ⚡ Partial |
| Contradiction Detection | ✅ Yes | ⚡ Basic | ⚡ Basic | ❌ No | ❌ No |
| 14 Retrieval Modes | ✅ Yes | ⚡ Limited | ⚡ Moderate | ⚡ Limited | ⚡ Limited |

*Source: Benchmark reviews from tryxlr8.ai, mcp.directory, and xlr8.ai (June 2026)*

**Key insight:** Cognee is the ONLY open-source framework that combines *all six* capabilities. Most competitors are either vector stores with light memory (Mem0), temporal session memory (Zep), or graph-only corpus tools (GraphRAG). The **self-improvement + temporal + ontology + contradiction** stack is Cognee's monopoly.

---

## Domain-by-Domain Gap Analysis

### 1. Argument Mapping / Debate Tools
**Existing:** Kialo (manual tree), DebateGraph (manual), Argunet (defunct), AI argument map generators (static, no memory)
**AI Memory?** ❌ No persistent knowledge graph. No contradiction detection across debates.
**Gap:** No tool auto-ingests debates, builds a persistent argument graph, detects contradictions across time, or self-improves argument quality scores.

### 2. Genealogy / Family History
**Existing:** Ancestry.com (record matching), MyHeritage (DNA + photos), FamilySearch (collaborative tree)
**AI Memory?** ❌ No. AI is used for OCR and record matching, NOT for building knowledge graphs of family stories with contradiction detection.
**Gap:** No tool ingests oral histories, interviews, and documents into a knowledge graph that detects contradictions ("Grandpa said X, Aunt says Y") and resolves confidence over time.

### 3. Mediation / Negotiation
**Existing:** Modria, Smartsettle, Cybersettle (blind bidding, preference analysis)
**AI Memory?** ❌ No persistent knowledge graph of negotiation history. No temporal reasoning across sessions.
**Gap:** No tool builds a knowledge graph of multi-party negotiation positions, tracks how positions evolve, and detects contradictions between stated positions and past agreements.

### 4. Investigative Journalism
**Existing:** Aleph (entity search), i2 Analyst's Notebook (visualization)
**AI Memory?** ❌ No. These are search and visualization tools, not memory systems.
**Gap:** No tool builds a persistent investigation graph, auto-detects contradictions in witness statements, and self-improves confidence in facts as evidence accumulates.

### 5. Civic Engagement / Democratic Deliberation
**Existing:** Decidim (participation platform), Panoramic AI (RAG for consultations), Deliberation Knowledge Graph (academic research paper)
**AI Memory?** ⚡ The Deliberation Knowledge Graph is an ACADEMIC PAPER only. No production tool exists.
**Gap:** No production tool integrates institutional + civic deliberation into a temporal knowledge graph with argument quality tracking and contradiction detection.

### 6. Scientific Research Memory
**Existing:** AutoSci (academic paper, May 2026 — NOT a product), lab notebooks (manual)
**AI Memory?** ⚡ AutoSci is a research prototype. No production tool.
**Gap:** General-purpose lab notebook with knowledge graph, ontology validation, and self-improving research memory is not productized.

### 7. Mental Health / Therapy Tracking
**Existing:** Therapy apps (BetterHelp, Talkspace), mood trackers (Daylio)
**AI Memory?** ❌ No. Purely conversational or scalar tracking.
**Gap:** No tool builds a knowledge graph of therapy themes, triggers, insights, and medications with temporal reasoning and contradiction detection.

### 8. Real Estate / Property History
**Existing:** Zillow, Redfin (listings), property records (public databases)
**AI Memory?** ❌ No. Static data, no knowledge graph of property life history.
**Gap:** No tool builds a knowledge graph of inspections, renovations, permits, disclosures, and owner notes with contradiction detection and temporal reasoning.

### 9. Estate Planning / Legacy Preservation
**Existing:** Evaheld (digital vault with basic AI prompts), Trust & Will (document generation)
**AI Memory?** ❌ No. Evaheld stores documents but does not build a knowledge graph or reason about contradictions.
**Gap:** No AI tool builds a structured memory of family stories, values, and legal documents that can answer complex queries and detect contradictions between will versions.

### 10. Open Source Governance / RFC Tracking
**Existing:** GitHub Discussions, RFC repos, Semantica (general governance)
**AI Memory?** ⚡ Semantica is general-purpose. No specific open-source governance memory tool.
**Gap:** No tool specifically for open-source projects that tracks RFC arguments, decisions, and contradictions over time with institutional memory.

### 11. Event Planning / Wedding Planning
**Existing:** AI Gantt charts, Converiqo (vendor coordination), HoneyBook
**AI Memory?** ❌ No. Workflow automation, not persistent knowledge graph.
**Gap:** No tool builds a knowledge graph of event decisions, vendor relationships, and family preferences that persists and improves across multiple events.

### 12. Sports Coaching / Athlete Development
**Existing:** LLM-SPTRec (academic paper, 2026), wearable analytics (Whoop, Garmin)
**AI Memory?** ⚡ LLM-SPTRec is academic. No production product.
**Gap:** No tool builds a persistent knowledge graph of an athlete's full career history, injuries, techniques, and coaching advice with correlation discovery.

### 13. Music Production / Creative Collaboration
**Existing:** Suno, AIVA, MusicGen (generation), Teragraph (academic music graph)
**AI Memory?** ⚡ Teragraph is academic. No production creative memory tool.
**Gap:** No tool builds a knowledge graph of creative decisions, sounds, samples, and collaboration history that self-improves and enables temporal reasoning.

### 14. Language Learning with Ontology Validation
**Existing:** Duolingo, Babbel, MARTIALIS (medical ontology validation)
**AI Memory?** ⚡ MARTIALIS is for medical text. No general language learning tool.
**Gap:** No language learning app validates learner output against a linguistic ontology, tracks errors as a knowledge graph, and self-improves the curriculum.

### 15. Food / Nutrition Memory with Correlation Tracking
**Existing:** SwissFKG (food knowledge graph for recipes), MyFitnessPal (calorie tracking)
**AI Memory?** ⚡ SwissFKG is for public recipes. No personal correlation tool.
**Gap:** No personal tool tracks meals, symptoms, sleep, and energy in a knowledge graph to discover temporal correlations and self-improve its models.

### 16. Legal Contract Evolution Tracking
**Existing:** CLM platforms (Sirion, Agiloft, Aline, Salesforce), AI contract review
**AI Memory?** ❌ No. CLM tracks versions but does not build a knowledge graph of clause evolution with contradiction archaeology.
**Gap:** No tool builds a granular knowledge graph of how individual clauses evolved through negotiation, with temporal reasoning and provenance.

### 17. Supply Chain / Product Provenance
**Existing:** Blockchain traceability (IBM Food Trust), pharmaceutical tracking
**AI Memory?** ❌ No AI knowledge graph. Blockchain is ledger, not memory.
**Gap:** No AI tool builds a knowledge graph of supply chain events with contradiction detection and temporal reasoning.

### 18. Democratic Process / Legislation Tracking
**Existing:** GovTrack, LegiStorm, Deliberation Knowledge Graph (academic)
**AI Memory?** ⚡ Academic only. No production tool.
**Gap:** No production tool builds a temporal knowledge graph of legislation, amendments, and arguments with contradiction detection.

### 19. Disaster Response / Emergency Management
**Existing:** MHGSA (academic multimodal graph for disaster classification), EM-DAT database
**AI Memory?** ⚡ Academic only. No production persistent memory for responders.
**Gap:** No tool builds a persistent, self-improving knowledge graph of incident reports, eyewitness accounts, and resource deployments with contradiction detection.

### 20. Academic / Personal Life Logging
**Existing:** Day One, Obsidian, Roam Research (note-taking)
**AI Memory?** ❌ No. These are note-taking tools, not reasoning systems.
**Gap:** No tool builds a knowledge graph of personal life events, documents, and photos with temporal reasoning and contradiction detection.

---

## The 9 Most Promising Novel Use Cases

### 1. 🏠 PropertyDNA — "The Carfax for Houses, But Intelligent"
**Domain:** Real Estate / Property History  
**The Problem:** Home buyers make the biggest purchase of their life with fragmented, contradictory information. Inspection reports, seller disclosures, permits, and HOA documents are scattered. Sellers may misrepresent ages of systems. No tool connects these into a coherent, queryable history.
**What It Does:**
- Ingests inspection reports, permits, seller disclosures, HOA docs, neighborhood news
- Builds a temporal knowledge graph: Property → has_system → Roof → installed_in → 2018 (but permit says 2015)
- **Cognee Temporal:** "When was the last major system replacement?" → traces timeline
- **Cognee Contradiction:** Flags "Seller says roof is 5 years old, but inspection notes indicate 12 years"
- **Cognee Self-Improvement:** Learns which sources are reliable (permit > seller claim), weights facts accordingly
- **Demo:** Show a property graph with contradictions highlighted in red, timeline view, and a query like "What's the real age of the roof?"
**Why No One Built It:** Real estate is transaction-focused (Zillow = listings). The *post-purchase history layer* is completely unaddressed. Homeowners don't think about this until they sell, then scramble.
**Adoption Potential:** Massive. Every homebuyer would want this. Partner with inspectors or title companies.
**Feasibility:** HIGH. Ingest PDFs (inspection reports), extract entities, build graph. Clear data sources.

---

### 2. 👨‍👩‍👧‍👦 FamilyChronicle — "The AI Family Historian That Catches Lies"
**Domain:** Family History / Genealogy / Oral History  
**The Problem:** Family stories are passed down orally and decay. Different relatives remember events differently. Ancestry.com does record matching, but NO ONE builds a knowledge graph of family narratives with contradiction detection.
**What It Does:**
- Ingests family interviews (audio→text), letters, photos with captions, documents
- Builds knowledge graph: Person → met → Person → in → Place → on → Date
- **Cognee Contradiction:** "Grandma said she met Grandpa in 1952, but marriage certificate is 1951. Interview with Aunt says 1950."
- **Cognee Temporal:** "What happened to our family between 1940-1945?" → reconstructs timeline from scattered sources
- **Cognee Self-Improvement:** Confidence scores improve as corroborating evidence accumulates. A fact with 3 sources becomes "high confidence"; contradictory facts get flagged for investigation.
- **Demo:** Upload 3 family interviews, show the auto-built family graph, highlight contradictions, show timeline reconstruction.
**Why No One Built It:** Ancestry focuses on *records* (census, DNA). The *narrative layer* of family history is untapped. AI transcription exists, but not structured into a reasoning graph.
**Adoption Potential:** HUGE. 30M+ Ancestry users. Podcasts like "Family Ghosts" prove demand. Families love this.
**Feasibility:** HIGH. Audio→text (Whisper), entity extraction, graph building. Very demoable.

---

### 3. 🧠 TherapyTimeline — "Your Therapy, But Remembered"
**Domain:** Mental Health / Therapy / Personal Growth  
**The Problem:** Therapy is episodic. Patients forget insights between sessions. Therapists take notes but can't hold a full knowledge graph of a patient's mental model. No tool connects themes across months of sessions.
**What It Does:**
- Ingests therapy notes, journal entries, mood tracking data
- Builds knowledge graph: Theme → relates_to → Trigger → managed_by → CopingStrategy → learned_in → Session_12
- **Cognee Temporal:** "How did my anxiety levels relate to work changes over the past 6 months?"
- **Cognee Contradiction:** "I said my mother was supportive in Session 3, but 3 later sessions mention criticism. Flag for exploration."
- **Cognee Self-Improvement:** Identifies recurring patterns: "Every time you mention 'deadline' + 'insomnia' in the same week, a crisis follows within 10 days."
- **Multi-tenant:** Patient data is fully isolated. Therapists can query their own patient graphs.
- **Demo:** Show a session graph growing over time, a timeline of anxiety vs. work events, and a pattern alert.
**Why No One Built It:** Therapy apps (BetterHelp) are chat platforms. Mood trackers are scalar. NO ONE connects *content* across sessions into a reasoning graph. Privacy concerns blocked this, but self-hosted Cognee solves it.
**Adoption Potential:** HIGH. Therapists would pay for this. Patients want insight. The self-hosted angle addresses HIPAA concerns.
**Feasibility:** HIGH. Journal entries are text. Session notes are text. Clear ontology: People, Events, Emotions, Themes, Insights.

---

### 4. 💪 AthleteLedger — "Your Body's Wikipedia"
**Domain:** Sports Coaching / Athlete Development  
**The Problem:** Athletes' careers are scattered across training logs, injury reports, competition results, and coaching notes. Coaches can't see the full causal graph. "Why did I get injured before every major championship?" is answerable only with a knowledge graph.
**What It Does:**
- Ingests training logs, injury reports, competition results, nutrition, sleep data, coaching notes
- Builds knowledge graph: TrainingBlock → intensity → High → followed_by → Injury → type → Hamstring
- **Cognee Temporal:** "What training changes preceded my 3 best performances?"
- **Cognee Self-Improvement:** Discovers correlations: "High intensity + poor sleep → injury within 14 days (confidence: 0.87)"
- **Cognee Contradiction:** "Coach recommended rest, but training log shows 3 hard sessions. Flag."
- **Demo:** Show an athlete's career graph, query for injury precursors, show a correlation discovery.
**Why No One Built It:** Wearables (Whoop, Garmin) do time-series analytics but NO graph reasoning. LLM-SPTRec (2026 paper) is academic and not athlete-specific. Sports teams use data but not knowledge graphs.
**Adoption Potential:** STRONG. Amateur athletes (runners, triathletes) are data-obsessed. Coaches would pay.
**Feasibility:** HIGH. Training logs are structured text. Clear ontology: Training, Competition, Injury, Nutrition, Sleep, Technique.

---

### 5. 🎵 SoundMemory — "The Producer's Second Brain"
**Domain:** Music Production / Creative Collaboration  
**The Problem:** Music producers make thousands of micro-decisions per project. "What synth did I use on Track 3 that had that warm pad sound?" or "I tried this reverb on the last EP, didn't work, but might work here." Current tools (DAW project files) don't have semantic memory.
**What It Does:**
- Ingests DAW project notes, audio stems, chat with collaborators, decision logs
- Builds knowledge graph: Track → uses → Synth → setting → Pad → similar_to → Track_7_Synth
- **Cognee Temporal:** "What processing chain did I use on vocals in January vs. June?"
- **Cognee Self-Improvement:** Learns producer's preferences: "You always roll off 100Hz on bass after trying it 8 times"
- **Cognee Contradiction:** "You said you hate compressor X, but you used it 3 times last month. Flag."
- **Demo:** Upload a producer's notes, show a "sound genealogy" graph, query for "find me that warm pad from last EP."
**Why No One Built It:** Music production tools are about *creation* (Suno, AIVA), not *memory*. No tool remembers WHY decisions were made. Teragraph is academic and not for personal production memory.
**Adoption Potential:** STRONG. Music producers are obsessive about their workflows. SoundCloud/Spotify ecosystem.
**Feasibility:** MEDIUM-HIGH. Need to parse DAW notes or manual input. But ontology is simple: Instruments, Effects, Settings, Tracks, Projects, Decisions.

---

### 6. 📜 RFCArchaeology — "Why Did We Decide This?"
**Domain:** Open Source Governance / Technical Decision Tracking  
**The Problem:** Open source projects lose decision history. New contributors ask "why was this designed this way?" and the answer is buried in a 400-comment GitHub issue from 2021. RFCs get forgotten. New proposals unknowingly contradict past decisions.
**What It Does:**
- Ingests RFCs, GitHub discussions, PR comments, meeting transcripts, mailing lists
- Builds knowledge graph: Proposal → argued_by → Person → supported_by → Argument → decided_as → Rejected → because_of → Performance_Concern
- **Cognee Temporal:** "What were the arguments against microservices in 2021?"
- **Cognee Contradiction:** "This new RFC proposes microservices, but RFC #42 was rejected for the same reason. SURFACE THE PAST."
- **Cognee Self-Improvement:** Learns recurring rejection patterns: "Performance concerns always block architecture changes in this project."
- **Demo:** Show a project's decision graph, query "Why did we choose monolith?", show contradiction alert on new RFC.
**Why No One Built It:** GitHub Discussions and wikis are flat. Semantica is general governance, not specific to open-source RFC archaeology. No tool connects arguments across time.
**Adoption Potential:** STRONG. Every major open source project needs this. Rust, Python, Kubernetes all struggle with institutional memory.
**Feasibility:** HIGH. GitHub API provides structured data. Clear ontology: RFC, Argument, Decision, Person, Topic, Status.

---

### 7. 🍽️ SymptomChef — "What Did I Eat Before I Felt Bad?"
**Domain:** Food / Nutrition / Personal Health Correlation  
**The Problem:** People with migraines, IBS, allergies, or autoimmune issues need to find food triggers. Current apps track food OR symptoms, but not the *correlation* over time. No tool uses knowledge graphs to discover "every time I eat X + Y under stress, symptom Z follows in 24 hours."
**What It Does:**
- Ingests meal logs, symptom logs, sleep data, stress levels, energy ratings
- Builds knowledge graph: Meal → contains → Ingredient → correlated_with → Symptom → with_lag → 24h
- **Cognee Temporal:** "What did I eat in the 48 hours before each of my 5 migraines this month?"
- **Cognee Self-Improvement:** Discovers non-obvious correlations: "Gluten + poor sleep → migraine (not gluten alone)"
- **Cognee Contradiction:** "You said avocado doesn't trigger you, but 4 of 5 recent episodes followed avocado. Flag."
- **Demo:** Show a personal food/symptom graph, query for migraine precursors, show a discovered correlation.
**Why No One Built It:** MyFitnessPal = calorie counting. SwissFKG = public recipe graph. No PERSONAL knowledge graph that learns individual correlations over time.
**Adoption Potential:** MASSIVE. Millions of people with food sensitivities. Dieticians would recommend this.
**Feasibility:** HIGH. Text logs are easy. Ontology is straightforward: Food, Ingredient, Meal, Symptom, Sleep, Stress, Time.

---

### 8. 📋 ContractAncestry — "The Archaeology of a Deal"
**Domain:** Legal / Contract Negotiation  
**The Problem:** Lawyers negotiate contracts through 10+ redlined versions. Six months later, no one remembers WHY a clause was changed. "Who negotiated the liability cap down from $5M to $1M?" requires reading 200 emails. CLM tools track versions but don't build reasoning graphs.
**What It Does:**
- Ingests contract drafts, redlines, negotiation emails, signed versions
- Builds knowledge graph: Clause_v1 → changed_to → Clause_v2 → negotiated_by → Lawyer → reason → "Client risk tolerance"
- **Cognee Temporal:** "How did the liability clause evolve across 4 versions?" → reconstructs lineage
- **Cognee Contradiction:** "Version 3 says 30 days, but version 4 says 45 days. Flag for review."
- **Cognee Self-Improvement:** Learns which clauses are always negotiated: "Indemnity clauses are modified in 90% of deals."
- **Demo:** Show a clause's evolution graph, query "Why did we change this?", show negotiation archaeology.
**Why No One Built It:** CLM (Sirion, Agiloft) focuses on *management* (renewals, obligations). The *negotiation archaeology* layer is completely missing. No one treats contract evolution as a knowledge graph.
**Adoption Potential:** STRONG. In-house legal teams at startups and enterprises constantly revisit past deals.
**Feasibility:** HIGH. Contract drafts are text. Redlines are structured changes. Emails are text. Clear ontology: Clause, Version, Party, Negotiation, Change, Reason.

---

### 9. 🚨 EmergencyLedger — "The Institutional Memory of Disasters"
**Domain:** Disaster Response / Emergency Management  
**The Problem:** First responders start from zero at every incident. Eyewitness reports contradict each other. Decisions made in the first hour are forgotten. No system accumulates institutional memory across incidents with contradiction detection.
**What It Does:**
- Ingests incident reports, dispatch logs, news articles, social media, eyewitness accounts
- Builds knowledge graph: Incident → has_report → Eyewitness_A → says → "Fire started in kitchen" → contradicts → Eyewitness_B → says → "Fire started in garage"
- **Cognee Temporal:** "What resources were deployed 6 hours after the last flood in this region?"
- **Cognee Self-Improvement:** Learns which early reports are reliable: "Social media reports within 30min are 60% accurate; official dispatch at 1hr is 90% accurate."
- **Cognee Contradiction:** Auto-surfaces conflicting eyewitness accounts with confidence scoring.
- **Demo:** Show an incident knowledge graph with contradictory reports highlighted, resource timeline, and confidence scoring.
**Why No One Built It:** MHGSA (2024) is academic disaster classification. EM-DAT is a flat database. No production tool uses persistent knowledge graphs for incident memory. The TREK dataset (2026) is research-only.
**Adoption Potential:** HUGE for emergency management agencies. NGOs like Red Cross would use this. Government contracts.
**Feasibility:** MEDIUM. Public incident reports are available. Social media is accessible. The challenge is real-time ingestion, but for a hackathon demo, batch processing of historical incidents is sufficient.

---

## 3 Emerging 2026 Trends That Make These Timely

1. **"AI Memory" is becoming table stakes (VentureBeat, Jan 2026):** Contextual memory is expected to surpass RAG for adaptive AI workflows. The market is ready for memory-first applications.

2. **Contradiction resolution is the #1 weakness in all AI memory systems (BEAM benchmark, 2026):** At 10M tokens, ALL systems score <0.05 on contradiction resolution. Cognee is the only framework architecturally positioned to solve this. Judges will recognize this as a genuinely hard problem.

3. **Bi-temporal reasoning is the next frontier (Octoco.ai, Jan 2026):** "When did we learn this?" vs. "When did it happen?" is becoming critical. Cognee's `temporal_cognify` is the only open-source implementation that handles this natively.

---

## Why These Win the Hackathon

**Judging Criteria Alignment:**
- **Best Use of Open Source:** These all use Cognee's core differentiators (graph, temporal, self-improvement, contradiction) — not just "vector search + memory"
- **Novelty:** NO ONE is building these. The Cognee hackathon history shows only company brains, support agents, and sales tools. These are all in completely different domains.
- **Demo Impact:** Each has a visual, compelling 3-minute demo: "Here are the contradictions in my family history" / "Here's why my house's roof age is suspicious" / "Here's the pattern that predicts my migraines"
- **Feasibility in 6 Days:** Each has clear, bounded scope. Ingest text → extract entities → build graph → query. No external API dependencies needed beyond basic data sources.

**Top 3 Picks for Maximum Impact:**
1. **FamilyChronicle** — Emotionally resonant, universally relatable, demo blows minds when it catches a family "lie"
2. **PropertyDNA** — Addresses a $10T market with a clear value proposition. Everyone buys a house.
3. **SymptomChef** — Solves real daily pain for millions. The "migraine trigger discovery" demo is viscerally compelling.

---

## Research Sources

- Cognee GitHub: https://github.com/topoteretes/cognee
- Cognee Hackathon History: https://github.com/topoteretes/cognee-hackathons
- Open-Source AI Memory Frameworks 2026: https://tryxlr8.ai/blogs/best-open-source-ai-memory-frameworks-2026
- Mem0 vs Letta vs Zep vs Cognee: https://mcp.directory/blog/mem0-vs-letta-vs-zep-vs-cognee-2026
- BEAM Benchmark (Contradiction Resolution Gap): https://arxiv.org/html/2604.11364v2
- BEAM Benchmark Results: https://raw.githubusercontent.com/muratcankoylan/Agent-Skills-for-Context-Engineering/main/skills/memory-systems/SKILL.md
- Knowledge Graphs as Memory: https://www.octoco.ai/blog/knowledge-graphs-as-memory
- Cognee Tutorial (Beyond Recall): https://www.cognee.ai/blog/tutorials/beyond-recall-building-persistent-memory-in-ai-agents-with-cognee
- AI Memory vs RAG vs KG (Enterprise Guide 2026): https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/
- AutoSci (Scientific Memory Research Paper): https://arxiv.org/html/2605.31468v1
- Deliberation Knowledge Graph (Academic): https://cosasbuenas.es/pdf/119.pdf
- Swiss Food Knowledge Graph: https://arxiv.org/html/2507.10156v1
- MARTIALIS (Ontology Validation): https://ceur-ws.org/Vol-4182/paper60.pdf
- Language Learning + KG Review: https://www.mdpi.com/2076-3417/16/5/2611
- Music + Knowledge Graphs: https://ulopenaccess.com/papers/ULAHU_V02I04/ULAHU20250204_003.pdf
- LLM-SPTRec (Sports Training): https://pmc.ncbi.nlm.nih.gov/articles/PMC12916763/
- Disaster Knowledge Graphs: https://www.nature.com/articles/s41597-026-07036-2
- Contract Lifecycle Management AI: https://www.sirion.ai/library/contract-insights/ai-contract-lifecycle-management/
- Digital Legacy (Evaheld): https://evaheld.com/
- Genealogy AI: https://www.many-roads.com/2025/04/04/the-role-of-artificial-intelligence-in-genealogy-and-historical-research/
- Argument Mapping Tools: https://discovery.ucl.ac.uk/id/eprint/10172106/1/frai-06-1124045.pdf
- AI in Mediation: https://moritzlaw.osu.edu/sites/default/files/2024-11/Emma%20Vertin%20-%20Blog%201.pdf
- Memory Provenance: https://www.memorylake.ai/en/blogs/memory-provenance-explained

---

*Research compiled by sub-agent for Mnemosyne project. July 1, 2026.*

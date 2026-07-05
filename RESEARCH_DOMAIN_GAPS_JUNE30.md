# Domain Gap Analysis for Cognee-Powered Novel Solutions
**Research Date:** July 1, 2026 (CEST)  
**Hackathon Context:** The Hangover Part AI (Cognee x WeMakeDevs, June 29 - July 5, 2026, $10,000 prize)  
**Researcher:** Sub-agent research for Mnemosyne project  
**Goal:** Identify genuinely novel opportunities where Cognee's unique features (graph + self-improvement + temporal + ontology + contradiction detection) could create solutions that NO existing tool currently provides.

---

## Domain 1: Argument Mapping / Fact-Checking / Debate Tools

### 1.1 Existing Tools (with descriptions)

| Tool | Description | AI? | Knowledge Graph? | Memory? | Self-Improve? |
|------|-------------|-----|------------------|---------|---------------|
| **Kialo** | Platform for rational debate with tree structures (19,000+ debates, 724,000+ arguments). Each node is a textual argument with pro/con branches, voting, and history tracking. | NO | NO (tree structure only, no semantic graph) | Partial (edit history, votes) | NO |
| **Kialo Edu** | Education version for classroom debates and assessment. | NO | NO | Partial | NO |
| **DebateGraph** | Visual debate mapping as directed graphs with claims, questions, evidence as linked nodes. Shareable and collaborative. | NO | Partial (visual graph, but no semantic reasoning) | NO | NO |
| **Argunet** | Open-source argument mapping (discontinued as of 2025). | NO | NO | NO | NO |
| **PolitiFact** | Human journalist fact-checking with "Truth-O-Meter" ratings. | NO (human-driven) | NO | NO (archived articles, no live graph) | NO |
| **Snopes** | Human fact-checking urban legends and misinformation. | NO (human-driven) | NO | NO | NO |
| **FactCheck.org** | Human political fact-checking by Annenberg Center. | NO (human-driven) | NO | NO | NO |
| **Ground News** | Aggregates news coverage from across the political spectrum. | Partial (coverage analysis) | NO | NO | NO |
| **AllSides** | Media bias ratings and balanced news coverage. | Partial (bias analysis) | NO | NO | NO |
| **NewsGuard** | Trust ratings for news websites based on journalistic criteria. | Partial (automated + human) | NO | NO | NO |
| **ArguNet (research model)** | Neural architecture for argumentative relation classification in online debates. Uses Dialogue Acts and context encoding. | YES (ML model) | Partial (graph-like Bipolar Argumentation Graph encoding) | NO (single-session inference) | NO |
| **ClaimsKG** | Knowledge graph of fact-checked claims from fact-checking websites with truth values, authors, dates, metadata. | Partial (semi-automated pipeline) | YES (RDF knowledge graph) | NO (static, not self-updating) | NO |
| **Carneades** | Online tool for generating and reasoning with argument graphs (4 versions, open-source). | NO | Partial (argument graph) | NO | NO |
| **TOAST** | Online ASPIC+ implementation for structured argumentation. | NO | Partial | NO | NO (discontinued) |
| **DAMN / Arg&Dec** | Multi-agent decision-making tools with argumentation. | NO | Partial | NO | NO |
| **ArguCast** | Tool for human predictions about future events with arguments linked via supports/attacks, votes, and forecasts. Filters irrational users using gradual semantics. | Partial (semantics filtering) | Partial (argument graph) | NO | NO |
| **CISpaces** | Military intelligence analysis combining argumentation, provenance, and crowdsourcing. Evaluated to improve analysts' daily activities. | Partial (AI + human) | Partial (provenance + argumentation) | NO | NO |
| **YabAI, Parley, Consensus** | AI-assisted debate preparation, multiplayer civic debates, literature search for evidence. | Partial | NO | NO | NO |
| **FactAgent** | LLM agent for fake news detection using expert workflows with tools (standing tool, URL tool, search tool). | YES (LLM agent) | NO | NO (session-based) | NO |

### 1.2 What They CANNOT Do (The Gap)

- **NO temporal reasoning:** No tool tracks how arguments evolve over time, how evidence shifts, or how a claim's strength changes as new information emerges.
- **NO contradiction detection across sessions:** Kialo votes within a debate, but no system detects when a user contradicts themselves across 10 different debates, or when a fact-check from 2023 is contradicted by new evidence in 2026.
- **NO self-improving knowledge graph:** ClaimsKG is static. No system learns that certain types of claims are frequently false, or that certain sources consistently contradict each other, and builds an ontology from that.
- **NO memory across debates:** Each debate is an isolated silo. No tool remembers that Argument A in Topic X was defeated by Evidence B, and applies that learning to Topic Y where the same argument appears.
- **NO ontology-driven reasoning:** No tool can classify arguments by type (e.g., "slippery slope", "appeal to authority") and reason about their validity across domains using a formal ontology.
- **NO cross-source verification:** Fact-checkers check individual claims against sources, but no tool builds a graph connecting all claims, sources, and their contradictions into a single, queryable knowledge base.

### 1.3 The Cognee Opportunity

**"Chronicle" — A Self-Improving Argument Knowledge Graph**

- Build a knowledge graph where every claim, evidence, source, and fact-check is a node.
- Use Cognee's temporal reasoning to track how argument strength changes as new evidence is added.
- Use contradiction detection to flag when a source contradicts itself across time, or when two "trusted" sources make incompatible claims.
- Use ontology to classify argument types and automatically identify logical fallacies.
- The graph self-improves: when a claim is repeatedly debunked, the system learns to flag similar claims faster in new debates.
- **Novelty:** This is NOT just "Kialo with AI." It is a persistent, cross-domain argument memory that no existing tool provides.

---

## Domain 2: Mediation / Negotiation / Dispute Resolution Tools

### 2.1 Existing Tools (with descriptions)

| Tool | Description | AI? | Knowledge Graph? | Memory? | Self-Improve? |
|------|-------------|-----|------------------|---------|---------------|
| **Modria (Tyler Technologies)** | "World's most successful ODR platform." Processes 2M+ digital disputes/year. Uses decision trees + NLP for diagnosis, negotiation, mediation, and arbitration modules. Semi-automated, widely used in municipal courts. | Partial (decision trees, NLP) | NO (rule-based logic) | NO (case-by-case, no cross-case learning) | Partial (learns from resolved disputes, but no graph) |
| **Smartsettle** | Multi-criteria decision analysis and visual negotiation. Uses optimization algorithms and game theory to find "win-win" solutions. Fully automated. Analyzes preferences and suggests optimal solutions dynamically. | YES (optimization, game theory) | NO | NO (single negotiation session) | Partial (learns user preferences within a session) |
| **Cybersettle** | Insurance claim negotiation software. Processes 18,000 digital settlements/day. | Partial (automated negotiation) | NO | NO | NO |
| **Kleros** | Blockchain-based dispute resolution with crowdsourcing and probabilistic voting. For smart contract disputes. | Partial (blockchain + crowdsourcing) | NO (blockchain ledger, not semantic graph) | NO | NO |
| **eBay/PayPal ODR** | Rule-based logic + NLP for buyer-seller conflicts. Highly automated, 400M+ disputes resolved historically. | Partial (rule-based + NLP) | NO | NO | NO |
| **Alibaba ODR** | NLU and modeling for B2B disputes. Fully automated. | Partial (NLU) | NO | NO | NO |
| **FairClaims** | AI-powered legal chatbots for customer inquiry response. | Partial (chatbots) | NO | NO | NO |
| **Immediation** | Multilingual virtual mediation (45 languages). | NO | NO | NO | NO |
| **Matterhorn (Court Innovations)** | Online court dispute resolution. | NO | NO | NO | NO |
| **Youstice** | Semantic AI + pattern recognition for retail disputes. Discontinued EU pilot. | Partial (semantic AI) | NO | NO | NO |
| **OurFamilyWizard** | Co-parenting coordination platform with AI dispute prevention. | Partial (AI prevention) | NO | NO | NO |
| **Family Winner** | Game theory + decision theory for negotiation facilitation. | Partial (game theory) | NO | NO | NO |
| **Resolve (UK/EU)** | AI case management + email analytics for consumer services. | Partial (AI case management) | NO | NO | NO |
| **Arbilex / LexiMediate / Risolv / eJust** | Various online arbitration and mediation platforms. | NO | NO | NO | NO |
| **NewGenesis / Caseload** | Court and tribunal ODR systems. | NO | NO | NO | NO |
| **UK Courts & Tribunals Service** | Online divorce, probate, small claims, traffic appeals. | NO | NO | NO | NO |
| **Estonia AI ODR** | AI-based system for claims up to EUR 7,000. | Partial (AI) | NO | NO | NO |

### 2.2 What They CANNOT Do (The Gap)

- **NO cross-case pattern memory:** Modria "learns from resolved disputes" but does not build a knowledge graph of negotiation patterns. A landlord-tenant dispute in Berlin and one in Tokyo are unrelated in the system, even if they share identical fact patterns.
- **NO temporal reasoning about dispute evolution:** No system tracks how a dispute type has evolved over time (e.g., how Airbnb dispute patterns changed from 2019 to 2025), or how legal precedent has shifted, to predict optimal settlement strategies.
- **NO contradiction detection in party positions:** No tool detects when a party contradicts their own position in a negotiation, or when their current claim contradicts their claims in a previous dispute.
- **NO ontology of dispute types:** No system classifies disputes by domain ontology (e.g., "consumer fraud" → "e-commerce" → "digital goods" → "non-delivery") and applies proven resolution strategies from similar cases.
- **NO memory of what works:** If a particular mediation strategy succeeded in 100 similar cases, no system remembers that and proactively recommends it. Each case is treated as isolated.
- **NO emotional/personal pattern tracking:** In family mediation, no system tracks recurring conflict patterns across sessions (e.g., one party always escalates when a specific topic is raised) to prepare the mediator.

### 2.3 The Cognee Opportunity

**"Mnemosyne Mediator" — A Dispute Resolution Knowledge Graph with Memory**

- Build a temporal knowledge graph of disputes, parties, claims, outcomes, and strategies.
- Use Cognee's ontology to classify disputes by type, jurisdiction, and fact pattern.
- Use temporal reasoning to track how dispute resolution effectiveness changes over time (e.g., certain mediation techniques become less effective as parties become more sophisticated).
- Use contradiction detection to flag when a party's position is inconsistent with their own prior statements, or with legal precedent.
- The graph self-improves: successful mediation strategies are linked to dispute types, and the system recommends proven strategies based on subgraph matching.
- **Novelty:** No ODR platform has a persistent, cross-case memory. Modria handles volume; this would handle *pattern*.

---

## Domain 3: Investigative Journalism / Document Analysis Tools

### 3.1 Existing Tools (with descriptions)

| Tool | Description | AI? | Knowledge Graph? | Memory? | Self-Improve? |
|------|-------------|-----|------------------|---------|---------------|
| **Aleph (OCCRP)** | Document and entity search platform for investigative journalists. Extracts entities, links documents, enables cross-referencing. | Partial (entity extraction) | Partial (entity-document links) | NO (search index, no persistent reasoning) | NO |
| **i2 Analyst's Notebook (IBM)** | Link analysis and data visualization for intelligence and law enforcement. Visual network analysis. | NO (manual link analysis) | Partial (visual network) | NO | NO |
| **Palantir** | Data integration and analysis platform for government/intelligence. Expensive, proprietary. | YES (advanced analytics) | Partial (entity resolution) | Partial (persistent data) | Partial (model updates) |
| **DocumentCloud** | Document hosting, annotation, and OCR for journalists. | Partial (OCR) | NO | NO | NO |
| **PANDA** | Alerts for new documents matching journalist queries. | Partial (alerting) | NO | NO | NO |
| **CISpaces** | Military intelligence analysis tool combining argumentation, provenance, and crowdsourcing. | Partial (AI + argumentation) | Partial (provenance graph) | NO | NO |
| **HADSS (Hypermedia Argumentation DSS)** | Graphical representation tool for argument-based decision support. | NO | Partial (argument graph) | NO | NO |
| **arguEIRA** | Argumentation-based justification for clinical anomaly detection. | Partial (argumentation) | NO | NO | NO |
| **REACT (Risks/Events/Action/Consequences)** | Medical planning support with argumentation. | NO | NO | NO | NO |
| **Graal / DAGGER / NAKED** | Argument generation tools for knowledge bases with existential rules. | NO | Partial (rule-based graph) | NO | NO |
| **Gorgias** | General argument-based expert decision tool for multiple domains. | Partial (argumentation engine) | NO | NO | NO |
| **Cities Knowledge Graph (CANES/SIC)** | Urban knowledge graph projects for city data analysis. | Partial (graph construction) | YES | NO | NO |
| **Blazegraph / RDF-GAS API** | Graph database tools for RDF analysis. | NO | YES (database) | NO | NO |
| **SAsSy** | Visual explanation of complex plans through argumentation. | NO | Partial | NO | NO |
| **Article 6 Predictor (ECtHR)** | Predicts European Court of Human Rights case outcomes using ADF frameworks. 97% accuracy. | YES (H-BERT + ADF) | Partial (argument framework) | NO | NO |
| **Collemette et al. Legal Prediction** | Machine learning models for legal case reasoning using H-BERT and argumentation. | YES (ML) | NO | NO | NO |

### 3.2 What They CANNOT Do (The Gap)

- **NO temporal document graph:** No tool builds a temporal knowledge graph where documents, entities, events, and claims are connected with time-evolving relationships. A document from 2015 mentioning Person X is not linked to a document from 2024 where Person X appears in a different context, unless a journalist manually connects them.
- **NO contradiction detection across sources:** Investigative journalists manually cross-reference sources. No tool automatically detects when Source A says Person X was in Location Y on Date Z, but Source B says Person X was in Location W on the same date — and flags this as a contradiction requiring investigation.
- **NO self-improving hypothesis generation:** No tool learns from past investigations. If 10 previous corruption investigations followed the pattern "Company A → Shell Company B → Politician C → Policy D", the system does not recognize this pattern and suggest it as a hypothesis in a new investigation with similar starting points.
- **NO persistent investigation memory:** Each investigation is a project. When it ends, the insights are lost (or archived as a report). No system maintains a persistent knowledge graph that grows with each investigation, making cross-investigation insights possible.
- **NO ontology-driven entity resolution:** Aleph does entity extraction, but no tool uses a formal ontology to reason that "Company X" in Document A is the same entity as "Subsidiary X" in Document B because of a corporate relationship defined in the ontology.
- **NO argumentation + evidence graph:** CISpaces combines argumentation and provenance, but it's military-focused, not available for journalism, and has no temporal or self-improving capabilities.

### 3.3 The Cognee Opportunity

**"Mnemosyne Investigator" — A Self-Improving Investigation Knowledge Graph**

- Build a temporal knowledge graph where documents, entities, events, claims, and sources are all nodes with time-stamped relationships.
- Use contradiction detection to automatically flag conflicting statements across documents (e.g., two sources claiming different locations for the same person at the same time).
- Use ontology to define entity types (Person, Corporation, Shell Company, Political Party, Policy) and their relationships, enabling automated hypothesis generation.
- The graph self-improves: successful investigation patterns are retained, and the system suggests similar patterns in new investigations (e.g., "this network resembles the Panama Papers pattern").
- Use temporal reasoning to track how entity relationships change (e.g., "Person X was CEO of Company Y until 2020, then became advisor to Government Z").
- **Novelty:** Palantir is expensive and analyst-driven. Aleph is search-driven. This would be *pattern-driven*, with persistent memory across investigations.

---

## Domain 4: Civic Engagement / City Decision Tracking / Government Transparency

### 4.1 Existing Tools (with descriptions)

| Tool | Description | AI? | Knowledge Graph? | Memory? | Self-Improve? |
|------|-------------|-----|------------------|---------|---------------|
| **OpenGov** | Public sector ERP platform for 1,600+ governments. Budgeting, procurement, permitting, CRM, 311, capital projects. "OG Assist" AI feature. | Partial (OG Assist AI) | NO (relational database) | NO (transactional records) | NO |
| **SeeClickFix** | 311 service request platform. 1M+ users, 300+ local governments. Users report issues (potholes, etc.) with photos and GPS. Civic Points gamification. | Partial (point-of-interest notifications) | NO | NO (individual issue tracking) | NO |
| **MuckRock** | FOIA request filing and tracking platform. Tracks request status, response times, success rates by agency. | NO | NO (request database) | NO (archived requests) | NO |
| **Pol.is** | Open-source platform for large-scale deliberation. Uses machine learning to map opinions and surface consensus. Used in Taiwan (vTaiwan), UK, Finland, UN. Now includes LLM summarization. | YES (ML + LLM) | Partial (opinion clusters) | NO (per-conversation) | NO |
| **vTaiwan** | Combines Pol.is + Discourse for online-offline consultation. 80% of 26 discussed issues led to decisive government action. | Partial (Pol.is backend) | NO | NO | NO |
| **Cofacts** | Collaborative fact-checking chatbot by g0v Taiwan. Community-driven editorial process for viral misinformation. | Partial (chatbot + crowdsourcing) | NO | NO | NO |
| **Disfactory** | Crowdsourced illegal factory reporting using GIS. 4,200+ reports feeding into regulatory enforcement. | NO (GIS mapping) | Partial (geographic data) | NO | NO |
| **g0v.tw** | Decentralized civic tech community. Tools like MoeDict, Cofacts, Disfactory. | Partial (various tools) | NO | NO | NO |
| **Loomio** | Collaborative decision-making platform for groups. | NO | NO | NO | NO |
| **Ushahidi** | Open-source crowdsourcing and crisis-mapping platform. Used in 159 countries. | NO | Partial (geographic mapping) | NO | NO |
| **BudgIT** | Fiscal transparency across 6 African countries. Tracka (project monitoring), Govspend, BIMI (AI-powered public finance assistant). | Partial (BIMI AI) | NO | NO | NO |
| **Mzalendo / Odekro** | Parliamentary monitoring (Kenya, Ghana). MP scorecards, attendance, legislative activity. | NO | NO | NO | NO |
| **OpenUp (South Africa)** | Vulekamali (budget portal), Wazimap (demographic explorer), PMG (parliamentary monitoring). | NO | NO | NO | NO |
| **They Vote For You / Right To Know (OpenAustralia)** | Parliamentary voting tracking and FOI tools. | NO | NO | NO | NO |
| **PlanningAlerts** | 5M+ alerts for development applications near users. | NO | Partial (geographic matching) | NO | NO |
| **e-People (South Korea)** | E-petitioning, citizen proposals, policy discussions across 303 government orgs. | NO | NO | NO | NO |
| **Gwanghwamoon 1st Street** | Online citizen participation platform for national government. | NO | NO | NO | NO |
| **Code for Japan / Code for Africa** | Civic tech communities with dozens of local projects. | Partial (various) | NO | NO | NO |
| **Open Data Portals (88 countries)** | ~1.19 million open datasets published as of 2019. | NO | NO | NO | NO |
| **OpenRecords / Request Tracker** | Various government FOIA/open records platforms. | NO | NO | NO | NO |
| **City Council Tracking (various)** | Local government meeting trackers, agendas, minutes. | NO | NO | NO | NO |

### 4.2 What They CANNOT Do (The Gap)

- **NO decision evolution tracking:** OpenGov tracks budgets, but no tool tracks how a specific decision (e.g., "Build Highway X") evolved through proposals, votes, amendments, budget changes, and final outcome as a temporal graph. Citizens cannot query: "How did this decision change, and who influenced each change?"
- **NO contradiction detection in government claims:** No tool detects when a politician's statement in 2023 contradicts their vote in 2025, or when a city council's stated priority ("affordable housing") contradicts their budget allocation (0% for housing).
- **NO knowledge graph of civic issues:** SeeClickFix tracks individual issues, but no tool builds a knowledge graph connecting "pothole on Street A" → "water main break on Street A" → "construction permit for Street A" → "city council vote on Street A repairs" → all reported by the same 15 residents over 3 years.
- **NO memory of civic engagement patterns:** No tool learns that when a certain neighborhood reports 3+ issues, a city council vote on that area typically follows within 60 days, or that certain types of issues are always resolved faster in certain districts.
- **NO ontology of government processes:** No tool uses formal ontology to model that "Policy Proposal → Committee Review → Public Comment → Amendment → Vote → Budget Allocation → Implementation → Evaluation" is a standard workflow, and automatically tracks where any given proposal is in that workflow.
- **NO cross-platform integration:** Pol.is does opinion mapping, SeeClickFix does issue reporting, MuckRock does FOIA, OpenGov does budgets. No tool connects these into a single knowledge graph showing: "Citizens reported Issue X → Council voted Y → Budget Z allocated → FOIA request revealed W → Citizen opinion shifted."

### 4.3 The Cognee Opportunity

**"Mnemosyne Civic" — A Government Decision Knowledge Graph with Memory**

- Build a temporal knowledge graph of all civic activity: issues, votes, budgets, statements, FOIA requests, petitions, and citizen reports.
- Use ontology to model government processes (proposals, committees, votes, budgets, implementations) and automatically track proposal status.
- Use contradiction detection to flag when government actions contradict stated priorities, or when politicians contradict their past positions.
- Use temporal reasoning to track how issues evolve: "Issue reported 2023 → Study commissioned 2024 → Budget allocated 2025 → Construction started 2026 → Citizen complaint 2026."
- The graph self-improves: learns patterns like "Districts with 3+ water issues in 6 months typically get infrastructure funding within 12 months" and alerts citizens to expected timelines.
- **Novelty:** Not a "better SeeClickFix" or "better OpenGov." It is a *single persistent memory* that connects all civic tools and remembers everything.

---

## Domain 5: Family History / Genealogy / Legacy Preservation

### 5.1 Existing Tools (with descriptions)

| Tool | Description | AI? | Knowledge Graph? | Memory? | Self-Improve? |
|------|-------------|-----|------------------|---------|---------------|
| **Ancestry.com** | Largest genealogy database. 2023 launched "Ancestry AI Stories" — LLM-generated 200-400 word first-person narratives from photos + biographical data. No source citations. | YES (LLM for stories) | NO (record database, not semantic graph) | NO (individual trees, no cross-tree reasoning) | NO |
| **MyHeritage** | "Deep Nostalgia" — proprietary video diffusion model animates portraits with micro-movements (blinking, head tilts). No identity inference or provenance. | YES (video diffusion) | NO | NO | NO |
| **FamilySearch** | Free genealogy records from the LDS Church. Collaborative family tree building. | NO | NO (hierarchical tree) | NO | NO |
| **StoryCorps** | Oral history recording and preservation (nonprofit, NPR partnership). | NO | NO (audio archive) | NO | NO |
| **StoryWorth** | Subscription service for weekly family story prompts, compiled into books. | NO | NO (text collection) | NO | NO |
| **Find a Grave** | Cemetery records and memorials. | NO | NO | NO | NO |
| **WikiTree** | Collaborative genealogy with community standards. | NO | NO (collaborative tree) | NO | NO |
| **Geni** | Crowdsourced family tree building. | NO | NO | NO | NO |
| **GEDmatch** | DNA genealogy analysis and matching. | Partial (DNA algorithms) | NO | NO | NO |
| **23andMe / AncestryDNA** | DNA testing and ethnicity/relative matching. | Partial (DNA analysis) | NO | NO | NO |
| **Fold3** | Military records genealogy. | NO | NO | NO | NO |
| **Newspapers.com** | Historical newspaper archive for genealogy. | Partial (OCR) | NO | NO | NO |
| **Immigration records (Ellis Island, etc.)** | Ship manifests and immigration records. | NO | NO | NO | NO |
| **Family Tree Maker / Legacy Family Tree** | Desktop genealogy software. | NO | NO | NO | NO |
| **DNA Painter / chromosome mapping tools** | Visual chromosome mapping for DNA genealogy. | NO | Partial (visual mapping) | NO | NO |
| **RootsMagic / Gramps** | Open-source genealogy software. | NO | NO | NO | NO |
| **Family history / local historical societies** | Various regional archives and societies. | NO | NO | NO | NO |
| **AI genealogy tools (emerging 2024-2025)** | Various startups using LLMs for family narrative generation. | Partial (LLM) | NO | NO | NO |

### 5.2 What They CANNOT Do (The Gap)

- **NO medical reasoning across generations:** No tool connects family trees with medical ontologies to reason about inherited conditions, genetic risk patterns, or environmental health factors across generations. A tool could flag: "3 generations of males in this branch had heart conditions by age 50" → "suggest cardiovascular screening."
- **NO contradiction detection in genealogical claims:** Family trees are full of conflicting information (e.g., Census A says birth year 1890, Census B says 1892). No tool automatically detects these contradictions and reasons about which source is more reliable based on provenance and temporal context.
- **NO knowledge graph of family relationships:** Family trees are hierarchical parent-child structures, not knowledge graphs. No tool represents relationships as a semantic graph: "Person A worked at Company B in City C during Period D, which was owned by Person E who married Person F (A's cousin)."
- **NO temporal reasoning about family evolution:** No tool tracks how a family's socioeconomic status, location, or occupations changed over time as a graph, and connects those changes to historical events (e.g., "Family moved from rural to urban after the 1930 Dust Bowl").
- **NO self-improving narrative validation:** Ancestry AI Stories generates plausible but fictional narratives. No tool learns from user corrections ("Actually, the AI said my grandmother visited the World's Fair, but she never did") to improve future narrative generation for that family or others.
- **NO memory across family trees:** Each family tree is isolated. No tool connects the fact that "Family A's ancestor worked in the same factory as Family B's ancestor in 1910" to suggest a possible relationship or shared experience.
- **NO legacy reasoning:** No tool uses ontology to model what "legacy" means (e.g., values, skills, traditions, property, stories) and track how these are transmitted, transformed, or lost across generations.

### 5.3 The Cognee Opportunity

**"Mnemosyne Legacy" — A Family Knowledge Graph with Temporal & Medical Reasoning**

- Build a knowledge graph where family members, events, locations, occupations, documents, photos, and DNA segments are all connected nodes with temporal edges.
- Use contradiction detection to flag conflicting genealogical records and reason about source reliability (e.g., "Birth certificate is more reliable than census for birth year").
- Use medical ontology to connect family health patterns across generations and generate health risk hypotheses (e.g., "3 generations of early-onset diabetes in this maternal branch").
- Use temporal reasoning to track family evolution against historical events ("Family moved from X to Y in 1847 during the Irish famine").
- The graph self-improves: when users correct AI-generated narratives, the system learns and improves. When new records are added, the graph automatically infers new relationships and flags contradictions with existing data.
- **Novelty:** Not "Ancestry with better AI." It is a *semantic family memory* that reasons about relationships, contradictions, health, and legacy across time. No existing tool does this.

---

## Summary: The 5 Domains Ranked by Most Promising Gap

| Rank | Domain | Gap Size | Cognee Fit | Novelty | Feasibility (5 days) | Why |
|------|--------|----------|------------|---------|---------------------|-----|
| **1** | **Domain 4: Civic Engagement** | **MASSIVE** | **Perfect** | **High** | **Medium** | No tool connects government decisions, citizen issues, FOIA requests, and opinions into a single temporal graph. Pol.is is opinion-only; SeeClickFix is issue-only; OpenGov is budget-only; MuckRock is FOIA-only. A Cognee-powered knowledge graph connecting ALL of these would be genuinely novel and highly relevant to the "community good" theme of hackathons. |
| **2** | **Domain 1: Argument Mapping** | **LARGE** | **Perfect** | **High** | **High** | Kialo and DebateGraph are visual-only. No tool has AI reasoning, contradiction detection, or cross-debate memory. ClaimsKG is the closest (static RDF graph of fact-checks) but has no temporal reasoning or self-improvement. A Cognee-powered argument graph with contradiction detection is a clear, achievable hackathon project. |
| **3** | **Domain 3: Investigative Journalism** | **LARGE** | **Strong** | **High** | **Medium** | Palantir is expensive, analyst-driven, and proprietary. Aleph is search-driven. No tool has persistent, self-improving cross-investigation memory. The gap is real but the domain is more specialized (fewer users than civic engagement). |
| **4** | **Domain 2: Dispute Resolution** | **MEDIUM** | **Good** | **Medium** | **Medium** | Modria and Smartsettle handle volume but have no cross-case pattern memory. The gap is real but the domain is heavily regulated (legal/mediation), making a hackathon prototype harder to demonstrate. |
| **5** | **Domain 5: Genealogy** | **MEDIUM** | **Good** | **Medium** | **High** | Ancestry and MyHeritage have AI features but no knowledge graphs. The gap is real but the market is saturated with large incumbents, and a hackathon prototype would struggle to show value without massive data integration. |

### Top 3 Recommendations for the Hackathon

1. **Civic Engagement (Domain 4)** is the strongest candidate because:
   - The gap is the most obvious and visually demonstrable.
   - Cognee's temporal + contradiction + graph features map perfectly to tracking government decision evolution.
   - A hackathon prototype can be built with publicly available data (city council agendas, SeeClickFix APIs, budget data).
   - It has clear social impact and aligns with the "community good" theme of most civic hackathons.
   - The name "Mnemosyne Civic" (or similar) fits the project's existing naming convention.

2. **Argument Mapping (Domain 1)** is the second strongest because:
   - The prototype is easiest to build (can use Kialo data, political debates, or fact-check datasets).
   - The value proposition is immediate: "Kialo shows you arguments; our tool shows you contradictions, argument patterns, and logical fallacies across ALL debates."
   - ClaimsKG provides a starting point for a knowledge graph of fact-checks.
   - The "Chronicle" name fits the temporal/historical aspect.

3. **Investigative Journalism (Domain 3)** is the third strongest because:
   - It has the highest technical sophistication potential, which judges often appreciate.
   - It leverages Cognee's most advanced features (temporal reasoning, entity resolution, hypothesis generation).
   - However, it requires more domain expertise to demonstrate value effectively in a hackathon setting.

---

## Research Sources
- ArgMining 2024 (ACL Anthology) — Kialo dataset analysis, ArguNet model
- Vesic & Yun, "Argumentation-based applications for decision-making" (Handbook of Formal Argumentation, 2024) — comprehensive tool survey
- Debate Software 2026 Review (Gitnux) — Kialo, DebateGraph, YabAI, Parley, Consensus comparison
- MarketResearchGuru Online Dispute Resolution Market Report (2026) — Modria, Smartsettle, Cybersettle market data
- AI in Mediation (OSU Moritz Law, 2024) — ODR and AI substantive vs. supportive approaches
- European ODR / ADR benchmarking studies (2024) — Modria, Smartsettle, Kleros, eBay ODR, Alibaba ODR feature comparison
- Gov.ong Civic Tech Field Guide — OpenGov, SeeClickFix, Pol.is, vTaiwan, MuckRock, g0v, Cofacts, BudgIT, Ushahidi
- OpenGov.com (2026) — platform capabilities and OG Assist AI
- Erhardt & Graeff — SeeClickFix civic technology study (2014)
- MuckRock FOIA tracking platform — agency response data
- OpenReview ArguNet paper (2024) — Bipolar Argumentation Graph, argument relation classification
- MyHeritage Deep Nostalgia vs. Ancestry AI Stories comparison (2024)
- AAAI 2025 — Debate on Graph (DoG) for knowledge graph reasoning
- AAAI 2025 — CognTKE (Cognitive Temporal Knowledge Extrapolation)
- arXiv 2025 — Cognee interface optimization for complex reasoning (Markovic)
- Slashdot Cognee comparisons (2026) — Cognee vs. CAMEL-AI, Head AI, Memories.ai
- Core.ac.uk / Uniupo — Fake news detection, ClaimsKG, PolitiFact/Snopes/GossipCop dataset analysis
- arXiv 2024 — FactAgent (LLM agent for fake news detection)
- CISpaces / Toniolo et al. — intelligence analysis with argumentation and provenance
- Cities Knowledge Graph (CANES, SIC, Cambridge) — urban knowledge graph research

---

*Research compiled July 1, 2026 for the Cognee x WeMakeDevs Hangover Part AI hackathon.*
*All data verified via web search, academic papers, and platform documentation retrieved in this session.*

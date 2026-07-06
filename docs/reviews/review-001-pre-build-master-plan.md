---
title: "Pre-Build Review: Master Plan and Decisions — Critical Gaps Found"
date: 2026-07-06
tags: [review, audit, planning, gaps, phase-0]
type: review
salience: 0.95
links: []
---

# Pre-Build Review: Master Plan and Decisions

**Reviewer:** Architect Session (self-review)
**Scope:** Master Plan v1.0, 4 Key Decisions, Code (`mo_graphify_memory.py`), and Process
**Status:** 🔴 CRITICAL ISSUES FOUND — Must fix before Phase 0 Builder Session

---

## EXECUTIVE SUMMARY

The Master Plan and decisions are sound in strategy but have **12 critical gaps and 8 code-level bugs** that must be addressed before spawning the Phase 0 Builder Session. Without these fixes, the builder session will produce flawed code that requires rework, wasting time and context.

**Recommendation:** Fix the plan and add a "Pre-Flight Checklist" to the Phase 0 prompt. Then spawn the builder session.

---

## PART 1: CRITICAL GAPS IN THE PLAN (Must Fix Before Phase 0)

### Gap 1: No `develop` Branch Exists on GitHub

**Severity:** 🔴 Critical
**Location:** Decision 002, Git Workflow Section
**Problem:** The plan assumes a `develop` branch exists. The repo currently only has `main`. The builder session will try to create `feature/phase-0-restructure` from `develop` and fail.
**Fix:** Add to Phase 0 tasks: `git checkout -b develop` and `git push origin develop`. Or change the workflow to branch from `main` for now and create `develop` after Phase 0 is stable.
**Recommendation:** Branch from `main` for Phase 0. Create `develop` after Phase 0 is merged.

### Gap 2: No Test Database Strategy Defined

**Severity:** 🔴 Critical
**Location:** Phase 0 Exit Criteria, Test Session
**Problem:** The plan says "Add pytest test suite (5-10 tests)" but doesn't specify how to test without a live PostgreSQL database. CI/CD (GitHub Actions) won't have PostgreSQL running. Tests will fail.
**Fix:** Add explicit strategy:
1. Use `pytest-postgresql` for ephemeral test databases in CI
2. Or use Docker Compose in CI (GitHub Actions `services:`)
3. Or mock `PgVectorStore` for unit tests and use integration tests only locally
**Recommendation:** Use GitHub Actions `services:` with PostgreSQL + pgvector Docker container. Add integration test markers (`pytest.mark.integration`). Unit tests mock the database.

### Gap 3: No `SKILL.md` Update Strategy

**Severity:** 🔴 Critical
**Location:** Repo Root, `SKILL.md`
**Problem:** After restructuring from `scripts/` to `mnemosyne/`, the `SKILL.md` references `scripts/mo_graphify_memory.py` and outdated paths. The builder session might not know to update it. Also, the `SKILL.md` references `test_report.md` (doesn't exist) and `memory_stack.docx` (large binary, shouldn't be in repo).
**Fix:** Add to Phase 0: "Update `SKILL.md` to reference new package paths. Remove `test_report.md` reference. Document `memory_stack.docx` as external document (not in repo)."

### Gap 4: No Module Splitting Map Provided to Builder

**Severity:** 🔴 Critical
**Location:** Phase 0 Builder Prompt
**Problem:** The builder prompt says "Split `mo_graphify_memory.py` into modules" but doesn't provide a mapping. The builder might make wrong decisions about what goes where, creating an inconsistent API.
**Fix:** Provide the exact module mapping in the Phase 0 prompt:
```
mnemosyne/
├── __init__.py          # Exports: UnifiedMemorySystem, MemoryMCPServer, autoload_memory
├── core.py              # UnifiedMemorySystem (main API class)
├── stores/
│   ├── __init__.py
│   └── postgres.py      # PgVectorStore
├── embedder.py          # Embedder
├── vault.py             # VaultManager
├── security.py          # AdmissionControl, SalienceEngine
├── prospective.py       # ProspectiveMemory
├── consolidation.py     # ConsolidationEngine
├── mcp_server.py        # MemoryMCPServer
└── cli.py               # CLI entry point (placeholder for Phase 3)
```

### Gap 5: `pyproject.toml` vs `setup.py` — Which One?

**Severity:** 🔴 Critical
**Location:** Phase 0 Tasks, Package Config
**Problem:** The plan says "Add `setup.py` or `pyproject.toml`" but doesn't specify which. Modern Python uses `pyproject.toml` (PEP 621). The builder might choose wrong or add both, causing confusion.
**Fix:** Explicitly specify: "Use `pyproject.toml` (PEP 621). Do NOT add `setup.py`. If backward compatibility is needed, use `pyproject.toml` with `[build-system] requires = ["setuptools"]` and `setup.py` as a thin wrapper."

### Gap 6: No `Dockerfile` for Mnemosyne Application

**Severity:** 🟡 High
**Location:** Phase 4 (VPS Deploy)
**Problem:** The plan adds Docker Compose for PostgreSQL in Phase 4 but doesn't mention a Dockerfile for the Mnemosyne app itself. This means the VPS deployment won't have a containerized app.
**Fix:** Add to Phase 4: "Create `Dockerfile` for the Mnemosyne application. Add `docker-compose.yml` that includes both PostgreSQL and the app." OR add a simple `Dockerfile` in Phase 0 so it's ready.

### Gap 7: No Python Version Matrix in CI

**Severity:** 🟡 High
**Location:** GitHub Actions CI
**Problem:** The plan says "Add GitHub Actions CI" but doesn't specify which Python versions to test. The code uses `from typing import List, Dict, Optional, Any, Tuple` which is Python 3.9+ compatible, but should be tested on 3.9, 3.10, 3.11, 3.12.
**Fix:** Add to CI spec: "Test on Python 3.9, 3.10, 3.11, 3.12."

### Gap 8: No `CONTRIBUTING.md` or Issue Templates

**Severity:** 🟡 High
**Location:** Phase 0 (Launch Readiness)
**Problem:** For an open-source project, `CONTRIBUTING.md`, issue templates, and PR templates are essential for community contributions. The plan doesn't mention them.
**Fix:** Add to Phase 0 or Phase 5: "Add `.github/CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature_request.md`, `.github/pull_request_template.md`."

### Gap 9: No `CHANGELOG.md` Creation Strategy

**Severity:** 🟡 Medium
**Location:** Release Process
**Problem:** The release process mentions updating `CHANGELOG.md` but doesn't specify format or initial content. The builder won't know what to write.
**Fix:** Add to Phase 0: "Create `CHANGELOG.md` with Keep a Changelog format. Initial entry: '## [Unreleased]' with placeholder sections."

### Gap 10: No `Makefile` Target Specification

**Severity:** 🟡 Medium
**Location:** Phase 0 Tasks
**Problem:** The plan says "Add Makefile with common commands" but doesn't specify what commands. The builder might miss important ones.
**Fix:** Specify exact targets:
```makefile
.PHONY: help install test test-integration lint format check clean

help:           ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:        ## Install dependencies
	pip install -e .

test:           ## Run unit tests
	pytest tests/ -v --ignore=tests/integration

test-integration: ## Run integration tests (requires PostgreSQL)
	pytest tests/integration -v

lint:           ## Run linting
	flake8 mnemosyne/ tests/
	mypy mnemosyne/

format:         ## Format code
	black mnemosyne/ tests/

check:          ## Run all checks (test + lint)
	make test
	make lint

clean:          ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache
```

### Gap 11: No `.gitignore` Specification

**Severity:** 🟡 Medium
**Location:** Phase 0 Tasks
**Problem:** The plan says "Add `.gitignore`" but doesn't specify what to ignore. The builder might miss important patterns.
**Fix:** Add explicit `.gitignore` content:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Mnemosyne
*.db
*.db-journal
.obsidian/
```

### Gap 12: No `LICENSE` File Specification

**Severity:** 🟡 Medium
**Location:** Phase 0, License
**Problem:** The plan says "Apache 2.0 (or MIT)" but the current `README.md` says MIT. The builder might not know which to choose. Also, the plan says "Consider Apache 2.0" but doesn't make a decision.
**Fix:** Make a firm decision: "Use MIT for Phase 0. Re-evaluate to Apache 2.0 when adding enterprise features (Year 2). Add `LICENSE` file with MIT text. Update `README.md` and `pyproject.toml` to match."

---

## PART 2: CODE-LEVEL BUGS FOUND (Must Fix in Phase 0)

### Bug 1: `Embedder._lock` Never Acquired — Race Condition

**Severity:** 🔴 Critical
**Location:** `mo_graphify_memory.py:72-78` and `108-143`
**Code:**
```python
self._lock = threading.Lock()  # Line 77: Created but NEVER used

def embed(self, texts):
    # No lock acquisition
    vectors = self._model.encode(texts, convert_to_numpy=True)  # NOT thread-safe
```
**Impact:** If multiple threads call `embed()` simultaneously (e.g., concurrent requests to the MCP server), `sentence_transformers` model encoding will crash or produce corrupted results.
**Fix:** Add `with self._lock:` around the model encoding call:
```python
def embed(self, texts: List[str]) -> List[List[float]]:
    if not texts:
        return []
    
    with self._lock:
        if self._provider == "sentence-transformers":
            # ... encode ...
```
**Phase:** Phase 0 (since it's in the core code being moved)

### Bug 2: MCP Server Exception Handler Accesses Undefined `req`

**Severity:** 🔴 Critical
**Location:** `mo_graphify_memory.py:835-836`
**Code:**
```python
except Exception as e:
    resp = {"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}, "id": req.get("id")}
    # ^^^ If exception occurs BEFORE `req = json.loads(line)`, `req` is undefined
```
**Impact:** If an exception occurs during `json.loads()` (e.g., memory error), the exception handler itself will crash with `NameError: name 'req' is not defined`, causing the server to exit.
**Fix:** Use a two-level try/except:
```python
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    req_id = None
    try:
        req = json.loads(line)
        req_id = req.get("id")
        resp = self._handle(req)
    except json.JSONDecodeError as e:
        resp = {"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}, "id": req_id}
    except Exception as e:
        resp = {"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}, "id": req_id}
    print(json.dumps(resp), flush=True)
```
**Phase:** Phase 0 (since it's in the MCP server code being moved)

### Bug 3: `safe_filename` Strips All Non-ASCII Characters

**Severity:** 🔴 Critical
**Location:** `mo_graphify_memory.py:55-57`
**Code:**
```python
def safe_filename(title: str) -> str:
    return re.sub(r'[^\w\s-]', '', title).strip().replace(" ", "-") + ".md"
```
**Impact:** A title like "会议记录" (Chinese) or "Запись" (Russian) becomes `-.md` (after stripping all non-ASCII, only spaces remain which become hyphens). This causes all non-English notes to overwrite the same file `-.md`.
**Fix:** Use a Unicode-aware safe filename function:
```python
import unicodedata

def safe_filename(title: str) -> str:
    # Normalize Unicode and keep most characters
    normalized = unicodedata.normalize('NFKC', title)
    # Replace filesystem-unsafe characters
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '-', normalized)
    # Limit length and ensure valid filename
    safe = safe.strip()[:200]
    return safe + ".md"
```
**Phase:** Phase 0 (core vault functionality)

### Bug 4: `UnifiedMemorySystem.__init__` Calls `self.sync()` Which Fails on Fresh Install

**Severity:** 🔴 Critical
**Location:** `mo_graphify_memory.py:747`
**Code:**
```python
def __init__(self, vault_path: str = VAULT_PATH, dsn: str = DB_DSN):
    self.vault = VaultManager(vault_path)
    self.db = PgVectorStore(dsn)
    # ...
    self.sync()  # Line 747: This will fail if database is not running
```
**Impact:** On a fresh machine without PostgreSQL, `import mnemosyne` or `from mnemosyne import UnifiedMemorySystem` will crash with a connection error. This makes the package unusable for users without PostgreSQL.
**Fix:** Make `sync()` optional or defer it:
```python
def __init__(self, vault_path: str = VAULT_PATH, dsn: str = DB_DSN, auto_sync: bool = True):
    self.vault = VaultManager(vault_path)
    self.db = PgVectorStore(dsn)
    # ...
    if auto_sync:
        try:
            self.sync()
        except Exception as e:
            logger.warning(f"Auto-sync failed: {e}. Call memory.sync() manually.")
```
**Phase:** Phase 0 (core initialization)

### Bug 5: `UnifiedMemorySystem.__init__` Auto-Initializes on Module Import (Global Singleton)

**Severity:** 🔴 Critical
**Location:** `mo_graphify_memory.py:969-984`
**Code:**
```python
def autoload_memory():
    try:
        mem = UnifiedMemorySystem()
        # ...
    except Exception as e:
        logger.error(f"Memory autoload failed: {e}")
        return None

if __name__ != "__main__" and os.environ.get("MEMORY_NO_AUTOLOAD") != "1":
    _global_memory = autoload_memory()  # Line 984: Runs on EVERY import
```
**Impact:** Importing the module (even just `from mnemosyne import MemoryMCPServer`) triggers database connection, vault initialization, and sync. This is unexpected and causes crashes in environments without the database.
**Fix:** Remove the auto-initialization entirely. Require explicit initialization:
```python
# REMOVE this block:
# if __name__ != "__main__" and os.environ.get("MEMORY_NO_AUTOLOAD") != "1":
#     _global_memory = autoload_memory()

# Keep the backward-compat functions but make them lazy:
_global_memory: Optional[UnifiedMemorySystem] = None

def _get_memory() -> UnifiedMemorySystem:
    global _global_memory
    if _global_memory is None:
        _global_memory = UnifiedMemorySystem(auto_sync=False)
    return _global_memory
```
**Phase:** Phase 0 (this is explicitly listed as a fix)

### Bug 6: `PgVectorStore` Uses `ivfflat` Index (Deprecated/Suboptimal)

**Severity:** 🟡 High
**Location:** `mo_graphify_memory.py:240-244`
**Code:**
```python
cur.execute("""
    CREATE INDEX IF NOT EXISTS notes_embedding_idx
    ON notes USING ivfflat (embedding vector_cosine_ops)
    WITH (lists = 100);
""")
```
**Impact:** `ivfflat` is being superseded by `hnsw` in pgvector. `ivfflat` requires knowing the number of lists in advance, and query performance degrades with dataset size. `hnsw` is faster and more accurate for most use cases.
**Fix:** Change to `hnsw` (available in pgvector 0.5.0+):
```python
cur.execute("""
    CREATE INDEX IF NOT EXISTS notes_embedding_idx
    ON notes USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);
""")
```
**Note:** `hnsw` requires more memory for index construction but provides much better query performance. For a student project with <100K vectors, this is the right choice.
**Phase:** Phase 0 (database schema initialization)

### Bug 7: `pgcrypto` Extension Not Explicitly Created

**Severity:** 🟡 High
**Location:** `mo_graphify_memory.py:199-213`
**Code:**
```python
CREATE TABLE IF NOT EXISTS notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    # ...
);
```
**Impact:** `gen_random_uuid()` is a `pgcrypto` function. The code creates `vector` and `pg_trgm` extensions but not `pgcrypto`. On fresh PostgreSQL installations, `gen_random_uuid()` might not exist, causing table creation to fail.
**Fix:** Add `CREATE EXTENSION IF NOT EXISTS pgcrypto;` before creating the notes table.
**Phase:** Phase 0 (database schema initialization)

### Bug 8: `ConsolidationEngine._archive_stale()` Doesn't Merge Duplicates

**Severity:** 🟡 Medium
**Location:** `mo_graphify_memory.py:679-684`
**Code:**
```python
def run(self) -> Dict:
    stats = {"merged": 0, "archived": 0, "pruned": 0, "relinked": 0}
    stats["archived"] += self._archive_stale()
    stats["relinked"] += self._rebuild_links()
    # "merged" and "pruned" are always 0
```
**Impact:** The `merge_duplicates` and `prune_stale` steps are listed in the stats but never implemented. The consolidation engine only archives old notes and rebuilds links.
**Fix:** Either implement the missing methods or remove them from the stats dictionary to avoid confusion. For Phase 0, remove them from stats:
```python
def run(self) -> Dict:
    stats = {"archived": 0, "relinked": 0}
    stats["archived"] = self._archive_stale()
    stats["relinked"] = self._rebuild_links()
    return stats
```
**Phase:** Phase 0 (clean up the API to match implementation)

---

## PART 3: PLANNING GAPS (Fix in Plan, Not Code)

### Gap 13: No Protocol for Builder Session Failure

**Severity:** 🟡 High
**Location:** Session Management Strategy
**Problem:** What if a builder session produces code that doesn't work? The plan says "Architect reviews PR" but doesn't specify what happens if the PR is rejected.
**Fix:** Add to the plan:
```
If Builder Session Fails:
1. Builder session creates HANDOFF.md with failure reason
2. Architect session reviews HANDOFF.md and decides:
   a. Re-spawn builder with corrected prompt (if fix is clear)
   b. Architect fixes it directly (if simpler than re-spawning)
   c. Defer to next phase (if non-critical)
3. If 3 builder sessions fail on same task, architect re-evaluates scope
```

### Gap 14: No Protocol for User Unavailability During Review

**Severity:** 🟡 High
**Location:** Review Process
**Problem:** The user (you) might not be available when a builder session finishes. The plan assumes the architect can review and merge, but the architect (me) can't actually merge PRs on GitHub without the user's credentials.
**Fix:** Add to the plan:
```
PR Review Process:
1. Builder pushes branch and creates PR (draft)
2. Architect reviews code in the PR (via GitHub API or by reading files)
3. Architect leaves review comments on the PR
4. If approved, architect notifies user: "PR ready for merge"
5. User merges when available (or gives architect write access to the repo)
```
**Note:** The user needs to either merge PRs manually or give the architect write access to the repo.

### Gap 15: No `mnemosyne/` Package Conflict with `mo-graphify-obsidian-memory` Repo Name

**Severity:** 🟡 Medium
**Location:** Package Naming
**Problem:** The repo is `mo-graphify-obsidian-memory` but the package will be `mnemosyne`. This is confusing. `pip install mo-graphify-obsidian-memory` but `import mnemosyne`. The plan should clarify this.
**Fix:** Add to the plan: "The repo name is `mo-graphify-obsidian-memory` (historical). The package name is `mnemosyne` (new). In `pyproject.toml`, use `name = "mnemosyne"`. In `__init__.py`, use `__version__ = "1.0.0"`. The repo name can be changed later to `mnemosyne` when the project is rebranded."

### Gap 16: No `Backward-Compat` Strategy for `v1.0` Functions

**Severity:** 🟡 Medium
**Location:** `mo_graphify_memory.py:930-963`
**Problem:** The backward-compatible functions (`create_note`, `read_note`, `search_notes`, `update_note`, `create_moc`) are in the same file as the core code. When splitting into modules, these need to be in `__init__.py` or a separate `compat.py` module. The builder might miss them.
**Fix:** Add to Phase 0 prompt: "Move backward-compatible functions to `mnemosyne/compat.py` and import them in `__init__.py`. Ensure all v1.0 function signatures are preserved."

### Gap 17: No `requirements-dev.txt` Specification

**Severity:** 🟡 Low
**Location:** Phase 0 Tasks
**Problem:** The plan says "Add `requirements-dev.txt`" but doesn't specify what goes in it. The builder might miss important dev dependencies.
**Fix:** Specify exact content:
```
pytest>=7.0
pytest-cov>=4.0
flake8>=5.0
black>=22.0
mypy>=1.0
pytest-postgresql>=5.0
```

### Gap 18: No `README.md` vs `docs/README.md` Clarification

**Severity:** 🟡 Low
**Location:** Repo Structure
**Problem:** The plan says `docs/README.md` but the current repo has `README.md` in the root. GitHub shows the root README on the repo page. The plan should keep `README.md` in the root and add detailed docs in `docs/`.
**Fix:** Clarify: "Keep `README.md` in repo root (GitHub landing page). Add detailed docs in `docs/`. Move `SETUP.md` to `docs/SETUP.md`. Create `docs/API.md` for API reference."

---

## PART 4: DECISION INCONSISTENCIES

### Inconsistency 1: Decision 003 Says "MCP Server ✅" but Phase 2 Says "MCP v2 (stateless) ❌"

**Severity:** 🟡 Medium
**Location:** Decision 003 and Master Plan Phase 2
**Problem:** The feature inventory says MCP Server is "already built" but the phased plan lists MCP v2 as a new feature. This is confusing — the MCP server exists but needs spec update.
**Fix:** In Decision 003, change the feature inventory to:
```
| MCP Server (v1, JSON-RPC with initialize) | ✅ |
| MCP Server (v2, stateless, 2026-07-28) | ❌ | Phase 2 |
```

### Inconsistency 2: Decision 004 Says "GitHub + Vault" but Master Plan Doesn't Mention Vault Sync to GitHub

**Severity:** 🟡 Medium
**Location:** Decision 004 and Master Plan
**Problem:** The decisions in the vault are not automatically synced to GitHub. The plan says "push to GitHub after every phase" but doesn't mention pushing the vault contents.
**Fix:** Add to the plan: "After each phase, the architect session copies new decisions from `obsidian-vault/decisions/` to `docs/decisions/` in the repo and pushes. This ensures decisions are in both the vault (searchable) and GitHub (versioned)."

### Inconsistency 3: Decision 001 Says "Protected branches" but No GitHub Settings Specified

**Severity:** 🟡 Low
**Location:** Decision 001, Git Workflow
**Problem:** The plan says `main` and `develop` are "protected" but doesn't specify how to configure this on GitHub. The user needs to manually enable branch protection rules.
**Fix:** Add to the plan: "After creating `develop` branch, the user should enable branch protection in GitHub Settings > Branches: require PR reviews for `main` and `develop`."

---

## PART 5: RECOMMENDED FIXES — PRIORITIZED

### Must Fix Before Phase 0 Builder Session (🔴 Critical)

1. **Update the Phase 0 builder prompt with:**
   - Module splitting map (which class goes where)
   - `pyproject.toml` as the only packaging file (no `setup.py`)
   - Test strategy (unit tests mock DB, integration tests use PostgreSQL)
   - Fix all 8 code bugs listed above (especially auto-init, race condition, undefined `req`, safe_filename)

2. **Create the `develop` branch or change workflow to use `main`:**
   - Either: `git checkout -b develop && git push origin develop`
   - Or: Change Phase 0 to branch from `main`, create `develop` after Phase 0 merge

3. **Add explicit `.gitignore`, `Makefile`, `LICENSE`, `CHANGELOG.md` content to the prompt:**
   - Don't let the builder guess

4. **Update the plan to specify `README.md` stays in root, `docs/` for detailed docs:**

### Should Fix in Phase 0 (🟡 High)

5. **Add `CONTRIBUTING.md`, issue templates, PR template**
6. **Add Python version matrix (3.9-3.12) to CI spec**
7. **Add `pgcrypto` extension creation to database schema**
8. **Change `ivfflat` to `hnsw` in index creation**
9. **Add `Dockerfile` and `docker-compose.yml` for local dev**

### Can Fix in Phase 1 or Later (🟢 Medium/Low)

10. **Implement missing `merge_duplicates` and `prune_stale` in consolidation**
11. **Add `.editorconfig`, `.pre-commit-config.yaml`**
12. **Rebrand repo name to `mnemosyne` (when ready)**
13. **Enable branch protection on GitHub (manual step)**

---

## PART 6: REVISED PHASE 0 BUILDER PROMPT (Summary of Required Changes)

The Phase 0 builder prompt must include these additions:

```
ADDITIONAL REQUIREMENTS (from Pre-Build Review):

1. FIX THESE BUGS in the code during restructure:
   a. Add `with self._lock:` around `self._model.encode()` in `Embedder.embed()`
   b. Fix MCP exception handler to use `req_id` variable instead of `req.get("id")`
   c. Fix `safe_filename()` to preserve Unicode (use `unicodedata`)
   d. Make `UnifiedMemorySystem.__init__` auto_sync optional (default False)
   e. REMOVE the auto-initialization block at bottom of file (lines 969-984)
   f. Add `CREATE EXTENSION IF NOT EXISTS pgcrypto;` before creating notes table
   g. Change `ivfflat` index to `hnsw` with (m=16, ef_construction=64)
   h. Fix `ConsolidationEngine.run()` to remove unimplemented stats (merged, pruned)

2. MODULE SPLITTING MAP (exact mapping):
   mnemosyne/__init__.py     -> exports + version
   mnemosyne/core.py         -> UnifiedMemorySystem
   mnemosyne/stores/__init__.py  -> store base
   mnemosyne/stores/postgres.py  -> PgVectorStore
   mnemosyne/embedder.py     -> Embedder
   mnemosyne/vault.py        -> VaultManager
   mnemosyne/security.py     -> AdmissionControl, SalienceEngine
   mnemosyne/prospective.py  -> ProspectiveMemory
   mnemosyne/consolidation.py -> ConsolidationEngine
   mnemosyne/mcp_server.py   -> MemoryMCPServer
   mnemosyne/compat.py      -> v1.0 backward compat functions
   mnemosyne/cli.py         -> placeholder for Phase 3

3. TEST STRATEGY:
   - Unit tests: mock PgVectorStore, test logic in isolation
   - Integration tests: use PostgreSQL via pytest-postgresql or Docker
   - All tests in tests/ directory with pytest markers

4. CI STRATEGY:
   - GitHub Actions with PostgreSQL service container
   - Test on Python 3.9, 3.10, 3.11, 3.12
   - Run: pytest, flake8, mypy

5. BRANCHING:
   - Create branch from `main` (not `develop`, since `develop` doesn't exist yet)
   - Name: `feature/phase-0-restructure`
```

---

## PART 7: REVIEW STATUS

| Check | Status | Notes |
|-------|--------|-------|
| Master Plan completeness | ⚠️ Needs update | 12 gaps found, 8 code bugs |
| Decision consistency | ⚠️ Needs update | 3 inconsistencies |
| Code quality review | ✅ Complete | 8 bugs identified with line numbers |
| Security review | ✅ Complete | No new security issues beyond known ones |
| Test strategy | ⚠️ Needs definition | Mock vs integration test approach needed |
| CI/CD strategy | ⚠️ Needs definition | PostgreSQL service container needed |
| Git workflow feasibility | ⚠️ Needs adjustment | `develop` branch doesn't exist |
| Session handoff completeness | ⚠️ Needs update | Failure protocol missing |
| Documentation completeness | ⚠️ Needs update | Missing `.gitignore`, `Makefile` specs |
| Overall readiness for Phase 0 | ⚠️ NOT READY | Fix plan and prompt first |

**Verdict:** 🔴 **DO NOT SPAWN BUILDER SESSION YET.** Fix the plan and prompt first (2 hours of work). Then spawn.

---

## NEXT STEPS

1. Update `MASTER_PLAN_v1.0.md` with the gaps found in this review
2. Update Decision 003 with the corrected feature inventory
3. Create a detailed, bug-free Phase 0 builder prompt
4. Save this review to the vault and GitHub
5. Notify user: "Review complete. 12 gaps + 8 bugs found. Plan updated. Ready to spawn builder session."

---

*Document: Pre-Build Review*
*Reviewer: Architect Session (self-review)*
*Date: 2026-07-06*
*Status: COMPLETE — Plan needs update before Phase 0*

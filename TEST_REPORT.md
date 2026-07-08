# Phase 0 Test Report

## Environment
- Python version: Python 3.9.6
- PostgreSQL: Available (Docker container `mnemosyne-pg-test` on port 15432)

## Unit Tests
```
pytest tests/ -v -m "not integration" -p no:postgresql
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
collecting ... collected 13 items / 2 deselected / 11 selected

tests/test_embedder.py::TestEmbedder::test_embed_single_text PASSED
tests/test_embedder.py::TestEmbedder::test_embed_empty_list PASSED
tests/test_embedder.py::TestEmbedder::test_embed_multiple_texts PASSED
tests/test_mcp.py::TestMCPServer::test_initialize_request PASSED
tests/test_mcp.py::TestMCPServer::test_tools_list PASSED
tests/test_security.py::TestAdmissionControl::test_valid_note_passes FAILED
tests/test_security.py::TestAdmissionControl::test_injection_detection PASSED
tests/test_security.py::TestAdmissionControl::test_too_long_content_fails PASSED
tests/test_vault.py::TestVaultManager::test_write_and_read_note PASSED
tests/test_vault.py::TestVaultManager::test_safe_filename_unicode PASSED
tests/test_vault.py::TestVaultManager::test_wiki_links_extraction PASSED

============ 1 failed, 10 passed, 2 deselected, 1 warning in 17.65s ===========
```

**Failure:**
- `tests/test_security.py::TestAdmissionControl::test_valid_note_passes`
  - Expected: `(True, "")`
  - Actual:   `(True, "All checks passed")`
  - The `validate()` method returns a success message instead of an empty string.

## Integration Tests
```
export MEMORY_DB_DSN="postgresql://mnemosyne:mnemosyne@localhost:15432/mnemosyne"
pytest tests/ -v -m integration -p no:postgresql
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
collecting ... collected 13 items / 11 deselected / 2 selected

tests/test_integration.py::TestIntegration::test_remember_and_recall PASSED
tests/test_integration.py::TestIntegration::test_hybrid_search PASSED

================= 2 passed, 11 deselected, 1 warning in 11.34s =================
```

## Linting

### flake8
```
mnemosyne/__init__.py:12:80: E501 line too long (87 > 79 characters)
mnemosyne/compat.py:10:1: E302 expected 2 blank lines, found 1
mnemosyne/compat.py:16:1: E302 expected 2 blank lines, found 1
mnemosyne/compat.py:16:80: E501 line too long (86 > 79 characters)
mnemosyne/compat.py:18:80: E501 line too long (85 > 79 characters)
mnemosyne/compat.py:20:1: E302 expected 2 blank lines, found 1
mnemosyne/compat.py:25:1: E302 expected 2 blank lines, found 1
mnemosyne/compat.py:29:1: E302 expected 2 blank lines, found 1
mnemosyne/compat.py:42:80: E501 line too long (142 > 79 characters)
mnemosyne/compat.py:44:1: E302 expected 2 blank lines, found 1
mnemosyne/compat.py:49:80: E501 line too long (89 > 79 characters)
mnemosyne/consolidation.py:57:80: E501 line too long (87 > 79 characters)
mnemosyne/core.py:3:1: F401 'os' imported but unused
mnemosyne/core.py:15:80: E501 line too long (87 > 79 characters)
mnemosyne/core.py:30:80: E501 line too long (97 > 79 characters)
mnemosyne/core.py:37:80: E501 line too long (84 > 79 characters)
mnemosyne/core.py:43:80: E501 line too long (87 > 79 characters)
mnemosyne/core.py:60:80: E501 line too long (107 > 79 characters)
mnemosyne/core.py:62:80: E501 line too long (89 > 79 characters)
mnemosyne/core.py:63:80: E501 line too long (91 > 79 characters)
mnemosyne/core.py:64:80: E501 line too long (129 > 79 characters)
mnemosyne/core.py:71:80: E501 line too long (80 > 79 characters)
mnemosyne/embedder.py:26:80: E501 line too long (84 > 79 characters)
mnemosyne/embedder.py:41:80: E501 line too long (85 > 79 characters)
mnemosyne/embedder.py:49:80: E501 line too long (80 > 79 characters)
mnemosyne/embedder.py:60:80: E501 line too long (85 > 79 characters)
mnemosyne/embedder.py:73:80: E501 line too long (84 > 79 characters)
mnemosyne/embedder.py:81:80: E501 line too long (94 > 79 characters)
mnemosyne/embedder.py:90:80: E501 line too long (86 > 79 characters)
mnemosyne/mcp_server.py:29:80: E501 line too long (86 > 79 characters)
mnemosyne/mcp_server.py:41:80: E501 line too long (101 > 79 characters)
mnemosyne/mcp_server.py:43:80: E501 line too long (101 > 79 characters)
mnemosyne/mcp_server.py:53:80: E501 line too long (116 > 79 characters)
mnemosyne/mcp_server.py:55:80: E501 line too long (87 > 79 characters)
mnemosyne/mcp_server.py:60:80: E501 line too long (122 > 79 characters)
mnemosyne/mcp_server.py:61:80: E501 line too long (116 > 79 characters)
mnemosyne/mcp_server.py:67:80: E501 line too long (92 > 79 characters)
mnemosyne/mcp_server.py:81:80: E501 line too long (101 > 79 characters)
mnemosyne/mcp_server.py:86:80: E501 line too long (103 > 79 characters)
mnemosyne/mcp_server.py:101:80: E501 line too long (95 > 79 characters)
mnemosyne/mcp_server.py:115:80: E501 line too long (159 > 79 characters)
mnemosyne/mcp_server.py:117:80: E501 line too long (140 > 79 characters)
mnemosyne/mcp_server.py:119:80: E501 line too long (191 > 79 characters)
mnemosyne/prospective.py:15:80: E501 line too long (106 > 79 characters)
mnemosyne/prospective.py:20:80: E501 line too long (83 > 79 characters)
mnemosyne/prospective.py:47:80: E501 line too long (100 > 79 characters)
mnemosyne/security.py:20:80: E501 line too long (97 > 79 characters)
mnemosyne/security.py:44:80: E501 line too long (90 > 79 characters)
mnemosyne/security.py:53:80: E501 line too long (95 > 79 characters)
mnemosyne/security.py:62:80: E501 line too long (94 > 79 characters)
mnemosyne/security.py:70:80: E501 line too long (83 > 79 characters)
mnemosyne/security.py:83:80: E501 line too long (84 > 79 characters)
mnemosyne/security.py:88:80: E501 line too long (87 > 79 characters)
mnemosyne/stores/postgres.py:10:80: E501 line too long (81 > 79 characters)
mnemosyne/stores/postgres.py:53:80: E501 line too long (80 > 79 characters)
mnemosyne/stores/postgres.py:60:80: E501 line too long (92 > 79 characters)
mnemosyne/stores/postgres.py:61:80: E501 line too long (92 > 79 characters)
mnemosyne/stores/postgres.py:64:80: E501 line too long (89 > 79 characters)
mnemosyne/stores/postgres.py:65:80: E501 line too long (86 > 79 characters)
mnemosyne/stores/postgres.py:86:80: E501 line too long (97 > 79 characters)
mnemosyne/stores/postgres.py:87:80: E501 line too long (99 > 79 characters)
mnemosyne/stores/postgres.py:88:80: E501 line too long (102 > 79 characters)
mnemosyne/stores/postgres.py:89:80: E501 line too long (110 > 79 characters)
mnemosyne/stores/postgres.py:92:80: E501 line too long (87 > 79 characters)
mnemosyne/stores/postgres.py:94:80: E501 line too long (101 > 79 characters)
mnemosyne/stores/postgres.py:95:80: E501 line too long (103 > 79 characters)
mnemosyne/stores/postgres.py:96:80: E501 line too long (120 > 79 characters)
mnemosyne/stores/postgres.py:118:80: E501 line too long (112 > 79 characters)
mnemosyne/stores/postgres.py:129:80: E501 line too long (96 > 79 characters)
mnemosyne/stores/postgres.py:138:80: E501 line too long (99 > 79 characters)
mnemosyne/stores/postgres.py:161:80: E501 line too long (85 > 79 characters)
mnemosyne/stores/postgres.py:177:80: E501 line too long (85 > 79 characters)
mnemosyne/stores/postgres.py:178:80: E501 line too long (87 > 79 characters)
mnemosyne/stores/postgres.py:188:80: E501 line too long (91 > 79 characters)
mnemosyne/stores/postgres.py:189:80: E501 line too long (81 > 79 characters)
mnemosyne/stores/postgres.py:194:80: E501 line too long (90 > 79 characters)
mnemosyne/stores/postgres.py:201:80: E501 line too long (96 > 79 characters)
mnemosyne/stores/postgres.py:209:80: E501 line too long (89 > 79 characters)
mnemosyne/stores/postgres.py:245:80: E501 line too long (92 > 79 characters)
mnemosyne/stores/postgres.py:252:80: E501 line too long (87 > 79 characters)
mnemosyne/stores/postgres.py:255:80: E501 line too long (85 > 79 characters)
mnemosyne/stores/postgres.py:258:80: E501 line too long (80 > 79 characters)
mnemosyne/stores/postgres.py:266:80: E501 line too long (82 > 79 characters)
mnemosyne/stores/postgres.py:270:80: E501 line too long (89 > 79 characters)
mnemosyne/stores/postgres.py:272:80: E501 line too long (95 > 79 characters)
mnemosyne/vault.py:62:80: E501 line too long (108 > 79 characters)
mnemosyne/vault.py:68:80: E501 line too long (82 > 79 characters)
mnemosyne/vault.py:125:80: E501 line too long (94 > 79 characters)
mnemosyne/vault.py:126:80: E501 line too long (124 > 79 characters)
tests/test_embedder.py:1:1: F401 'pytest' imported but unused
tests/test_integration.py:15:80: E501 line too long (113 > 79 characters)
tests/test_mcp.py:1:1: F401 'pytest' imported but unused
tests/test_security.py:1:1: F401 'pytest' imported but unused
tests/test_security.py:8:80: E501 line too long (87 > 79 characters)
tests/test_security.py:12:80: E501 line too long (88 > 79 characters)
```

### mypy
```
mnemosyne/cli.py:6: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/cli.py:6: note: Use "-> None" if function does not return a value
mnemosyne/security.py:16: error: Function is missing type annotation  [no-untyped-def]
mnemosyne/prospective.py:12: error: Function is missing a type annotation  [no-untyped-def]
mnemosyne/prospective.py:27: error: Returning Any from function declared to return "str"  [no-any-return]
mnemosyne/prospective.py:43: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/consolidation.py:18: error: Function is missing a type annotation  [no-untyped-def]
mnemosyne/stores/postgres.py:24: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/stores/postgres.py:27: error: Library stubs not installed for "psycopg2"  [import-untyped]
mnemosyne/stores/postgres.py:31: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/stores/postgres.py:31: note: Use "-> None" if function does not return a value
mnemosyne/stores/postgres.py:132: error: Returning Any from function declared to return "str"  [no-any-return]
mnemosyne/stores/postgres.py:229: error: Function is missing a type annotation  [no-untyped-def]
mnemosyne/stores/postgres.py:248: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/embedder.py:34: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/embedder.py:34: note: Use "-> None" if function does not return a value
mnemosyne/embedder.py:70: error: "None" has no attribute "encode"  [attr-defined]
mnemosyne/embedder.py:74: error: Incompatible types in assignment (expression has type "str", variable has type "None")  [assignment]
mnemosyne/embedder.py:94: error: Incompatible types in assignment (expression has type "str", variable has type "None")  [assignment]
mnemosyne/vault.py:37: error: Incompatible default for argument "tags" (default has type "None", argument has type "list[str]")  [assignment]
mnemosyne/vault.py:39: error: Incompatible default for argument "links" (default has type "None", argument has type "list[str]")  [assignment]
mnemosyne/vault.py:61: error: Library stubs not installed for "yaml"  [import-untyped]
mnemosyne/vault.py:110: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
mnemosyne/core.py:45: error: Incompatible default for argument "tags" (default has type "None", argument has type "list[str]")  [assignment]
mnemosyne/core.py:46: error: Incompatible default for argument "links" (default has type "None", argument has type "list[str]")  [assignment]
mnemosyne/mcp_server.py:28: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/compat.py:16: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/compat.py:16: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
mnemosyne/compat.py:25: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/compat.py:29: error: Function is missing a return type annotation  [no-untyped-def]
mnemosyne/compat.py:29: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
mnemosyne/compat.py:44: error: Function is missing a return type annotation  [no-untyped-def]
Found 29 errors in 10 files (checked 12 source files)
```

## Import Checks
| Import | Result |
|--------|--------|
| `from mnemosyne import UnifiedMemorySystem, MemoryMCPServer` | OK |
| `from mnemosyne.core import UnifiedMemorySystem` | OK |
| `from mnemosyne.vault import VaultManager, safe_filename` | OK |
| `from mnemosyne.embedder import Embedder` | OK |
| `from mnemosyne.stores.postgres import PgVectorStore` | OK |
| `from mnemosyne.security import AdmissionControl, SalienceEngine` | OK |
| `from mnemosyne.mcp_server import MemoryMCPServer` | OK |

## Summary
- Unit tests: **FAIL** (1 failed — test/code mismatch in `test_valid_note_passes`)
- Integration tests: **PASS** (2 passed when `MEMORY_DB_DSN` is set)
- Linting: **FAIL** (flake8: many style violations; mypy: 29 type errors)
- Imports: **PASS**

## Issues Found

### 1. Test/Code Mismatch in `test_security.py`
**File:** `tests/test_security.py:8`
**Error:**
```
AssertionError: assert (True, 'All checks passed') == (True, '')
```
**Fix:** Either update the test to expect `"All checks passed"` or change `AdmissionControl.validate()` to return an empty string on success.

### 2. `make test` Fails
**Cause:** Two issues:
1. `pytest` is not on `PATH` when installed via `pip install --user`.
2. `pytest-postgresql` plugin auto-loads and crashes because `psycopg` v3 cannot find `libpq` on this system.

**Workaround:** Run with explicit path and disable plugin:
```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
pytest tests/ -v -m "not integration" -p no:postgresql
```

### 3. Integration Test Default DSN Uses Port 5432
**File:** `tests/test_integration.py:13`
The fallback DSN defaults to port `5432`, but the test instructions specify port `15432`. Integration tests only pass when `MEMORY_DB_DSN` is explicitly exported. Consider updating the fallback DSN or documenting the requirement more prominently.

### 4. Linting Violations
- **flake8:** Numerous `E501` (line too long), `E302` (blank lines), and `F401` (unused imports) violations across `mnemosyne/` and `tests/`.
- **mypy:** 29 type-checking errors including missing type annotations, missing stub packages (`psycopg2`, `yaml`), and implicit `Optional` defaults.

### 5. Missing psycopg3 libpq Support
The `pytest-postgresql` dependency pulls in `psycopg` v3, which requires `libpq` installed on the system or the `psycopg_binary` / `psycopg_c` extras. On macOS with the stock Python from Xcode, neither is available, causing pytest to crash unless `-p no:postgresql` is used.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial package structure
- PostgreSQL + pgvector support
- Markdown vault with YAML frontmatter
- MCP server (JSON-RPC)
- Admission control and salience scoring
- Prospective memory (reminders)
- Memory consolidation (archive + relink)
- SQLite fallback store (zero-config, no PostgreSQL needed)
- Cross-platform compatibility (macOS, Linux, Windows)

### Changed
- Restructured from single file to proper Python package
- `prospective.py` and `consolidation.py` now auto-detect SQLite vs PostgreSQL

### Fixed
- **SQLite compatibility**: `prospective.py` and `consolidation.py` now work with SQLite fallback
  - Fixed `AttributeError: __enter__` on cursor context managers (sqlite3 doesn't support `with conn.cursor()`)
  - Fixed PostgreSQL-only `NOW() + INTERVAL` syntax for SQLite `datetime()`
  - Fixed PostgreSQL-only `RETURNING id` with manual UUID generation for SQLite
  - Fixed `%s` placeholders to `?` for SQLite dialect
- Race condition in Embedder
- MCP exception handler NameError
- Unicode filename handling
- Auto-initialization crash

## [0.1.0] - 2026-07-XX

### Added
- Initial release

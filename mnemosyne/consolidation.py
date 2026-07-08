"""Consolidation engine (sleep-time maintenance)."""

import logging
from datetime import datetime, timedelta
from typing import Dict

logger = logging.getLogger("unified-memory")


class ConsolidationEngine:
    """
    Nightly batch maintenance:
    - Merge near-duplicate notes
    - Archive stale, low-salience notes
    - Prune orphaned notes
    - Rebuild graph edges
    """

    def __init__(self, db, vault, embedder):
        self.db = db
        self.vault = vault
        self.embedder = embedder

    def _is_sqlite(self) -> bool:
        """Check if we're using SQLite."""
        return hasattr(self.db, 'db_path') or type(self.db).__name__ == 'SQLiteStore'

    def run(self) -> Dict:
        """Run full consolidation. Returns stats."""
        stats = {"archived": 0, "relinked": 0}
        stats["archived"] = self._archive_stale()
        stats["relinked"] = self._rebuild_links()
        logger.info(f"Consolidation complete: {stats}")
        return stats

    def _archive_stale(self) -> int:
        """Archive notes not updated in 90 days with salience < 0.2."""
        conn = self.db._conn()
        try:
            cur = conn.cursor()
            if self._is_sqlite():
                cutoff = (datetime.now() - timedelta(days=90)).isoformat()
                cur.execute(
                    """
                    UPDATE notes
                    SET status = 'archived'
                    WHERE status = 'active'
                      AND updated_at < ?
                      AND salience < 0.2
                    """,
                    (cutoff,)
                )
                archived = cur.rowcount
            else:
                cur.execute(
                    """
                    UPDATE notes
                    SET status = 'archived'
                    WHERE status = 'active'
                      AND updated_at < NOW() - INTERVAL '90 days'
                      AND salience < 0.2
                    RETURNING id;
                    """
                )
                archived = len(cur.fetchall())
            conn.commit()
            return archived
        finally:
            cur.close()
            conn.close()

    def _rebuild_links(self) -> int:
        """Rebuild graph edges from vault files."""
        count = 0
        for filepath in self.vault.list_notes():
            try:
                text = filepath.read_text(encoding="utf-8")
                parsed = self.vault._parse_note(text)
                title = parsed["frontmatter"].get("title", filepath.stem)
                conn = self.db._conn()
                try:
                    cur = conn.cursor()
                    if self._is_sqlite():
                        cur.execute("SELECT id FROM notes WHERE title = ?;", (title,))
                    else:
                        cur.execute("SELECT id FROM notes WHERE title = %s;", (title,))
                    row = cur.fetchone()
                    if row:
                        links = self.vault.extract_wiki_links(text)
                        self.db.update_links(row[0], links)
                        count += 1
                finally:
                    cur.close()
                    conn.close()
            except Exception as e:
                logger.error(f"Link rebuild error: {e}")
        return count

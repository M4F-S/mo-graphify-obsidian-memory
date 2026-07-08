"""Prospective memory (scheduled reminders)."""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional

logger = logging.getLogger("unified-memory")


class ProspectiveMemory:
    """Remember to do something in the future."""

    def __init__(self, db):
        self.db = db

    def _is_sqlite(self) -> bool:
        """Check if we're using SQLite (for dialect-specific queries)."""
        return hasattr(self.db, 'db_path') or type(self.db).__name__ == 'SQLiteStore'

    def schedule(
        self, title: str, content: str, trigger_at: str, recurring: Optional[str] = None
    ) -> str:
        """Schedule a future reminder. trigger_at: ISO 8601 datetime string."""
        import uuid
        pid = str(uuid.uuid4())
        
        conn = self.db._conn()
        try:
            cur = conn.cursor()
            if self._is_sqlite():
                cur.execute(
                    """
                    INSERT INTO prospective (id, title, content, trigger_at, recurring)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (pid, title, content, trigger_at, recurring),
                )
            else:
                cur.execute(
                    """
                    INSERT INTO prospective (title, content, trigger_at, recurring)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    (title, content, trigger_at, recurring),
                )
                pid = cur.fetchone()[0]
            conn.commit()
            logger.info(f"Scheduled reminder: {title} at {trigger_at}")
            return pid
        finally:
            cur.close()
            conn.close()

    def get_due(self, window_hours: int = 24) -> List[Dict]:
        """Get reminders due within the next N hours."""
        conn = self.db._conn()
        try:
            cur = conn.cursor()
            if self._is_sqlite():
                # SQLite: compute cutoff with datetime()
                cutoff = (datetime.now() + timedelta(hours=window_hours)).isoformat()
                cur.execute(
                    """
                    SELECT id, title, content, trigger_at, recurring
                    FROM prospective
                    WHERE status = 'pending'
                      AND trigger_at <= ?
                    ORDER BY trigger_at;
                    """,
                    (cutoff,),
                )
            else:
                cur.execute(
                    """
                    SELECT id, title, content, trigger_at, recurring
                    FROM prospective
                    WHERE status = 'pending'
                      AND trigger_at <= NOW() + INTERVAL '%s hours'
                    ORDER BY trigger_at;
                    """,
                    (window_hours,),
                )
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]
        finally:
            cur.close()
            conn.close()

    def mark_done(self, reminder_id: str):
        """Mark a reminder as completed."""
        conn = self.db._conn()
        try:
            cur = conn.cursor()
            if self._is_sqlite():
                cur.execute(
                    "UPDATE prospective SET status = 'done' WHERE id = ?;",
                    (reminder_id,)
                )
            else:
                cur.execute(
                    "UPDATE prospective SET status = 'done' WHERE id = %s;",
                    (reminder_id,)
                )
            conn.commit()
        finally:
            cur.close()
            conn.close()

import json
import sqlite3
from abc import ABC, abstractmethod
from typing import List, Dict


class Storage(ABC):
    """Abstract storage interface (SOLID DIP)."""

    @abstractmethod
    def save(self, contacts: List[Dict[str, str]]) -> None:
        pass

    @abstractmethod
    def load(self) -> List[Dict[str, str]]:
        pass
    
class JSONStorage(Storage):
    """Save and load contacts from a JSON file."""

    def __init__(self, filename: str = "contacts.json"):
        self.filename = filename

    def save(self, contacts: List[Dict[str, str]]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4)

    def load(self) -> List[Dict[str, str]]:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

class SQLiteStorage(Storage):
    """Save and load contacts from a SQLite database."""

    def __init__(self, db_name: str = "contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL DEFAULT ''
            )
        """)
        # Add email to databases created by the earlier two-column schema.
        cursor.execute("PRAGMA table_info(contacts)")
        columns = {row[1] for row in cursor.fetchall()}
        if "email" not in columns:
            cursor.execute("ALTER TABLE contacts ADD COLUMN email TEXT NOT NULL DEFAULT ''")
        self.conn.commit()

    def save(self, contacts: List[Dict[str, str]]) -> None:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM contacts")  # Clear existing contacts
        for contact in contacts:
            cursor.execute(
                "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
                (contact["name"], contact["phone"], contact.get("email", "")),
            )
        self.conn.commit()

    def load(self) -> List[Dict[str, str]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT name, phone, email FROM contacts")
        rows = cursor.fetchall()
        return [{"name": row[0], "phone": row[1], "email": row[2]} for row in rows]


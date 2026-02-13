import json
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

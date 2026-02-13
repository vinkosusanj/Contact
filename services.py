from typing import List
from models import Contact
from storage import Storage


class ContactService:
    """Business logic for managing contacts."""

    def __init__(self, storage: Storage):
        self.storage = storage
        self.contacts: List[Contact] = []
        self._load_contacts()

    # --- Private method ---
    def _load_contacts(self) -> None:
        data = self.storage.load()
        self.contacts = [Contact(**d) for d in data]

    # --- Public API ---
    def add_contact(self, name: str, phone: str, email: str) -> None:
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self._save_contacts()

    def list_contacts(self) -> List[Contact]:
        return self.contacts

    def _save_contacts(self) -> None:
        data = [c.to_dict() for c in self.contacts]
        self.storage.save(data)

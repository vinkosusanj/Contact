class ConsoleUI:
    def show_menu(self):
        print("\n📒 Contact Manager")
        print()
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def get_input(self, text):
        return input(text)

    def show_contacts(self, contacts):
        if not contacts:
            print("No contacts found.")
            return
        for index, c in enumerate(contacts, start=1):
            print(f"{index}. {c.name} | {c.phone} | {c.email}")

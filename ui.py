class ConsoleUI:
    def show_menu(self):
        print("\n📒 Contact Manager")
        print()
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search Contact")
        print("4. Exit")

    def get_input(self, text):
        return input(text)

    def show_contacts(self, contacts):
        for c in contacts:
            print(f"{c.name} | {c.phone} | {c.email}")
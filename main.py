from storage import JSONStorage
from services import ContactService
from ui import ConsoleUI


def main():
    storage = JSONStorage()
    service = ContactService(storage)
    ui = ConsoleUI()

    while True:
        ui.show_menu()
        choice = ui.get_input("Please select an option: ")

        if choice == "1":
            name = ui.get_input("Name: ")
            phone = ui.get_input("Phone numbre: ")
            email = ui.get_input("E-mail: ")
            service.add_contact(name, phone, email)
            print("✅ Contact added!")
        elif choice == "2":
            ui.show_contacts(service.list_contacts())
        elif choice == "3":
            name = ui.get_input("Contact name: ")
            result = service.search_contact(name)
            if result:
                ui.show_contacts(result)
            else:
                print("contact not found")
        elif choice == "4":
            original_name = ui.get_input("Contact name to update: ")
            matches = service.search_contact(original_name)
            if not matches:
                print("contact not found")
                continue
            if len(matches) > 1:
                print("Multiple contacts found:")
                ui.show_contacts(matches)
                index = ui.get_input("Select contact number to update: ")
                if not index.isdigit() or int(index) < 1 or int(index) > len(matches):
                    print("Invalid selection")
                    continue
                contact = matches[int(index) - 1]
            else:
                contact = matches[0]

            name = ui.get_input(f"New name [{contact.name}]: ") or contact.name
            phone = ui.get_input(f"New phone [{contact.phone}]: ") or contact.phone
            email = ui.get_input(f"New e-mail [{contact.email}]: ") or contact.email
            if service.update_contact(contact.name, name, phone, email):
                print("✅ Contact updated!")
            else:
                print("contact not found")
        elif choice == "5":
            name = ui.get_input("Contact name to delete: ")
            matches = service.search_contact(name)
            if not matches:
                print("contact not found")
                continue
            if len(matches) > 1:
                print("Multiple contacts found:")
                ui.show_contacts(matches)
                index = ui.get_input("Select contact number to delete: ")
                if not index.isdigit() or int(index) < 1 or int(index) > len(matches):
                    print("Invalid selection")
                    continue
                contact = matches[int(index) - 1]
            else:
                contact = matches[0]

            confirm = ui.get_input(f"Delete {contact.name}? (y/n): ")
            if confirm.lower() == "y":
                if service.delete_contact(contact.name):
                    print("✅ Contact deleted!")
                else:
                    print("contact not found")
            else:
                print("Deletion canceled")
        elif choice == "6":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
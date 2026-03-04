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
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
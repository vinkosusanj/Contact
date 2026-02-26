from storage import JSONStorage
from services import ContactService
from ui import ConsoleUI


def main():
    storage = JSONStorage()
    service = ContactService(storage)
    ui = ConsoleUI()

    while True:
        ui.show_menu()
        choice = ui.get_input("Selecciona una opción:")

        if choice == "1":
            name = ui.get_input("Nombre: ")
            phone = ui.get_input("Teléfono: ")
            email = ui.get_input("Email: ")
            service.add_contact(name, phone, email)
            print("✅ Contact added!")
        elif choice == "2":
            ui.show_contacts(service.list_contacts())
        elif choice == "3":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
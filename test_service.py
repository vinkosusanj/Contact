from storage import JSONStorage
from services import ContactService

storage = JSONStorage()
service = ContactService(storage)

service.add_contact("Juan", "123", "juan@test.com")
service.add_contact("Maria", "456", "maria@test.com")

for c in service.list_contacts():
    print(c)

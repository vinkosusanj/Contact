from storage import JSONStorage

storage = JSONStorage()

data = [
    {"name": "Vinko", "phone": "789", "email": "vinko@test.com"}
]


storage.save(data)
print(storage.load())

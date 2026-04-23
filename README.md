# 📒 Contact Manager (CLI - JSON Version)

A simple Contact Manager built with Python.
This project demonstrates object-oriented programming, separation of concerns, and data persistence using a JSON file.

## 🛠 Technologies Used

- Python 3
- JSON for data persistence
- Object-Oriented Programming (OOP)
- SOLID principles
- CLI (Command Line Interface)

## ✨ Features

- Add new contacts
- List saved contacts
- Search contacts by name
- Persistent storage using JSON file
- Modular and layered architecture

## 🚀 How to Run

1. Clone the repository:

   git clone <your-repo-url>

2. Navigate to the project folder:

   cd Contact

3. Run the application:

   python main.py

## 🧭 Suggested Next Steps (Roadmap)

If you want to keep advancing this project, follow this order:

1. **Update and Delete contacts (CRUD complete)**
   - Add methods in `ContactService` for update/delete.
   - Add options in the CLI menu.

2. **Input validation**
   - Validate empty names.
   - Validate phone format and email format.

3. **Unit tests**
   - Add tests for `ContactService` and `JSONStorage`.
   - Start with `pytest` and test add/list/search/update/delete.

4. **Improve persistence layer**
   - Replace JSON with SQLite.
   - Keep `Storage` as abstraction to respect SOLID.

5. **Expose an API (FastAPI)**
   - Reuse service layer in endpoints.
   - Keep CLI as optional interface.

## 🧠 Architecture Overview

The project follows a layered architecture:

- Model Layer → Defines the Contact entity
- Service Layer → Handles business logic
- Storage Layer → Manages JSON persistence
- UI Layer → Handles user interaction
- Main → Entry point of the application

This separation improves readability, maintainability, and scalability.

## 📚 What I Learned

- Applying SOLID principles
- Structuring a small project using multiple layers
- Working with file persistence (JSON)
- Separating business logic from presentation layer

## 🔮 Future Improvements

- [x] ~~Add delete/update features~~
- [ ] Migrate to SQLite database
- [ ] Add unit tests
- [ ] Convert to REST API using FastAPI

## 👨‍💻 Author

Vinko

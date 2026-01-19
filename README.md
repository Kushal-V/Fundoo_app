# Fundoo App Backend

Fundoo App is a comprehensive note-taking application backend built with **FastAPI** and **PostgreSQL**. It allows users to create, manage, and label notes, similar to Google Keep.

## 🚀 Features

-   **User Management**: Register and manage user accounts.
-   **Note Management**: Create, read, update, and delete notes.
-   **Label Management**: Create labels and attach/detach them to notes.
-   **Authentication**: Secure password hashing using Argon2 (via `passlib`).
-   **Database**: robust data persistence using PostgreSQL and SQLAlchemy ORM.

## 🛠 Tech Stack

-   **Language**: Python 3.x
-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **Database**: PostgreSQL
-   **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
-   **Server**: Uvicorn

## ⚙️ Setup & Installation

### Prerequisites
-   Python 3.8+
-   PostgreSQL installed and running.

### 1. Clone the Repository
```bash
git clone <repository_url>
cd Fundoo_app
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install packages
pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib[argon2]
```

### 3. Configure Database
Update the database connection string in `app/db/session.py` with your local PostgreSQL credentials.

Default configuration structure:
-   **User**: `your_username` (default: postgres)
-   **Password**: `your_password`
-   **Database**: `fundoo_db`
-   **Host**: `localhost`
-   **Port**: `5432`

> **Important**: Ensure you update `app/db/session.py` with your actual database credentials before running the app. Do not commit your real password to version control.

### 4. Run the Application
Navigate to the `app` directory and run the server:
```bash
cd app
python -m uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## 📖 API Documentation

FastAPI provides automatic interactive documentation:

-   **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
-   **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📁 Project Structure

```
Fundoo_app/
├── app/
│   ├── db/          # Database connection and models
│   ├── models/      # SQLAlchemy Database Models
│   ├── routes/      # API Routes (User, Note, Label)
│   ├── schemas/     # Pydantic Schemas
│   ├── src/         # Service layer / Business Logic
│   ├── utils/       # Utilities (e.g., Password hashing)
│   └── main.py      # Entry point
└── README.md
```

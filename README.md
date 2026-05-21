# FastAPI SQLModel Async Alembic CRUD API

A modern FastAPI backend project built with:

- FastAPI
- SQLModel
- PostgreSQL (Neon)
- Async SQLAlchemy
- AsyncPG
- Alembic
- Swagger/OpenAPI Docs

This project demonstrates a fully async CRUD API with database migrations using Alembic.

---

# Features

- Async FastAPI setup
- PostgreSQL cloud database (Neon)
- SQLModel ORM
- Async CRUD operations
- Alembic database migrations
- Swagger API documentation
- RESTful API structure

---

# Tech Stack

- Python
- FastAPI
- SQLModel
- SQLAlchemy Async
- AsyncPG
- PostgreSQL
- Alembic

---

# Project Structure

```bash
fastapi-sqlmodel-alembic/
│
├── alembic/
│   ├── versions/
│
├── app/
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   └── __init__.py
│
├── .env
├── alembic.ini
├── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd fastapi-sqlmodel-alembic
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql+asyncpg://USER:PASSWORD@HOST/neondb
```

---

# Run FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

---

# Swagger API Docs

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/songs` | Get all songs |
| POST | `/songs` | Create new song |
| PUT | `/songs/{song_id}` | Update song |
| DELETE | `/songs/{song_id}` | Delete song |

---

# Alembic Migrations

## Generate Migration

```bash
python -m alembic revision --autogenerate -m "initial"
```

## Apply Migration

```bash
python -m alembic upgrade head
```

---

# Sample Request

## POST `/songs`

```json
{
  "name": "Believer",
  "artist": "Imagine Dragons"
}
```

# Learning Purpose

This project was created for learning modern FastAPI backend development with async PostgreSQL integration and database migrations.

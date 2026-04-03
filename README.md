# FastAPI Machine Test

## Overview

This project is a simple backend application built using FastAPI.
It provides CRUD (Create, Read, Update, Delete) operations for **Category** and **Product**.

Each product belongs to a category (One-to-Many relationship).

---

## Features

* Create, Read, Update, Delete APIs for Categories
* Create, Read, Update, Delete APIs for Products
* One category can have multiple products
* Pagination support in listing APIs
* Tested using FastAPI Swagger UI (`/docs`)

---

## Tech Stack

* Python 3.10+
* FastAPI
* SQLAlchemy
* SQLite (used for simplicity)

---

## Project Structure

```
fastapi_machine_test/
│
├── main.py          # Main FastAPI app
├── models.py        # Database models
├── schemas.py       # Pydantic schemas
├── crud.py          # Database operations
├── database.py      # DB connection setup
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/Bhibham17/fastapi_machine_test.git
cd fastapi_machine_test
```

---

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the server

```
python -m uvicorn main:app --reload
```

---

### 5. Open API Docs

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## API Usage (Basic Flow)

### 1. Create Category

POST `/categories`

```
{
  "name": "Electronics"
}
```

---

### 2. Create Product

POST `/products`

```
{
  "name": "iPhone",
  "category_id": 1
}
```

---

### 3. Get All Products

GET `/products`

---

### 4. Update Product

PUT `/products/{id}`

```
{
  "name": "iPhone 15",
  "category_id": 1
}
```

---

### 5. Delete Product

DELETE `/products/{id}`

---

## Notes

* SQLite database (`test.db`) is created automatically
* No extra setup required
* If needed, database can be switched to PostgreSQL easily

---

## Author

Bhibham


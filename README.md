# FastAPI Machine Test

## Overview

This project is a simple backend application built using FastAPI. It provides CRUD operations for Category and Product modules.

## Features

* Create, Read, Update, Delete (CRUD) for Categories
* Create, Read, Update, Delete (CRUD) for Products
* One-to-Many relationship (One Category → Many Products)
* Pagination for listing APIs
* Product API returns category details

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite (can be switched to PostgreSQL)

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the server:
   python -m uvicorn main:app --reload

3. Open in browser:
   http://127.0.0.1:8000/docs

## Database Design

* Category: id, name
* Product: id, name, category_id (Foreign Key)

Each product belongs to one category, and one category can have multiple products.

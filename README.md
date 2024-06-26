# Book Management System with FastAPI

This project implements a RESTful API for managing books and reviews using FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- CRUD operations for books (Create, Read, Update, Delete)
- CRUD operations for book reviews
- Book summaries and recommendations
- Secure communication with the database
- Basic authentication for API endpoints

## Requirements

- Python 3.8+
- PostgreSQL
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/book-management.git
   cd book-management

2 .Setup virtual environment:

python -m venv venv
. venv/bin/activate

3.Install dependencies:

pip install -r requirements.txt

4. Setup PostgreSQL database:

Create a PostgreSQL database named book_management.
Update the database URL in app/database.py if necessary.

5.Run the migrations:

alembic upgrade head

6. Start the FastAPI server:

uvicorn app.main:app --reload

7. Access the API:

The API documentation (Swagger UI) can be accessed at http://localhost:8000/docs.

8. API Endpoints
POST /books/: Add a new book.
GET /books/: Retrieve all books.
GET /books/{id}/: Retrieve a specific book by its ID.
PUT /books/{id}/: Update a book's information by its ID.
DELETE /books/{id}/: Delete a book by its ID.
POST /books/{id}/reviews/: Add a review for a book.
GET /books/{id}/reviews/: Retrieve all reviews for a book.
GET /books/{id}/summary/: Get a summary and aggregated rating for a book.
GET /recommendations/: Get book recommendations based on user preferences.
POST /generate-summary/: Generate a summary for a given book content.


9 . Authentication
Basic authentication is implemented for accessing the API endpoints. Use the following credentials:
Username: rajesh
Password: ramanathan
Include these credentials in the URL when making requests to authenticated endpoints:
http://rajesh:ramanathan@localhost:8000/books/

10.Security
Ensure to secure your database connection and credentials.
For production deployment, configure HTTPS for secure communication.

 

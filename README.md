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

11: Database Schema

books Table
Stores information about books.
Column	Type	Constraints	Description
id	SERIAL	PRIMARY KEY	Unique identifier for each book.
title	VARCHAR(255)	NOT NULL	Title of the book.
author	VARCHAR(255)	NOT NULL	Author of the book.
genre	VARCHAR(50)		Genre of the book (optional).
year_published	INT		Year the book was published (optional).
summary	TEXT		Summary or description of the book.
reviews Table
Stores reviews for books.
Column	Type	Constraints	Description
id	SERIAL	PRIMARY KEY	Unique identifier for each review.
book_id	INT	REFERENCES books(id)	Foreign key referencing the books table.
user_id	INT	NOT NULL	Identifier for the user who wrote the review.
review_text	TEXT		Text content of the review.
rating	INT	CHECK (rating >= 1 AND rating <= 5)	Rating given by the user (1 to 5).
Explanation:
books Table: Contains information about each book including its title, author, genre, publication year, and summary.
reviews Table: Stores reviews associated with each book. Each review is linked to a specific book (book_id), has a user identifier (user_id), textual content (review_text), and a rating (rating).
Notes:
Ensure proper indexing and foreign key constraints for optimal database performance and data integrity.
Adjust column sizes (e.g., VARCHAR lengths) based on your specific requirements and expected data.
This schema assumes a basic structure; you may extend it with additional tables (e.g., users, genres) or modify existing ones to suit more complex scenarios.


![Fast API swagger](https://github.com/RAMANATHAN-19/Book_management_assessment/assets/148554695/1ec7cbdb-a78d-4688-b540-2ad5686add31)


 
![Schemas](https://github.com/RAMANATHAN-19/Book_management_assessment/assets/148554695/9620ff92-6258-40da-8fc5-25964db85448)

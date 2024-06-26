from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from . import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "rajesh"
    correct_password = "ramanathan"

    if not (credentials.username == correct_username and credentials.password == correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), current_user: str = Depends(authenticate_user)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.update_book(db=db, book_id=book_id, book=book)

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud.delete_book(db=db, book_id=book_id)
    return {"message": "Book deleted successfully"}

@app.post("/books/{book_id}/reviews", response_model=schemas.Review)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db=db, review=review, book_id=book_id)

@app.get("/books/{book_id}/reviews/", response_model=List[schemas.Review])
def read_reviews(book_id: int, db: Session = Depends(get_db)):
    reviews = crud.get_reviews(db, book_id=book_id)
    return reviews

@app.get("/books/{book_id}/summary")
def get_book_summary(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book_summary(db=db, book_id=book_id)

@app.get("/recommendations/")
def get_recommendations(user_preferences: schemas.UserPreferences, db: Session = Depends(get_db)):
    return crud.get_recommendations(db=db, user_preferences=user_preferences)

@app.post("/generate-summary/")
def generate_summary(book_content: schemas.BookContent, db: Session = Depends(get_db)):
    return crud.generate_summary(db=db, book_content=book_content)

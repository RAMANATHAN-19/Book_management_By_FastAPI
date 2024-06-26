from sqlalchemy.orm import Session
from . import models, schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db.query(models.Book).filter(models.Book.id == book_id).delete()
    db.commit()

def create_review(db: Session, review: schemas.ReviewCreate, book_id: int):
    db_review = models.Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

def get_book_summary(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    reviews = db.query(models.Review).filter(models.Review.book_id == book_id).all()
    summary = book.summary
    avg_rating = sum(review.rating for review in reviews) / len(reviews) if reviews else 0
    return {"summary": summary, "average_rating": avg_rating}

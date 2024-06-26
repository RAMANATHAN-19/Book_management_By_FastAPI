from pydantic import BaseModel
from typing import Optional, List


class BookBase(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    year_published: Optional[int] = None
    summary: Optional[str] = None

    class Config:
        from_attributes = True


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class ReviewBase(BaseModel):
    book_id: int
    user_id: int
    review_text: str
    rating: int

    class Config:
        from_attributes = True


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int

    class Config:
        from_attributes = True


class UserPreferences(BaseModel):
    genre: Optional[str]
    author: Optional[str]
    year_published: Optional[int]


class BookContent(BaseModel):
    content: str

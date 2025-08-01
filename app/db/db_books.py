from sqlalchemy.orm import Session
from app.models.books import Book
from app.schemas.books import BookCreate


def create_book(db: Session, request: BookCreate):
    new_book = Book(
        id=request.id,
        title=request.title,
        content=request.content,
        author=request.author,
        published=request.published
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_book(db: Session):
    book = db.query(Book).all()
    return book
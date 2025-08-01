from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.books import BookCreate, BookResponse
from app.db.db_books import create_book, get_book

router = APIRouter(
    prefix="/books",
    tags=["books"],
)

@router.post('/create', response_model=BookResponse)
def create_books(request: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, request)

@router.get('/all', response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return get_book(db)
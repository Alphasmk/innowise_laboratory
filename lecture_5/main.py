"""FastAPI application for book collection management."""
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from database import get_db, Book
from schemas import BookCreate, BookUpdate, BookResponse

app = FastAPI(title="Book Collection API")


@app.post("/books/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Add a new book to the collection."""
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    """Get all books from the collection."""
    return db.scalars(select(Book)).all()


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID."""
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    db: Session = Depends(get_db)
):
    """Update book details."""
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    update_data = book_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(book, key, value)
    
    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search/", response_model=list[BookResponse])
def search_books(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db)
):
    """Search books by title, author, or year."""
    book = select(Book)
    
    if title:
        book = book.where(Book.title.contains(title))
    if author:
        book = book.where(Book.author.contains(author))
    if year:
        book = book.where(Book.year == year)
    
    return db.scalars(book).all()

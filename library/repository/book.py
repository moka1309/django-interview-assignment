from library import schemas, models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from library.repository import authentication


def create(request: schemas.Book, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    new_book = models.Book(
        name=request.name,
        author=request.author
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def update(book_id, request: schemas.Book, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    book = db.query(models.Book).filter(models.Book.id == book_id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book {id} is not found")
    book.update(request.dict(), synchronize_session=False)
    db.commit()

    return 'updated'


def destroy(book_id, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    book = db.query(models.Book).filter(models.Book.id == book_id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book {book_id} is not found")
    book.delete(synchronize_session=False)
    db.commit()
    
    return f"Book {book_id} deleted successfully!"


def all_books(db: Session):
    books = db.query(models.Book).all()
    return books


def show(book_id, db: Session):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book {book_id} not found!")
    return book

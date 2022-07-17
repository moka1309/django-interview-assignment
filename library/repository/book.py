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


def check_book(book_id, db):
    book = db.query(models.Book).filter(models.Book.id == book_id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book {book_id} not found!")

    return book


def update(book_id, request: schemas.Book, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    book = check_book(book_id, db)
    book.update(request.dict(), synchronize_session=False)
    db.commit()

    return 'updated'


def destroy(book_id, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    book = check_book(book_id, db)
    book.delete(synchronize_session=False)
    db.commit()
    
    return f"Book {book_id} deleted successfully!"


def all_books(db: Session):
    books = db.query(models.Book).all()
    return books


def show(book_id, db: Session):
    book = check_book(book_id, db)
    return book.first()


def borrow(book_id, db: Session, current_user: schemas.User):
    authentication.check_is_member(current_user)

    book = check_book(book_id, db)

    if book.first().status == "Borrowed":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Selected book is already borrowed!")

    db.query(models.Book).filter(models.Book.id == book_id).update({"status": "Borrowed"})
    db.commit()

    return "Book borrowed successfully!"


def return_update(book_id, db: Session, current_user: schemas.User):
    authentication.check_is_member(current_user)

    book = check_book(book_id, db)

    if book.first().status == "Available":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Selected book is already returned!")

    db.query(models.Book).filter(models.Book.id == book_id).update({"status": "Available"})
    db.commit()

    return "Book returned successfully!"

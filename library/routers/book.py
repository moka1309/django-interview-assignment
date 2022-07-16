from fastapi import APIRouter, status, Depends
from library import schemas, database, oauth2
from sqlalchemy.orm import Session
from library.repository import book
from typing import List

get_db = database.get_db


router = APIRouter(
    prefix="/book",
    tags=['books']
)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBook)
def create(request: schemas.Book, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.create(request, db, current_user)


@router.put('/{book_id}', status_code=status.HTTP_202_ACCEPTED)
def update(
        book_id, request: schemas.Book,
        db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return book.update(book_id, request, db, current_user)


@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(book_id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.destroy(book_id, db, current_user)


@router.get('', response_model=List[schemas.ShowBook])
def all_books(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.all_books(db)


@router.get('/{book_id}', status_code=200, response_model=schemas.ShowBook)
def show(book_id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return book.show(book_id, db)

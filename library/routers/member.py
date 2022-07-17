from fastapi import APIRouter, status, Depends
from library import schemas, database, oauth2
from sqlalchemy.orm import Session
from library.repository import member
from typing import List

get_db = database.get_db


router = APIRouter(
    prefix="/member",
    tags=['members']
)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.MemberUser, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return member.create(request, db, current_user)


@router.put('/{user_id}', status_code=status.HTTP_202_ACCEPTED)
def update(
        user_id, request: schemas.MemberUser,
        db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return member.update(user_id, request, db, current_user)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(user_id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return member.destroy(user_id, db, current_user)


@router.get('', response_model=List[schemas.ShowUser])
def all_members(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return member.all_members(db, current_user)


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(user_id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return member.show(user_id, db, current_user)


@router.delete('/delete/account', status_code=status.HTTP_204_NO_CONTENT)
def delete_account(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return member.delete_account(db, current_user)

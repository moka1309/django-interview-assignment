from fastapi import APIRouter, status, Depends
from library import schemas, database
from sqlalchemy.orm import Session
from library.repository import user

get_db = database.get_db


router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


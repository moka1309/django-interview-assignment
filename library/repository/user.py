from library import schemas, models
from sqlalchemy.orm import Session
from library.hashing import Hash
from fastapi import HTTPException, status
from library.repository import authentication


def create(request: schemas.User, db: Session):
    authentication.check_name_email_exist(request, db)

    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
        role=request.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

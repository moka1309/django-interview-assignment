from library import schemas, models
from sqlalchemy.orm import Session
from library.hashing import Hash


def create(request: schemas.User, db: Session):
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

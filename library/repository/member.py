from library import schemas, models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from library.repository import authentication
from library.hashing import Hash


def create(request: schemas.MemberUser, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    authentication.check_name_email_exist(request, db)

    print(f"incoming request {request}")
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    print(new_user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update(user_id, request: schemas.MemberUser, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {id} is not found")
    user.update(request.dict(), synchronize_session=False)
    db.commit()

    return 'updated'


def destroy(user_id, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {user_id} is not found")

    authentication.check_is_member(user.first())

    user.delete(synchronize_session=False)
    db.commit()

    return f"User {user_id} deleted successfully!"


def all_members(db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)
    users = db.query(models.User).all()
    return users


def show(user_id, db: Session, current_user: schemas.User):
    authentication.check_permission(current_user)

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found!")
    return user

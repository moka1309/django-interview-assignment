from fastapi import HTTPException, status
from library import schemas, models
from sqlalchemy.orm import Session


def check_permission(current_user):
    if not current_user.role == "LIBRARIAN":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Logged in user '{current_user.name}' don't have permission")


def check_is_member(current_user):
    if not current_user.role == "MEMBER":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Logged in user '{current_user.name}' don't have permission")


def check_name_email_exist(request, db: Session):
    data = db.query(models.User).filter(models.User.name == request.name).first()
    if data is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this name already exist"
        )

    data = db.query(models.User).filter(models.User.email == request.email).first()
    if data is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )

    return True

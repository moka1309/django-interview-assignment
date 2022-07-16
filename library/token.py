from jose import JWTError, jwt
from datetime import datetime, timedelta
from library import schemas, models

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user(db, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return schemas.UserInDB(name=user.name, email=user.email, role=user.role, hashed_password=user.password)


def verify_token(token: str, credentials_exception, db):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
        user = get_user(db, email=token_data.email)
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception

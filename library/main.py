from fastapi import FastAPI
from library import models
from library.database import engine
from library.routers import user, authentication, book, member


app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(book.router)
app.include_router(member.router)

from fastapi import FastAPI
from library import models
from library.database import engine
from library.routers import user


app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(user.router)

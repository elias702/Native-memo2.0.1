from fastapi import FastAPI
from .database import Base, engine
import api.router.memos as memos


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(memos.router)

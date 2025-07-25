from fastapi import FastAPI
from app.api.router import router as api_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.todo import TodoCreate, TodoRead, TodoUpdate
from app.services.todo_service import create_todo, get_todo, put_todo

router = APIRouter()

@router.post('/create')
async def create(req: TodoCreate, request: Request, db: Session = Depends(get_db)):
    resp = create_todo(req, db)
    return {"message": "Successfully Create Todo!", "data": resp}

@router.post('/update')
async def update(req: TodoUpdate, request: Request, db: Session = Depends(get_db)):
    resp = put_todo(req, db)
    return {"message": "Successfully Updated Todo!", "data": resp}

@router.post('/get')
async def get(req: TodoRead, request: Request, db: Session = Depends(get_db)):
    resp = get_todo(req, db)
    return {"message": "Successfully Get Todo!", "data": resp}
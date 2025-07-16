from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoRead, TodoUpdate

def create_todo(req: TodoCreate, db: Session):
    todo_model = Todo(**req.dict())
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

def put_todo(req: TodoUpdate, db: Session):
    db.query(Todo).filter(Todo.id == req.id).update(req.dict(exclude_unset=True))
    db.commit()
    return db.get(Todo, req.id)

def get_todo(req: TodoRead, db: Session):
    todo_model = db.get(Todo, req.id)
    return todo_model

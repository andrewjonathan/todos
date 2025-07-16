from fastapi.routing  import APIRouter
from .todo import router as todo_router

router = APIRouter()
router.include_router(todo_router, prefix="/todos", tags=["todos"])
from fastapi import Depends
from fastapi.routing  import APIRouter

from app.api.dependencies import get_current_user
from .v1.endpoints.todos import router as todo_router
from .v1.endpoints.users import router as user_router

router = APIRouter()
router.include_router(todo_router, prefix="/todos", tags=["todos"], dependencies=[Depends(get_current_user)])
router.include_router(user_router, prefix="/users", tags=["users"])
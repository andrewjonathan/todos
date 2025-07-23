from typing import Optional
from fastapi import APIRouter, HTTPException, Header, Request, Depends
from sqlalchemy.orm import Session
from starlette import status
from app.api.dependencies import get_current_user
from app.core.security.security import create_access_token, verify_password
from app.db.database import get_db
from app.schemas.user import UserAuth, UserCreate, UserRead
from app.services.user_service import get_user_by_username, get_user, register_user

router = APIRouter()

@router.post('/login')
async def auth(req: UserAuth, request: Request, db: Session = Depends(get_db)):
    user = get_user_by_username(req, db)
    if not user or not verify_password(req.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": str(user.id)})
    resp = {"access_token": access_token, "token_type": "bearer", "user": user}
    return {"message": "Successfully Login!", "data": resp}

@router.post('/register')
async def register(req: UserCreate, request: Request, db: Session = Depends(get_db)):
    resp = register_user(req, db)
    return {"message": "Successfully Registered User!", "data": resp}

@router.post('/me')
async def get(current_user = Depends(get_current_user)):
    resp = current_user
    return {"message": "Successfully Get User!", "data": resp}
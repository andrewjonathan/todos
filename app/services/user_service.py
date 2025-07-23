from sqlalchemy.orm import Session
from app.core.security.security import hash_password
from app.models.user import User
from app.schemas.user import UserAuth, UserCreate, UserRead

def register_user(req: UserCreate, db: Session):
    hashed_password = hash_password(req.password)
    req.password = hashed_password
    user_model = User(**req.dict())
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model

def get_user_by_username(req: UserAuth, db: Session):
    user_model = db.query(User).filter(User.username == req.username).first()
    return user_model

def get_user(req: UserRead, db: Session):
    user_model = db.get(User, req.id)
    return user_model

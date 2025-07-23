from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.security.security import verify_token
from app.models.user import User
from app.schemas.user import UserRead
from app.services.user_service import get_user

security = HTTPBearer()

# Dependency: Get current user (from Bearer Token)
def get_current_user(
        # token: str = Header(..., alias="Token", description="Bearer Token"),
        authorization: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)) -> User:
    try:
        token = authorization.credentials
        payload = verify_token(token)
        sub = payload.get("sub")
        user = get_user(UserRead(id=int(sub)), db)
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid token")

# Optional: Require superuser/admin access
def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return current_user
from sqlalchemy import Boolean, Column, Integer, String, DateTime, VARCHAR
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(VARCHAR(150))
    password = Column(VARCHAR(255))
    first_name = Column(VARCHAR(150))
    last_name = Column(VARCHAR(150))
    email = Column(VARCHAR(150))
    last_login = Column(DateTime)
    created_at = Column(DateTime)
    is_superuser = Column(Boolean)
    is_active = Column(Boolean)
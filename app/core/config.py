from pydantic import BaseSettings
import os
class Settings(BaseSettings):
    DB_HOST=os.getenv('DB_HOST', 'localhost')
    DB_PORT=os.getenv('DB_PORT', 5432)
    DB_PWD=os.getenv('DB_PWD', 'pwd')
    DB_NAME=os.getenv('DB_NAME', 'db_name')
    DB_USERNAME=os.getenv('DB_USERNAME', 'user_name')

    SECRET_KEY: str = "this-is-super-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
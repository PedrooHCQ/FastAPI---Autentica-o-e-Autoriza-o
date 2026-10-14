from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

DBBaseModel = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:admin@localhost:5432/faculdade"

    JWT_SECRET: str = "UdiNK3IjxPtE0AAs3-_7OZ5VvJhy0XvsB16gLrVdmBg"
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
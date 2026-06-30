from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = (
        "postgresql+psycopg://postgres:postgres@postgres:5432/jobtracker"
    )

    class Config:
        env_file = ".env"


settings = Settings()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    MongoClient: str
    MongoDB: str
    SECRET_KEY: str
    EMAIL_HOST: str
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str

    class Config:
        env_file = "../.env"

settings = Settings()

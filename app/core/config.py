from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "StudyRead"
    environment: str = "development"
    openai_api_key: str | None = None
    elevenlabs_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
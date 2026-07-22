from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str

    # Server
    HOST: str
    PORT: int

    # Database
    DATABASE_URL: str

    # Storage
    UPLOAD_FOLDER: str
    EXTRACTED_FOLDER: str
    TEMP_FOLDER: str

    # Logging
    LOG_LEVEL: str

    # OCR
    TESSERACT_PATH: str

    # Claude
    CLAUDE_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()
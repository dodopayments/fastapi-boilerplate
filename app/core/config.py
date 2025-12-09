from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DODO_PAYMENTS_API_KEY: str
    DODO_PAYMENTS_WEBHOOK_KEY: str
    DODO_PAYMENTS_RETURN_URL: str
    DODO_PAYMENTS_ENVIRONMENT: str

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

settings = Settings()

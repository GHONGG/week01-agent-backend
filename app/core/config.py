from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用配置：优先读 .env，其次读环境变量，最后用默认值"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "week01-agent-backend"
    debug: bool = False
    api_key: str = ""
    host: str = "127.0.0.1"
    port: int = 8000


settings = Settings()

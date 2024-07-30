from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True
    )
    
    # FIREBASE CONFIGURATION
    API_KEY : str
    AUTH_DOMAIN : str
    PROJECT_ID : str
    STORAGE_BUCKET : str
    MESSAGING_SENDER_ID : str
    APP_ID : str
    MEASUREMENT_ID : str
    
    # FASTAPI ARGS INIALIZATION
    APPLICATION_TITLE: str
    API_VERSION: str
    DOCS_URL: str
    
    @property
    def FIREBASE_CREDENTIALS(self) -> dict:
        return {
            "apiKey": self.API_KEY,
            "authDomain": self.AUTH_DOMAIN,
            "projectId": self.PROJECT_ID,
            "storageBucket": self.STORAGE_BUCKET,
            "messagingSenderId": self.MESSAGING_SENDER_ID,
            "appId": self.APP_ID,
            "measurementId": self.MEASUREMENT_ID
        }
    
    @property
    def FASTAPI_CONFIG_ARGS(self) -> dict:
        return {
            "title": self.APPLICATION_TITLE,
            "version": self.API_VERSION,
            "docs_url": self.DOCS_URL
        }
    


settings = Settings()
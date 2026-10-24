from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    app_name: str = "Language Learning Reader"
    debug: bool = False
    



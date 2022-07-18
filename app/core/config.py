
from typing import Any, Dict, List, Optional, Union
from dotenv import dotenv_values
from pydantic import AnyHttpUrl, BaseSettings, validator

configEnv = dotenv_values(".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_DATABASE: str
    DATABASE_URI: Optional[str] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql://{configEnv['MYSQL_USER']}:{configEnv['MYSQL_PASSWORD']}@{configEnv['MYSQL_HOST']}:" \
               f"{configEnv['MYSQL_PORT']}/{configEnv['MYSQL_DATABASE']}"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

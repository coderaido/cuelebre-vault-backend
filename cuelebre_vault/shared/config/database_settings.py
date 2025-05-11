from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

from cuelebre_vault.shared.constants import Paths


class DatabaseSettings(BaseSettings):

    driver: str = Field("postgresql+asyncpg", validation_alias="DATABASE_DRIVER")
    host: str = Field("localhost", validation_alias="DATABASE_HOST")
    port: int = Field(5432, validation_alias="DATABASE_PORT")
    name: str = Field("postgres", validation_alias="DATABASE_NAME")
    user: str = Field("postgres", validation_alias="DATABASE_USER")
    password: SecretStr = Field(..., validation_alias="DATABASE_PASSWORD")

    model_config = SettingsConfigDict(env_file=Paths.ROOT.joinpath(".env"), extra="ignore")

    @property
    def url(self) -> URL:
        return URL.create(
            drivername=self.driver,
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password.get_secret_value(),
            database=self.name,
        )


database_settings: DatabaseSettings = DatabaseSettings()

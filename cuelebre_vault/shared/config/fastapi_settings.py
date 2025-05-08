from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from cuelebre_vault.shared.constants import Paths


class FastApiSettings(BaseSettings):
    openapi_url: str | None = Field("/openapi.json", validation_alias="FASTAPI_OPENAPI_URL")
    openapi_prefix: str | None = Field("", validation_alias="FASTAPI_OPENAPI_PREFIX")
    root_path: str | None = Field("", validation_alias="FASTAPI_ROOT_PATH")
    root_path_in_servers: bool | None = Field(False, validation_alias="FASTAPI_ROOT_PATH_IN_SERVERS")
    debug: bool | None = Field(False, validation_alias="FASTAPI_DEBUG")
    docs_url: str | None = Field("/docs", validation_alias="FASTAPI_DOCS_URL")
    redoc_url: str | None = Field("/redoc", validation_alias="FASTAPI_REDOC_URL")

    model_config = SettingsConfigDict(env_file=Paths.ROOT.joinpath(".env"), extra="ignore")


fastapi_settings: FastApiSettings = FastApiSettings()

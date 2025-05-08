from pydantic_settings import BaseSettings, SettingsConfigDict

from cuelebre_vault.shared.constants import Paths


class DatabaseSettings(BaseSettings):

    model_config = SettingsConfigDict(env_file=Paths.ROOT.joinpath(".env"), extra='ignore')

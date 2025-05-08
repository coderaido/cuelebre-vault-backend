from fastapi import FastAPI

from cuelebre_vault.shared.config.metadata import tags_metadata, description, summary, license_info
from . import __version__
from .shared.config.fastapi_settings import fastapi_settings

app = FastAPI(
    title="💰 Cuelebre Vault API",
    description=description,
    summary=summary,
    version=__version__,
    openapi_tags=tags_metadata,
    license_info=license_info,
    **fastapi_settings.model_dump(),
)

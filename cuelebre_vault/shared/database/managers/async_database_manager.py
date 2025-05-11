from typing import AsyncGenerator

from sqlalchemy import URL, Engine
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker

from cuelebre_vault.shared.config.database_settings import database_settings


class AsyncDatabaseManager:

    def __init__(self, url: str | URL, **kwargs):

        self.__engine: AsyncEngine = create_async_engine(url, **kwargs)
        self.__session_factory: async_sessionmaker = async_sessionmaker(self.__engine, expire_on_commit=True)

    @property
    def async_engine(self) -> AsyncEngine:
        return self.__engine

    @property
    def sync_engine(self) -> Engine:
        return self.__engine.sync_engine

    @property
    def async_session_factory(self) -> async_sessionmaker[AsyncSession]:
        return self.__session_factory

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, ...]:
        async with self.__session_factory() as session:
            session: AsyncSession
            yield session


async_database_manager: AsyncDatabaseManager = AsyncDatabaseManager(database_settings.async_url)

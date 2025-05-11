from typing import Generator, Any

from sqlalchemy import URL, create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from cuelebre_vault.shared.config.database_settings import database_settings


class DatabaseManager:
    def __init__(self, url: str | URL, **kwargs):
        self.__engine: Engine = create_engine(url, **kwargs)
        self.__session_factory: sessionmaker = sessionmaker(self.__engine, expire_on_commit=True)

    @property
    def engine(self) -> Engine:
        return self.__engine

    @property
    def session_factory(self) -> sessionmaker[Session]:
        return self.__session_factory

    def get_session(self) -> Generator[Session, Any, None]:
        with self.__session_factory as session:
            session: Session
            yield session


database_manager: DatabaseManager = DatabaseManager(database_settings.url)

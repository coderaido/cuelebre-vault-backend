from sqlalchemy.orm import DeclarativeBase, declared_attr

from cuelebre_vault.shared.utils.strings import camel_to_snake


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls):
        return camel_to_snake(cls.__name__)

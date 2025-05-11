from datetime import datetime

from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, declarative_mixin

from cuelebre_vault.database.models.base import Base


@declarative_mixin
class BaseAuditable(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now, nullable=False, comment="Creation date"
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now,
        server_onupdate=func.now,
        nullable=False,
        comment="Last row update",
    )

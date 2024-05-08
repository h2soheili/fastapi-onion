from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, DateTime, func, Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped, declared_attr
from sqlalchemy.orm import mapped_column

from core.api.converter.BaseSerializer import BaseSerializer


class BaseEntity(AsyncAttrs, DeclarativeBase, BaseSerializer):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    __name__: str
    __table_args__ = {"extend_existing": True}

    date_created: Mapped[Optional[datetime]] = mapped_column(DateTime, default=func.current_timestamp(),
                                                             nullable=True)
    date_modified: Mapped[Optional[datetime]] = mapped_column(DateTime, default=func.current_timestamp(),
                                                              onupdate=func.current_timestamp(), nullable=True, )
    date_archived: Mapped[Optional[datetime]] = mapped_column(DateTime, default=None, nullable=True)

    create_by_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id'))
    create_by = relationship("UserEntity")

    updated_by_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id'))
    updated_by = relationship("UserEntity")

    archived_by_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id'))
    archived_by = relationship("UserEntity")

    __mapper_args__ = {"eager_defaults": True}

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

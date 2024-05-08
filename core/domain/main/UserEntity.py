from sqlalchemy import String, Integer, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.domain.main.BaseEntity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(120), nullable=True)
    last_name: Mapped[str] = mapped_column(String(120), nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    username: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(120), nullable=True)
    role_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('role.id'))
    role = relationship("RoleEntity")
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=0, index=True)

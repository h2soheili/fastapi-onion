from typing import Optional

from sqlalchemy import String, Integer, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.domain.main.BaseEntity import BaseEntity


class RoleEntity(BaseEntity):
    __tablename__ = "role"
    parent_role_id: Mapped[Optional[int]] = mapped_column(BigInteger, ForeignKey('role.id'))
    parent_role = relationship("RoleEntity")
    label: Mapped[str] = mapped_column(String(120), nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=0, index=True)

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.main.BaseEntity import BaseEntity


class AutomobileEntity(BaseEntity):
    __tablename__ = 'automobile'

    manufacture: Mapped[str] = mapped_column(String(80), nullable=True, index=False)
    type: Mapped[str] = mapped_column(String(80), nullable=True, index=False)
    model: Mapped[str] = mapped_column(String(80), nullable=True, index=False)

    state: Mapped[int] = mapped_column(Integer, nullable=False, default=0, index=True)

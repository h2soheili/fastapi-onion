from typing import Generic, Optional, Type, TypeVar, Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from core.domain.main.BaseEntity import BaseEntity
from core.service_app.configs.Logger import get_logger_gn
from core.service_app.configs.SQLDatabase import async_db_session

ModelType = TypeVar("ModelType", bound=BaseEntity)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType],
                 logger=Depends(get_logger_gn(__name__), use_cache=True)):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

        self.logger = logger

    def get(self,
            entity_id: int,
            state: int,
            session: Annotated[Session, Depends(async_db_session)], ) -> Optional[ModelType]:
        query = session.query(self.model)
        query = query.where(self.model.id == entity_id)
        if state:
            query = query.where(self.model.state == state)
        return query.first()

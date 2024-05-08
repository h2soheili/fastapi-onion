from typing import Any

from fastapi import HTTPException


class BaseServiceException(HTTPException):
    def __init__(self, status: int, code: int, message: str, data: Any = None):
        self.status = status
        self.code = code
        self.message = message
        self.data = data
        self.detail = {"code": code, "message": message, "data": data}
        super().__init__(status_code=status, detail=self.detail)

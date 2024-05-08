from core.domain.exception.BaseServiceException import BaseServiceException


class ErrorMessages:
    HTTP_NOT_AUTHENTICATED = BaseServiceException(401, 401, "HTTP_NOT_AUTHENTICATED")
    HTTP_BAD_REQUEST = BaseServiceException(402, 402, "HTTP_BAD_REQUEST")
    HTTP_NOT_AUTHORIZED = BaseServiceException(403, 403, "HTTP_NOT_AUTHORIZED")
    HTTP_NOT_FOUND = BaseServiceException(404, 404, "HTTP_NOT_FOUND")
    HTTP_INTERNAL_SERVER_ERROR = BaseServiceException(500, 500, "HTTP_INTERNAL_SERVER_ERROR")

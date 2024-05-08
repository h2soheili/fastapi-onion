from typing import Tuple, Any


class GetPaginatedListRequestDTO:
    def __init__(self,
                 content: Tuple[Any],
                 page: int = 0,
                 size: int = 100,
                 total_element: int = 0,
                 ):
        self.content = content
        self.page = page
        self.size = size
        self.total_element = total_element

from typing import Union, Tuple


class GetPaginatedListRequestDTO:
    def __init__(self,
                 filters: Union[str, None] = None,
                 page: int = 0,
                 size: int = 100,
                 sorts: Tuple[Tuple[str]] = (('id', 'asc'),)
                 ):
        self.filters = filters
        self.page = page
        self.size = size
        self.sorts = sorts

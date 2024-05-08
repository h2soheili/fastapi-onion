from typing import List, Any

from sqlalchemy.inspection import inspect


class BaseSerializer(object):

    def serialize(self):
        serialized = {}
        for c in inspect(self).attrs.keys():
            serialized[c] = getattr(self, c)
        return serialized

    @staticmethod
    def serialize_list(rows: List[Any]):
        return [r.serialize() for r in rows]

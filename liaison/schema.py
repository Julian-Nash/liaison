from typing import Tuple, List
from inspect import getmembers

from .namespace import Namespace
from .fields.base import Field


class Schema:
    """Schema class. Inherit and define your own schemas"""

    @classmethod
    def _get_fields(cls) -> List[Tuple[str, Field]]:
        return getmembers(cls, predicate=lambda x: isinstance(x, Field))

    @classmethod
    def parse(cls, data: dict) -> Namespace:
        """Given a dictionary (data), parses and returns a Namespace containing attributes defined
        as Fields on the Schema.

        :param data: A dict or dict like object to parse
        :returns: A Namespace object
        """
        ns_kwargs = {}

        for key, field in cls._get_fields():
            raw_value = data.get(key)
            ns_kwargs[key] = field.validate(key, raw_value)

        return Namespace(**ns_kwargs)

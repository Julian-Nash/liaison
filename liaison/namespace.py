from argparse import Namespace as _Namespace
from typing import Optional, Any, Sequence


class Namespace(_Namespace):
    """Simple namespace object returned when parsing a Schema"""

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get an attribute from the namespace, provide an optional default value"""
        return getattr(self, key, default)

    def to_dict(self, exclude: Optional[Sequence] = None) -> dict:
        """Returns the Namespace as a dictionary. An optional `exclude` param can be supplied
        to exclude values from the response.

        :param exclude: An optional sequence of values to exclude
        :returns: A dictionary of the Namespace keys and values
        """
        return {
            k: getattr(self, k)
            for k, v in vars(self).items()
            if k not in set(exclude or [])
        }

from typing import Optional, Any, Sequence, Callable

from .base import Field
from .mixins import SizedFieldMixin


class StringField(SizedFieldMixin, Field):
    """ Field for declaring strings """

    def __init__(
            self,
            required: Optional[bool] = False,
            default: Optional[Any] = None,
            choices: Optional[Sequence[str]] = None,
            validator: Optional[Callable] = None,
            min_len: Optional[int] = None,
            max_len: Optional[int] = None
    ):
        super().__init__(
            type=str,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_len=min_len,
            max_len=max_len
        )

    def validate(self, key, value):
        return super().validate(key, value)


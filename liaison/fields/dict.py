from typing import Optional, Any, Sequence, Callable

from .base import Field
from .mixins import SizedFieldMixin
from liaison.exceptions import ValidationError


class DictField(SizedFieldMixin, Field):
    def __init__(
        self,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
        min_len: Optional[int] = None,
        max_len: Optional[int] = None,
    ):
        super().__init__(
            type=dict,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_len=min_len,
            max_len=max_len,
        )

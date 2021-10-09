from typing import Optional, Any, Sequence, Callable
import re

from .base import Field
from .mixins import SizedFieldMixin
from ..exceptions import ValidationError


class StringField(SizedFieldMixin, Field):
    """Field for declaring strings"""

    def __init__(
        self,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
        min_len: Optional[int] = None,
        max_len: Optional[int] = None,
        regex: Optional[str] = None
    ):
        super().__init__(
            type=str,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_len=min_len,
            max_len=max_len,
        )
        self.regex = re.compile(regex) if regex else None

    def validate(self, key, value):
        if self.regex:
            if not self.regex.match(value):
                raise ValidationError(
                    f"Invalid pattern for '{key}', must match pattern '{self.regex.pattern}'"
                )
        return super().validate(key, value)

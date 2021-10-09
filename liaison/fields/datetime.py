from typing import Optional, Any, Sequence, Callable
from datetime import datetime

from .base import Field
from ..exceptions import ValidationError


class DateTimeField(Field):
    """Field for declaring datetime objects"""

    def __init__(
        self,
        date_format: str,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
    ):
        super().__init__(
            type=datetime,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
        )
        self.date_format = date_format

    def _cast_type(self, key, value: Any):
        try:
            value = datetime.strptime(value, self.date_format)
        except ValueError:
            raise ValidationError(
                f"Invalid value for '{key}', must match format '{self.date_format}'"
            )
        return value

    def validate(self, key, value):
        return super().validate(key, value)

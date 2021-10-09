from typing import Optional, Any, Sequence, Callable

from .base import Field
from liaison.exceptions import ValidationError


class BoolField(Field):
    """Field for declaring booleans"""

    def __init__(
        self,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
    ):
        super().__init__(
            type=bool,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
        )

    def _cast_type(self, key, value):
        if not isinstance(value, bool):
            raise ValidationError(
                f"Invalid type '{type(value)}' for parameter '{key}'. Value must be a boolean"
            )
        return super()._cast_type(key, value)

    def validate(self, key, value):
        return super().validate(key, value)

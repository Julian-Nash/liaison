from typing import Optional, Any, Sequence, Callable

from .base import Field
from liaison.exceptions import ValidationError


class BoolField(Field):
    """ Field for declaring booleans """

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

    def validate(self, key, value):
        if value not in (True, False):
            raise ValidationError('')
        return super().validate(key, value)


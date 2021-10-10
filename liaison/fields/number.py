from typing import Optional, Any, Sequence, Callable
from numbers import Number

from .base import Field
from .mixins import NumericFieldMixin


class NumberField(NumericFieldMixin, Field):
    """Base class for numerical fields"""

    def __init__(
        self,
        type: type,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
        min_val: Optional[Number] = None,
        max_val: Optional[Number] = None,
    ):
        super().__init__(
            type=type,
            input_types=(int, float, str),
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_val=min_val,
            max_val=max_val,
        )


class IntField(NumberField):
    """Integer field"""

    def __init__(
        self,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
        min_val: Optional[Number] = None,
        max_val: Optional[Number] = None,
    ):
        super().__init__(
            type=int,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_val=min_val,
            max_val=max_val,
        )


class FloatField(NumberField):
    """Float field"""

    def __init__(
        self,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
        min_val: Optional[Number] = None,
        max_val: Optional[Number] = None,
    ):
        super().__init__(
            type=float,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_val=min_val,
            max_val=max_val,
        )

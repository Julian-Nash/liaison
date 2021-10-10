from typing import Optional, Any, Sequence, Callable, Union

from .base import Field
from .mixins import SizedFieldMixin
from liaison.exceptions import ValidationError


class SequenceField(SizedFieldMixin, Field):
    def __init__(
        self,
        type: type,
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence[str]] = None,
        validator: Optional[Callable] = None,
        min_len: Optional[int] = None,
        max_len: Optional[int] = None,
    ):
        super().__init__(
            type=type,
            input_types=(list,),
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_len=min_len,
            max_len=max_len,
        )


class ListField(SequenceField):
    """Field for declaring lists"""

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
            type=list,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_len=min_len,
            max_len=max_len,
        )


class SetField(SequenceField):
    """Field for declaring sets. The list will be parsed and returned as a set"""

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
            type=set,
            required=required,
            default=default,
            choices=choices,
            validator=validator,
            min_len=min_len,
            max_len=max_len,
        )

    def _cast_type(self, key, value):
        return super()._cast_type(key, set(value))

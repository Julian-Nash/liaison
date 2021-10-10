from typing import Optional, Any
from numbers import Number

from liaison.exceptions import ValidationError


class FieldMixin:
    """Field mixin base class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, key, value: Any):
        return super().validate(key, value)


class SizedFieldMixin(FieldMixin):
    """Mixin for sized fields"""

    def __init__(
        self, min_len: Optional[int] = None, max_len: Optional[int] = None, **kwargs
    ):
        self.min_len = min_len
        self.max_len = max_len
        super().__init__(**kwargs)

    def validate(self, key, value: Any):
        if value is not None:
            if any((self.min_len, self.max_len)) and not hasattr(value, "__len__"):
                raise ValidationError(
                    f"Invalid value for '{key}', expecting '{self.type.__name__}'"
                )

            if self.min_len and len(value) < self.min_len:
                raise ValidationError(
                    f"Value for '{key}' did not meet required length of {self.min_len}"
                )
            if self.max_len and len(value) > self.max_len:
                raise ValidationError(
                    f"Value for '{key}' exceeded maximum length of {self.max_len}"
                )
        return super().validate(key, value)


class NumericFieldMixin(FieldMixin):
    """Mixin for numeric fields"""

    def __init__(
        self,
        min_val: Optional[Number] = None,
        max_val: Optional[Number] = None,
        **kwargs,
    ):
        self.min_val = min_val
        self.max_val = max_val
        super().__init__(**kwargs)

    def _check_type(self, key, value: Any):
        try:
            int(value)
        except ValueError:
            raise ValidationError(
                f"Incorrect type '{type(value).__name__}' for '{key}', expecting a number"
            )

    def validate(self, key, value: Any):
        if value is not None:
            self._check_type(key, value)
            if self.min_val and value < self.min_val:
                raise ValidationError(
                    f"Value for '{key}' must be at least {self.min_val}"
                )
            if self.max_val and value > self.max_val:
                raise ValidationError(
                    f"Value for '{key}' must be less than {self.max_val}"
                )
        return super().validate(key, value)

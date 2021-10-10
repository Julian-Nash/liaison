from typing import Any, Optional, Callable, Sequence, Tuple
from inspect import signature

from liaison.exceptions import SchemaException, ValidationError


class Field:
    """Base class for all Field types"""

    def __init__(
        self,
        type: type,
        input_types: Tuple[type],
        required: Optional[bool] = False,
        default: Optional[Any] = None,
        choices: Optional[Sequence] = None,
        validator: Optional[Callable] = None,
        strict_type: Optional[bool] = False,
    ):
        self.type = type
        self.required = required
        self.default = default
        self.choices = set(choices) if choices else None
        if validator:
            self._check_validator_signature(validator)
        self._validator = validator
        self.strict_type = strict_type
        self.input_types = input_types

    def _check_validator_signature(self, func: Callable):
        if not callable(func):
            raise TypeError(f"validators must be callable, not '{type(func)}'")
        if len(signature(func).parameters) != 3:
            raise SchemaException(
                f"validator method signature must match (self, key, value)"
            )

    def validator(self, func: Callable):
        """Validation decorator"""
        self._check_validator_signature(func)
        self._validator = func

    def _cast_type(self, key, value: Any):

        if isinstance(value, self.type):
            return value

        if type(value) not in self.input_types:
            raise ValidationError(
                f"Incorrect type '{type(value).__name__}' for '{key}', expecting '{self.type.__name__}'"
            )

        if self.strict_type and not isinstance(value, self.type):
            raise ValidationError(
                f"Incorrect type '{type(value).__name__}' for '{key}', expecting '{self.type.__name__}'"
            )

        try:
            value = self.type(value)
        except (TypeError, ValueError):
            raise ValidationError(
                f"Invalid type '{type(value).__name__}' for '{key}', expecting '{self.type.__name__}'"
            )
        return value

    def validate(self, key: str, value: Any) -> Any:
        """Validates the field"""

        if self._validator:
            return self._validator(self, key, value)

        if self.required and value is None:
            raise ValidationError(f"Missing required value for '{key}'")

        if value is not None:
            value = self._cast_type(key, value)

        if self.choices and value not in self.choices:
            raise ValidationError(f"Invalid choice '{value}' for '{key}'")

        if value is None and self.default:
            if callable(self.default):
                return self.default()
            return self.default

        return value

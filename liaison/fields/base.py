from typing import Any, Optional, Callable, Sequence
from inspect import signature

from liaison.exceptions import SchemaException, ValidationError


class Field:
    """ Base class for all Field types """

    def __init__(
            self,
            type: type,
            required: Optional[bool] = False,
            default: Optional[Any] = None,
            choices: Optional[Sequence] = None,
            validator: Optional[Callable] = None,
            strict_type: Optional[bool] = False
    ):
        self.type = type
        self.required = required
        self.default = default
        self.choices = set(choices) if choices else None
        if validator:
            self._check_validator_signature(validator)
        self._validator = validator
        self.strict_type = strict_type

    def _check_validator_signature(self, func: Callable):
        if not callable(func):
            raise TypeError(f"validators must be callable, not '{type(func)}'")
        if len(signature(func).parameters) != 3:
            raise SchemaException(f"validator method signature must match (self, key, value)")

    def validator(self, func: Callable):
        """ Validation decorator """
        self._check_validator_signature(func)
        self._validator = func

    def validate(self, key: str, value: Any) -> Any:
        """ Validates the field value """

        if self._validator:
            return self._validator(self, key, value)

        if self.required and value is None:
            raise ValidationError(f"Missing required parameter '{key}'")

        if value is not None:

            if self.strict_type and type(value) != self.type:
                raise ValidationError(
                    f"Incorrect type '{type(value)}' for parameter '{key}', expecting '{self.type}'"
                )

            try:
                value = self.type(value)
            except (TypeError, ValueError):
                raise ValidationError(
                    f"Incorrect type '{type(value)}' for parameter '{key}', expecting '{self.type}'"
                )

        if self.choices and value not in self.choices:
            raise ValidationError(f"Invalid choice for parameter '{key}'")

        return value or self.default

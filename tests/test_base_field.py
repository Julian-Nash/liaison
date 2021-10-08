import pytest

from liaison.fields.base import Field
from liaison.exceptions import ValidationError, SchemaException


def test_field():
    field = Field(type=str)
    value = field.validate("foo", "bar")
    assert value == "bar"


def test_field_raises_exception_incorrect_type():
    # Note - All fields have a test for their respective type conversion
    field = Field(type=int)
    with pytest.raises(ValidationError):
        value = field.validate("foo", "bar")


def test_field_casts_to_type():
    field = Field(type=str)
    value = field.validate("foo", 1)
    assert value == "1"


def test_field_raises_exception_with_strict_type():
    field = Field(type=int, strict_type=True)
    with pytest.raises(ValidationError):
        value = field.validate("foo", "1")


def test_field_with_required():
    field = Field(type=str, required=True)
    value = field.validate("foo", "bar")
    assert value == "bar"


def test_field_with_required_raises_error():
    field = Field(type=str, required=True)
    with pytest.raises(ValidationError):
        field.validate("foo", None)


def test_field_with_default():
    field = Field(type=str, default="DEFAULT")
    value = field.validate("foo", None)
    assert value == "DEFAULT"


def test_field_with_choices():
    field = Field(type=str, choices=["Hello", "World"])
    value = field.validate("foo", "Hello")
    assert value == "Hello"


def test_field_with_choices_raises_error():
    field = Field(type=str, choices=["Hello", "World"])
    with pytest.raises(ValidationError):
        field.validate("foo", "Bar")


def test_field_with_validator():

    def my_validator(field_cls, key, value):  # pragma: no cover
        if value == "FOO":
            raise ValidationError("Value cannot be FOO")
        return value

    field = Field(type=str, validator=my_validator)
    value = field.validate("Hello", "World")
    assert value == "World"


def test_field_with_incorrect_validator_type():
    with pytest.raises(TypeError):
        field = Field(type=str, validator="foo")


def test_field_with_validator_raises_error():

    def my_validator(field_cls, key, value):  # pragma: no cover
        if value == "FOO":
            raise ValidationError("Value cannot be FOO")
        return value

    field = Field(type=str, validator=my_validator)
    with pytest.raises(ValidationError):
        value = field.validate("Hello", "FOO")


def test_field_with_validator_using_decorator():

    field = Field(type=str)

    @field.validator
    def my_validator(field_cls, key, value):  # pragma: no cover
        if value == "FOO":
            raise ValidationError("Value cannot be FOO")
        return value

    value = field.validate("Hello", "Bar")
    assert value == "Bar"


def test_field_with_validator_using_decorator_raises_error():

    field = Field(type=str)

    @field.validator
    def my_validator(field_cls, key, value):  # pragma: no cover
        if value == "FOO":
            raise ValidationError("Value cannot be FOO")
        return value

    with pytest.raises(ValidationError):
        value = field.validate("Hello", "FOO")


def test_field_with_validator_decorator_raises_exception_with_bad_signature():

    field = Field(type=str)

    with pytest.raises(SchemaException):

        @field.validator
        def my_validator(key, value):  # pragma: no cover
            if value == "FOO":
                raise ValidationError("Value cannot be FOO")
            return value

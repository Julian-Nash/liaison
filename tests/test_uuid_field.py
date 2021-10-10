import uuid

import pytest

from liaison.fields import UUIDField
from liaison.exceptions import ValidationError


def test_field():
    expected = str(uuid.uuid4())
    field = UUIDField()
    value = field.validate("uuid", expected)
    assert value == expected


def test_field_with_none_value():
    field = UUIDField()
    value = field.validate("uuid", None)
    assert value is None


def test_field_raises_validation_error_with_int():
    field = UUIDField()
    with pytest.raises(ValidationError):
        value = field.validate("foo", 1)


def test_field_raises_validation_error_with_str():
    field = UUIDField()
    with pytest.raises(ValidationError):
        value = field.validate("foo", "1")

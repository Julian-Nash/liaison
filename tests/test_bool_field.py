import pytest

from liaison.fields import BoolField
from liaison.exceptions import ValidationError


def test_field():
    field = BoolField()
    value = field.validate("foo", True)
    assert value is True

    field = BoolField()
    value = field.validate("foo", False)
    assert value is False


def test_field_raises_error_with_wrong_value_type():
    field = BoolField()
    with pytest.raises(ValidationError):
        value = field.validate("foo", 1)
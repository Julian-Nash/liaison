import pytest

from liaison.fields import DictField
from liaison.exceptions import ValidationError


def test_field():
    field = DictField()
    value = field.validate("foo", {"a": 1, "b": 2, "c": 3})
    assert value == {"a": 1, "b": 2, "c": 3}


def test_field_raises_validation_error():
    field = DictField()
    with pytest.raises(ValidationError):
        value = field.validate("foo", "{'hello': 'world'}")

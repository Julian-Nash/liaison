import pytest

from liaison.fields import IntField
from liaison.exceptions import ValidationError


def test_field():
    field = IntField()
    value = field.validate("foo", 1)
    assert value == 1


def test_field_with_min_val():
    field = IntField(min_val=5)
    value = field.validate("foo", 6)
    assert value == 6


def test_field_with_min_val_no_value():
    field = IntField(min_val=5)
    value = field.validate("foo", None)
    assert value is None


def test_field_with_min_val_empty_String():
    field = IntField(min_val=5)
    with pytest.raises(ValidationError):
        value = field.validate("foo", "")


def test_field_with_min_len_raises_exception():
    field = IntField(min_val=5)
    with pytest.raises(ValidationError):
        value = field.validate("foo", 1)


def test_field_with_max_val():
    field = IntField(max_val=5)
    value = field.validate("foo", 1)
    assert value == 1


def test_field_with_max_val_raises_exception():
    field = IntField(max_val=5)
    with pytest.raises(ValidationError):
        value = field.validate("foo", 6)

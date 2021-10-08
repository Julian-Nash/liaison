import pytest

from liaison.fields import FloatField
from liaison.exceptions import ValidationError


def test_field():
    field = FloatField()
    value = field.validate("foo", 1)
    assert value == 1


def test_field_with_min_val():
    field = FloatField(min_val=5.5)
    value = field.validate("foo", 6)
    assert value == 6


def test_field_with_min_len_raises_exception():
    field = FloatField(min_val=5.5)
    with pytest.raises(ValidationError):
        value = field.validate("foo", 5)


def test_field_with_max_val():
    field = FloatField(max_val=5.5)
    value = field.validate("foo", 5)
    assert value == 5


def test_field_with_max_val_raises_exception():
    field = FloatField(max_val=5.51)
    with pytest.raises(ValidationError):
        value = field.validate("foo", 5.6)

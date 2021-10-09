import pytest

from liaison.fields import ListField, SetField
from liaison.exceptions import ValidationError


def test_field():
    field = ListField()
    value = field.validate("foo", [1, 2, 3])
    assert value == [1, 2, 3]


def test_list_field_incorrect_type_raises_validation_error():
    field = ListField()
    with pytest.raises(ValidationError):
        value = field.validate("foo", "bar")


def test_field_min_len_raises_error():
    field = ListField(min_len=3)
    with pytest.raises(ValidationError):
        value = field.validate("foo", [1, 2])


def test_field_max_len_raises_error():
    field = ListField(max_len=3)
    with pytest.raises(ValidationError):
        value = field.validate("foo", [1, 2, 3, 4])


def test_set_field():
    field = SetField()
    value = field.validate("foo", [1, 1, 2, 3, 3])
    assert value == {1, 2, 3}

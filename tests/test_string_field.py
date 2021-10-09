import pytest

from liaison.fields import StringField
from liaison.exceptions import ValidationError, SchemaException


def test_field():
    field = StringField()
    value = field.validate("foo", "bar")
    assert value == "bar"


def test_field_converts_type():
    field = StringField()
    value = field.validate("foo", 1)
    assert value == "1"


def test_field_with_min_len():
    field = StringField(min_len=5)
    value = field.validate("foo", "barbar")
    assert value == "barbar"


def test_field_with_min_len_raises_exception():
    field = StringField(min_len=5)
    with pytest.raises(ValidationError):
        value = field.validate("foo", "bar")


def test_field_with_max_len():
    field = StringField(max_len=5)
    value = field.validate("foo", "bar")
    assert value == "bar"


def test_field_with_max_len_raises_exception():
    field = StringField(max_len=5)
    with pytest.raises(ValidationError):
        value = field.validate("foo", "barbar")


def test_field_with_regex_succeeds():
    field = StringField(regex="123abc")
    value = field.validate("foo", "123abc")
    assert value == "123abc"


def test_field_with_regex_raises_validation_error():
    field = StringField(regex="123abc")
    with pytest.raises(ValidationError):
        value = field.validate("foo", "bar")

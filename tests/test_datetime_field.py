import datetime

import pytest

from liaison.fields import DateTimeField
from liaison.exceptions import ValidationError


def test_field():
    field = DateTimeField(date_format="%d-%m-%Y")
    value = field.validate("date", "09-10-2021")
    expected = datetime.datetime.strptime("09-10-2021", "%d-%m-%Y")
    assert value == expected


def test_field_raises_validation_error():
    field = DateTimeField(date_format="%d-%m-%Y")
    with pytest.raises(ValidationError):
        value = field.validate("date", "2021-10-09")


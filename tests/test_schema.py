import pytest

from liaison.schema import Schema
from liaison.fields import StringField, IntField
from liaison.decorators import strict_types
from liaison.exceptions import ValidationError


def test_schema_get_fields():
    class TestSchema(Schema):
        name = StringField()
        age = IntField()

    fields = TestSchema._get_fields()
    field_list = [i[1] for i in fields]

    assert TestSchema.name in field_list
    assert TestSchema.age in field_list


def test_schema_parse_method():
    class TestSchema(Schema):
        name = StringField()
        age = IntField()

    ns = TestSchema.parse({"name": "foo", "age": 30})

    assert ns.name == "foo"
    assert ns.age == 30


def test_schema_with_strict_decorator():

    data = {"name": "foo", "age": "30"}

    class TestSchema(Schema):
        name = StringField()
        age = IntField()

    ns = TestSchema.parse(data)
    assert ns.name == "foo"
    assert ns.age == 30

    @strict_types
    class TestSchemaStrict(Schema):
        name = StringField()
        age = IntField()

    with pytest.raises(ValidationError):
        TestSchemaStrict.parse(data)

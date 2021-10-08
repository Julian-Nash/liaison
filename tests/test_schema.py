from liaison.schema import Schema
from liaison.fields import StringField, IntField


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

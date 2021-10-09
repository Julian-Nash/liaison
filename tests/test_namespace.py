from liaison.schema import Namespace


def test_namespace_attrs():
    ns = Namespace(**{"foo": "bar", "age": 22})
    assert ns.foo == "bar"
    assert ns.age == 22


def test_namespace_get_method():
    ns = Namespace(**{"foo": "bar", "age": 22})
    assert ns.get("foo") == "bar"
    assert ns.get("age") == 22
    assert ns.get("nope", "default") == "default"


def test_namespace_dict_method():
    ns = Namespace(**{"foo": "bar", "age": 22})
    assert ns.to_dict() == {"foo": "bar", "age": 22}
    assert ns.to_dict(exclude=["foo"]) == {"age": 22}

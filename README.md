# Liaison

A zero dependency Python library for defining schemas, parsing and validating payloads.

[![CI](https://github.com/Julian-Nash/liaison/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/Julian-Nash/liaison/actions/workflows/main.yml)

Liaison doesn't aim to be too clever. It doesn't use descriptors, fancy metaprogramming or type hints for defining 
your schema. Simply inherit from the `Schema` base class, define your fields and call `parse`. In return, you'll 
receive a simple `Namespace` object containing your parsed data.

Goals:

- Simplicity
- Extensibility
- Speed
- 100% test coverage

Installation:

```shell
pip install liaison
```

Example:

```py3
from liaison import Schema, ValidationError
from liaison.fields import StringField, IntField, BoolField, ListField, DateTimeField


class UserSchema(Schema):

    name = StringField(required=True)
    email = StringField(required=True)
    age = IntField(min_val=18)
    date_of_birth = DateTimeField(date_format="%d-%m-%Y")
    subscribed = BoolField(default=False)
    tags = ListField(min_len=1)


data = {
    "name": "Bar",
    "email": "foo@bar.com",
    "age": 21,
    "tags": ["Python"]
}

result = UserSchema.parse(data)

print(result.name, result.email, result.age, result.tags)  # Bar foo@bar.com 21 ['Python']
```

Handling validation errors:

```py3
data = {
    "name": "Bar",
    "email": "foo@bar.com",
    "age": 16
}

try:
    result = UserSchema.parse(data)
except ValidationError as e:
    print(e)  # Value for 'age' must be at least 18
```

Defining custom field validators via the `<field>.validator` decorator:

```py3
class UserSchema(Schema):

    name = StringField(required=True)
    email = StringField(required=True)
    age = IntField(min_val=18)

    @name.validator
    def validate_name(self, key, value):
        # Define a custom validator, overrides the default validation method
        if value == "Foo":
            raise ValidationError(f"'{value}' is not a valid value for '{key}'")
        return value
```

Custom validators can also be passed as a parameter to the field:

```py3
def name_validator(schema_cls, key, value):
    if value in ("Foo", "Bar", "Baz"):
        raise ValidationError(f"'{value}' is not a valid value for '{key}'")
    return value


class UserSchema(Schema):

    name = StringField(required=True, validator=name_validator)
    email = StringField(required=True)
    age = IntField(min_val=18)
```

## Fields

Use fields to define your schema. By default, all fields accept the following common parameters:

| Parameter | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| `required` | `bool` | If the value is required | `False` |
| `default` | `Any` | A default value  | `None` |
| `choices` | `List[Any]` | A list of choices  | `None` |
| `validator` | `Callable` | A function to override the default validation method  | `None` |
| `strict_type` | `bool` | If `True`, only accept the fields data type  | `False` |

### `StringField` - Defining strings

| Parameter | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| `min_len` | `int` | The minimum length | `None` |
| `max_len` | `int` | The maximum length | `None` |

### `IntField` - Defining integers

| Parameter | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| `min_val` | `int` | The minimum value | `None` |
| `max_val` | `int` | The maximum value | `None` |

### `FloatField` - Defining floats

| Parameter | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| `min_val` | `int` | The minimum value | `None` |
| `max_val` | `int` | The maximum value | `None` |

### `BoolField` - Defining booleans

### `ListField` - Defining lists

| Parameter | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| `min_len` | `int` | The minimum length | `None` |
| `max_len` | `int` | The maximum length | `None` |

### `SetField` - Defining sets

> Note - `SetField` shares the same behaviour as `ListField`, returning a `set`.

| Parameter | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| `min_len` | `int` | The minimum length | `None` |
| `max_len` | `int` | The maximum length | `None` |

### `DictField` - Defining dictionaries

| Parameter | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| `min_len` | `int` | The minimum length | `None` |
| `max_len` | `int` | The maximum length | `None` |

### `DateTimeField` - Defining datetimes

> Note - `DateTimeField` fields will return `datetime` objects

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `date_format` | `str` | The date format |

### `UUIDField` - Defining UUIDs

> Note - `UUIDField` fields will NOT return a `UUID` obejct, it will return a string.

## Namespace

Calling the `parse` method on a `Schema` object will return a `Namespace` object, holding the parsed values as 
attributes.

```py3
from liaison import Schema
from liaison.fields import StringField, IntField, BoolField, FloatField, UUIDField


class RESTBaseSchema(Schema):

    offset = IntField(min_val=0, default=0)
    limit = IntField(max_val=100)
    search = StringField()


class ProductsRESTSchema(RESTBaseSchema):

    product_id = UUIDField()
    category = StringField()
    price = FloatField()
    in_stock = BoolField()


payload = {
    "offset": 10,
    "category": "shoes",
    "in_stock": True
}

result = ProductsRESTSchema.parse(payload)  

print(result.offset, result.limit, result.search, result.category, result.in_stock)
# 10 None None shoes True
```

`Namespace` objects have a `to_dict` method, returning a dictionary of the `Namespace` attributes and values:

```py3
print(result.to_dict())
# {'category': 'shoes', 'in_stock': True, 'limit': None, 'offset': 10, 'price': None, 'product_id': None, 'search': None}
```

An optional `exclude` parameter can be included to exclude certain attributes:

```py3
print(result.to_dict(exclude=("offset", "limit", "search")))
# {'category': 'shoes', 'in_stock': True, 'price': None, 'product_id': None}
```

## Defining custom fields

Create your own fields and validation logic by inheriting from any of the field classes and implementing a 
`validate` method.

> Note - The `validate` method must accept 2 params (key, value)

```py3
from liaison import Schema, ValidationError
from liaison.fields import StringField


class PasswordField(StringField):

    def validate(self, key, value):
        value = super().validate(key, value)
        if len(value) < 9:
            raise ValidationError("Value for 'password' must be at least 9 characters in length")
        # etc...
        return value


class UserSchema(Schema):

    username = StringField(required=True)
    password = PasswordField()


payload = {
    "username": "FooBar",
    "password": "password"
}

try:
    result = UserSchema.parse(payload)
except ValidationError as e:
    print(e)  # Value for 'password' must be at least 9 characters in length
    
payload = {
    "username": "FooBar",
    "password": "password12345!"
}

result = UserSchema.parse(payload)
print(result.password)  # password12345!
```
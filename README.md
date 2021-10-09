Liaison is a (Work in Progress) Python library designed for parsing and validating payloads.

Liaison doesn't aim to be too clever. It doesn't use descriptors, fancy metaprogramming or type hints for defining 
your schema. Simply inherit from the `Schema` base class, define your fields and call `parse`. In return, you'll 
receive a simple `Namespace` object containing the parsed data.

Goals:

- Simplicity
- Extensibility
- Speed
- 100% test coverage

Example:

```py3
from liaison import Schema, StringField, IntField, ValidationError


class UserSchema(Schema):

    name = StringField(required=True)
    email = StringField(required=True)
    age = IntField(min_val=18)


data = {
    "name": "Bar",
    "email": "foo@bar.com",
    "age": 21
}

result = UserSchema.parse(data)

print(result.name, result.email, result.age)  # Bar foo@bar.com 21
```

Catching validation errors:

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

Defining custom validators via the fields `validator` decorator:

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

TODO:

- [x] StringField
  - [] DateTimeField
- [x] NumberField
  - [x] IntField
  - [x] FloatField
- [] BoolField
- [] ListField
  - [] SetField
  - [] Add value type choices & check
- [] DictField
  - [] Add key type choices & check
  - [] Add value type choices & check
- [] Add regex to StringField


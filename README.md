Liaison is a (Work in Progress) Python library designed for parsing and validating payloads.

Liaison doesn't aim to be too clever. It doesn't use descriptors, fancy metaprogramming or type hints for defining 
your schema. Simply inherit from the `Schema` base class, define your fields and call `parse`. In return, you'll 
receive a simple `Namespace` object containing the parsed data.

Goals:

- Simplicity
- Extensibility
- Speed
- 100% test coverage

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


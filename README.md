Liaison is a Python library for parsing and validating dictionary payloads 

(Work in Progress)

Liaison doesn't aim to be too clever. It doesn't use type hints, descriptors or any fancy metaprogramming. Simply 
inherit from the `Schema` base class, define your fields and parse your data. In return, you'll receive a simple 
`Namespace` object containing the parsed data.

Goals:

- Simplicity
- Extensibility
- Speed
- 100% test coverage

TODO:

- [x] NumberField
  - [x] IntField
  - [x] FloatField
- [] BoolField
- [] ListField
- [] DictField


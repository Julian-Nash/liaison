from .schema import Schema


def strict_types(cls: Schema):
    """strict_types decorator. Decorate a Schema instance to enforce `strict_type` on all Fields"""
    fields = cls._get_fields()
    for name, field in fields:
        field.strict_type = True
    return cls

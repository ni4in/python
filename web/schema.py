from marshmallow import Schema, fields

# we use json for two end points
# 1. post and put. That is create and update


class ItemSchema(Schema):
    """class for post request schema

    Args:
        Schema (class): parent class
    """

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    """class for put request schema

    Args:
        Schema (class): parent class
    """

    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    """class for post request schema

    Args:
        Schema (_type_): _description_
    """

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

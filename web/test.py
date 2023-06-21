from marshmallow import Schema, fields

class ImageSchema(Schema):
    img = fields.Str(load_only=True)
    label = fields.Bool(dumps_only=True)


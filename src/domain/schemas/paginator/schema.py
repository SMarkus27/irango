from marshmallow import Schema, fields


class PaginatorSchema(Schema):
    name = fields.Str()
    size = fields.Int(default=1)
    page = fields.Int()
    sort = fields.Str()

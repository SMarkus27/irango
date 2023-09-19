from marshmallow import Schema, fields


class SpecialProductSchema(Schema):
    active = fields.Boolean(required=True)
    special_price = fields.Float(required=False)
    description = fields.Str(required=False)
    business_day = fields.Str(required=False)
    weekend = fields.Str(required=False)


class ProductSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    category = fields.Str()
    promotion = fields.Nested(SpecialProductSchema)

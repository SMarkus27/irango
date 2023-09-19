from marshmallow import Schema, fields


class AddressSchema(Schema):
    street_name = fields.Str()
    street_number = fields.Str()


class BusinessHoursSchema(Schema):
    business_day = fields.Str()
    weekend = fields.Str()


class RestaurantSchema(Schema):
    name = fields.Str()
    address = fields.Nested(AddressSchema)
    business_hours = fields.Nested(BusinessHoursSchema)

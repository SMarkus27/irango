from marshmallow import Schema, fields


class UsersSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()



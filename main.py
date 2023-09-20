from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from src.repositories.cache.repository import CacheRepository
from src.routes.restaurants.route import restaurant
from src.routes.products.route import products
from src.routes.users.route import users
from src.services.users.service import UsersService

authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

app = Flask(__name__)
app.config["API_TITLE"] = "IRANGO"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["JWT_SECRET_KEY"] = "xaps"

jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def token_in_blocklist_loader(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    in_blocklist = UsersService.blocklist(jti)
    return in_blocklist


@jwt.revoked_token_loader
def revoked_token_loader(jwt_header, jwt_payload):
    return {
        "message": "The token has been revoked",
        "status_code": 401
    }


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return {
        "message": "The token has expired",
        "status_code": 401
    }


@jwt.invalid_token_loader
def expired_token_callback(error):
    return {
        "message": "Signature verification failed",
        "status_code": 401
    }


@jwt.unauthorized_loader
def expired_token_callback(error):
    return {
        "message": "Request does not contain an access token",
        "status_code": 401
    }


api = Api(app)

api.register_blueprint(restaurant)
api.register_blueprint(products)
api.register_blueprint(users)

if __name__ == "__main__":
    app.run()

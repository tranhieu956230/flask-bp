from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace("User", description="user related operations")
    user = api.model("user", {
        "email": fields.String(required=True, description="user email address"),
        "username": fields.String(required=True, description="user username"),
        "password": fields.String(required=True, description="user password"),
        "public_id": fields.String(description="user identifier")
    })


class AuthDto:
    api = Namespace("Auth", description="auth related operations")
    auth = api.model("auth", {
        "email": fields.String(required=True, description="email address"),
        "password": fields.String(required=True, description="user password")
    })

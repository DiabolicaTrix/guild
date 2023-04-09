import os
import jwt
from werkzeug.wrappers import Request, Response, ResponseStream


class Authenticator(object):
    def __init__(self, app) -> None:
        self.app = app

    def __call__(self, env, start_response):
        request = Request(env)

        # Allow if the path is /login or /register or if the request method is OPTIONS (CORS preflight)
        if request.path in ['/login', '/register'] or request.method == 'OPTIONS':
            return self.app(env, start_response)

        token = request.headers.get('Authorization')

        # Deny if token is empty
        if token is None:
            return Response("Unauthorized", 401)(env, start_response)

        # Split token from the Bearer prefix
        token = token.split(' ')

        # Deny if token is not of Bearer type
        if token[0] != 'Bearer':
            return Response("Unauthorized", 401)(env, start_response)

        # Deny if token is invalid
        try:
            jwt.decode(token[1], os.getenv(
                "JWT_PRIVATE_KEY"), algorithms=['HS256'])
            env['token'] = token[1]
            return self.app(env, start_response)
        except jwt.exceptions.InvalidSignatureError:
            return Response("Unauthorized", 401)(env, start_response)

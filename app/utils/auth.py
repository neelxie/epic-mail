from functools import wraps
import jwt
from flask import request, jsonify
from .validation import Valid

token_validation = Valid()

my_secret_key = "#$^"

def token_required(my_function):
    @wraps(my_function)
    def decorate(*args, **kwargs):

        if not request.headers.get('Authorization'):
            return jsonify({
                'error': "Unauthorized! Token is missing.",
                'status': 401
            }), 401

        headers = request.headers.get('Authorization')
        token = token_validation.strip_token(headers)

        try:
            data = jwt.decode(token, my_secret_key)
            print(data)

        except (
            jwt.InvalidTokenError,
            jwt.InvalidSignatureError,
            jwt.ExpiredSignatureError):
            return jsonify({
            'error': "Unauthorized! Invalid Token!",
            "status": 401
        }), 401
        return my_function(*args, **kwargs)
    return decorate
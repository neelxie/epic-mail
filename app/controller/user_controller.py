""" File to hold the user class controller."""
from flask import jsonify
from flask import request
import datetime
import jwt
from ..utils.validation import Valid
from ..utils.auth import my_secret_key

from ..models.user_model import (
    Base, User, UserDB)

class User_Controller:
    """ Class that implements all app logic for users."""

    user_db = UserDB()
    validator = Valid()

    def __init__(self):
        pass

    def index(self):
        """ function for the index route."""

        data = [{'message': 'Welcome to Epic Mail.'}]
        return jsonify({
            'data': data,
            'status': 200
        }), 200

    def register_user(self):
        """ Controller logic for signup method.
        """
        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        phone_number = data.get("phone_number")
        user_name = data.get("user_name")
        password = data.get("password")
        is_admin = data.get("is_admin")
        user_id = len(self.user_db.all_users) + 1

        user_attributes = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password",
            "is_admin"]

        user_attribute_error = self.validator.validate_attributes(
            data,
            user_attributes)

        if user_attribute_error is not None:
            return jsonify({
                "error": "You have not entered this/these user attributes.",
                "missing attributes": user_attribute_error,
                "status": 400,
            }), 400

        # check if user data is valid if not return an error.
        error = self.validator.check_for_invalid_function(
            self.validator.check_base(
                first_name,
                last_name,
                phone_number), self.validator.check_other(
            email,
            password,
            is_admin))

        if error:
            return jsonify({
                'error': error,
                "status": 400
            }), 400

        # if the email is already registered return error.
        email_exist = self.user_db.verify_email(email)

        if email_exist is not None: 
            return jsonify({
                "status": 401,
                "error": "Email already in registered."
            }), 401

        user = User(
            Base(
                first_name,
                last_name,
                phone_number,
                password),
            email,
            is_admin,
            user_id)

        self.user_db.add_user(user)

        token = jwt.encode({"user_id": user_id,
                            "is_admin": is_admin,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)},
                           my_secret_key).decode('UTF-8')

        payload = jwt.decode(token, my_secret_key)

        return jsonify({
            "status": 201,
            'data': [{
                'token': token
            }]
        }), 201

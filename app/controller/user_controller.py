""" File to hold the user class controller."""
from flask import jsonify
from flask import request
import datetime
import jwt
from ..utils.validation import Valid
from ..utils.auth import app_secret_key
from ..models.db import DatabaseConnection

db = DatabaseConnection()
db.create_db_tables()

class UserController:
    """ Class that implements all app logic for users."""

    validator = Valid()

    def register_user(self):
        """ Controller logic for signup method.
        """
        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        phone_number = data.get("phone_number")
        password = data.get("password")

        user_attributes = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password"]

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
                password))

        if error:
            return jsonify({
                'error': error,
                "status": 400
            }), 400

        # if the email is already registered return error.
        email_exist = db.check_email(email)

        if email_exist is not None: 
            return jsonify({
                "status": 401,
                "error": "Email already in registered."
            }), 401

        user = db.add_user(
            first_name,
            last_name,
            phone_number,
            email,
            password)


        user_id = user.get('user_id')

        token = jwt.encode({"user_id": user_id,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           app_secret_key).decode('UTF-8')
        return jsonify({
            "status": 201,
            'message': 'User successfully signed in.',
            'token': token
        }), 201


    def log_in(self):
        """ Class method to log in user
        """
        login = request.get_json()

        email = login.get("email")
        password = login.get("password")

        bad_data = self.validator.validate_login(email, password)

        if bad_data:
            return jsonify({
                'error': bad_data,
                "status": 400
            }), 400

        user = db.login(password, email)
        print(user)

        if user is None:
            return jsonify({
                'error': "The log in credentials you entered are wrong.",
                "status": 403
            }), 403

        user = db.check_email(email)
        
        user_id = user.get('user_id')

        token = jwt.encode(
            {"user_id": user_id,
             'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, app_secret_key).decode('UTF-8')
        return jsonify({
            'status': 200,
            'message':'user logged in',
            'token': token
        }), 200


    def app_users(self):
        """ fetch all users.
        """
        users = db.get_users()

        if len(users) > 0:
            return jsonify({
                "status": 200,
                "data": [user for user in users]
            }), 200
        # this case is logically impossible but catered for.
        return jsonify({
            "status": 404,
            "error": "No app users yet."
        }), 404


    def fetch_user(self, user_id):
        """ fetch a single user.
        """
        user = db.get_user(user_id)

        if user:
            return jsonify({
                "status": 200,
                "data": [user]
            }), 200
        return jsonify({
            "status": 404,
            "error": "No user by that ID."
        }), 404

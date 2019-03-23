from flask import Flask
import unittest
import simplejson as json
import datetime
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import jwt
from app.utils.auth import app_secret_key
from app.views.app_views import create_app

app = create_app()


class TestStructure(unittest.TestCase):

    def setUp(self):
        """ The set up for my app tests."""
        self.app = app.test_client()
        self.registered = "2019-03-21 10:10:02.086352"
        self.test_message = dict(
            email_id = 1,
            created_on = self.registered,
            subject = "We ate mangoes.",
            message = "We should eat only young mangoes for lunch",
            sender_id = 1,
            receiver_id = 2,
            parent_message_id = 0,
            status = "unread",
            sender_status = "sent"
        )
        self.test_other_message = dict(
            email_id = 2,
            created_on = self.registered,
            subject = "We ate mangoes.",
            message = "We should eat only young mangoes for lunch",
            sender_id = 1,
            receiver_id = 2,
            parent_message_id = 0,
            status = "unread",
            sender_status = "sent"
        )
        self.other_message = dict(
            email_id = 3,
            created_on = self.registered,
            subject = "We ate mangoes.",
            message = "We should eat only young mangoes for lunch",
            sender_id = 2,
            receiver_id = 1,
            parent_message_id = 0,
            status = "unread",
            sender_status = "sent"
        )
        self.test_error_message = dict(
            email_id = "matama@gmal.com",
            created_on = self.registered,
            subject = "We ate mangoes.",
            message = "We should eat only young mangoes for lunch",
            sender_id = 1,
            receiver_id = 2,
            parent_message_id = 0,
            status = "unread",
            sender_status = "sent"
        )
        self.test_user = dict(
            first_name = "Greatest",
            last_name = "Coder",
            phone_number ="0705828612",
            password = "asdfghj",
            email = "dede@cia.gov",
            is_admin = False,
            user_id = 1,
        )
        self.test_app_user = dict(
            first_name = "Greatest",
            last_name = "Coder",
            phone_number ="0705828612",
            password = "asdfghj",
            email = "today@cia.gov",
            is_admin = False,
            user_id = 3,
        )
        self.test_user_email = dict(
            first_name = "Greatest",
            last_name = "Coder",
            phone_number ="0705828612",
            password = "asdfghj",
            email = "haxor@cia.gov",
            is_admin = False,
            user_id = 2,
        )
        self.test_user_no_msgs = dict(
            first_name = "Greatest",
            last_name = "Coder",
            phone_number ="0705828612",
            password = "asdfghj",
            email = "tewaly@cia.gov",
            is_admin = False,
            user_id = 5,
        )
        self.test_user_error = dict(
            first_name = 2,
            last_name = "Coder",
            phone_number ="0705828612",
            password = "asdfghj",
            email = "haxor@cia.gov",
            is_admin = False,
            user_id = 4,
        )

        self.token = jwt.encode({"user_id": self.test_user['user_id']}, app_secret_key).decode('UTF-8')
        self.headers = {'Authorization': f'Bearer {self.token}'}

        self.second_token = jwt.encode({"user_id": self.test_user_email['user_id']}, app_secret_key).decode('UTF-8')
        self.second_headers = {'Authorization': f'Bearer {self.second_token}'}

        self.forth_token = jwt.encode({"user_id": self.test_user_email['user_id']}, app_secret_key).decode('UTF-8')
        self.forth_headers = {'Authorization': f'Bearer {self.forth_token}'}

    def sign_up(self):
        create_user = self.app.post(
            "/api/v1/auth/signup", content_type='application/json', data=json.dumps(self.test_user))
        return create_user

    def user_login(self):
        signed_in = self.sign_up()
        logged_user = self.app.post('/api/v1/auth/login', content_type='application/json', 
            data=json.dumps({"email":"dede@cia.gov@gfhf.com", "password":"asdfghj"}))
        return logged_user


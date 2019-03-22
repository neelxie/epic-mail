""" email controller file. """
from flask import request, jsonify
from ..utils.validation import Valid
from ..models.email_model import (
    Email, EmailDB, Data, Identity)


class EmailController:
    """
    controller class for email.
    """
    my_email_db = EmailDB()
    valid = Valid()


    def index(self):
        """ function for the index route."""

        data = [{'message': 'Welcome to Epic Mail.'}]
        return jsonify({
            'data': data,
            'status': 200
        }), 200

    def compose_email(self):
        """
        Class method to compose email
        """
        email_data = request.get_json()

        email_id = len(self.my_email_db.email_server) + 1
        subject = email_data.get("subject")
        message = email_data.get("message")
        sender_id = email_data.get("sender_id")
        receiver_id = email_data.get("receiver_id")

        # only replies have this taking 0 as default value
        parent_message_id = 0 
        status = "unread" # to the recepient
        sender_status = "sent" # to the sender

        email_list = ['subject', 'message', "sender_id", 'receiver_id']

        email_error = self.valid.validate_attributes(email_data, email_list)

        if email_error:
            return jsonify({
                "missing": "This/These attributes are missing.",
                "status": 400,
                "error": email_error
            }), 400

        compose_error = self.valid.validate_composed_msg(subject, message, sender_id, receiver_id)

        if compose_error:
            return jsonify({
                "status": 400,
                "error": compose_error
            }), 400

        new_email = Email(
            Data(
                Identity(
                    sender_id,
                    receiver_id,
                    parent_message_id),
                subject,
                message,
                sender_status),
            status,
            email_id)

        self.my_email_db.add_email(new_email)

        return jsonify({
            "status": 201,
            'data': [new_email.to_json()]
        }), 201

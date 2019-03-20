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
                message),
            status,
            sender_status,
            email_id)

        self.my_email_db.add_email(new_email)

        return jsonify({
            "status": 201,
            'data': [new_email.to_json()]
        }), 201

    def received(self):
        """
        show all received mails.
        """
        new_mail_lst = self.my_email_db.get_received()

        if new_mail_lst:
            return jsonify({
                "status": 200,
                "data": [mail.to_json() for mail in new_mail_lst]
            }), 200

        return jsonify({
            "status": 400,
            "error": "No messages in the inbox."
        }), 400


    def unread(self):
        """
        show all unread mails.
        """
        all_unread = self.my_email_db.get_unread()

        if all_unread:
            return jsonify({
                "status": 200,
                "data": [one_msg.to_json() for one_msg in all_unread]
            }), 200

        return jsonify({
            "error": "No unread messages.",
            "status": 400,
        }), 400


    def sent_emails(self):
        """
        show all user sent mails.
        """
        user_sent = self.my_email_db.get_sent()

        if user_sent:
            return jsonify({
                "status": 200,
                "data": [my_sent.to_json() for my_sent in user_sent]
            }), 200

        return jsonify({
            "status": 400,
            "error": "You have no sent messages."
        }), 400


    def specific_email(self, email_id):
        """
        Read an email.
        """
        one_email = self.my_email_db.read_message(email_id)

        if one_email:
            return jsonify({
                "data": [one_email.to_json()],
                "status": 200
            }), 200
        return jsonify({
            "error": "No email by that ID.",
            "status": 400
        }), 400

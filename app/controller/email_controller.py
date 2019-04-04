""" email controller file. """
from flask import request, jsonify
from ..utils.validation import Valid
from ..utils.auth import user_identity
from ..models.db import DatabaseConnection

db = DatabaseConnection()
db.create_db_tables()

class EmailController:
    """
    controller class for email.
    """
    valid = Valid()

    def index(self):
        """ function for the index route."""
        return jsonify({
            'message': 'Welcome to Epic Mail.',
            'status': 200
        }), 200

    def compose_email(self, email_status):
        """
        Class method to compose email
        """
        email_data = request.get_json()

        subject = email_data.get("subject")
        message = email_data.get("message")
        receiver_email = email_data.get("receiver_email")
        payload = user_identity()
        sender_id = payload.get('email')

        # only replies have this taking 0 as default value
        parent_message_id = 0

        if email_status == 'send':
            status = "unread" # to the recepient
            sender_status = "sent" # to the sender

        elif email_status == 'save':
            status = "draft"
            sender_status = 'saved'

        elif isinstance(email_status, int):
            msg = db.get_a_message(email_status)
            if msg is None:
                return jsonify({
                    "status":404,
                    "error": "You can not reply to a non existant email."
                }), 404
            parent_message_id = email_status
            status = "unread"
            sender_status = "sent"

        else:
            return jsonify({
                "status": 400,
                "error": "You entered wrong reply email ID."
            }), 400

        email_list = ['subject', 'message', 'receiver_email']

        email_error = self.valid.validate_attributes(email_data, email_list)

        if email_error:
            return jsonify({
                "missing": "This/These attributes are missing.",
                "status": 400,
                "error": email_error
            }), 400

        compose_error = self.valid.validate_composed_msg(
            subject, message, receiver_email)

        if compose_error:
            return jsonify({
                "status": 400,
                "error": compose_error
            }), 400

        valid_email = db.check_email(receiver_email) 

        if valid_email is None:
            return jsonify(
                {
                    "status": 400,
                    "error": "No user by that email"
                }
            ), 400


        new_email = db.add_message(
            subject,
            message,
            sender_id,
            receiver_email,
            parent_message_id,
            status,
            sender_status)

        return jsonify({
            "status": 201,
            'data': [new_email]
        }), 201

    def received(self):
        """
        function fetching received mails.
        """
        get_user = user_identity()
        receiver_email = get_user.get('email')
        new_mail_lst = db.get_received(receiver_email)

        if new_mail_lst:
            return jsonify({
                "status": 200,
                "data": [mail for mail in new_mail_lst]
            }), 200

        return jsonify({
            "status": 400,
            "error": "No messages in the inbox."
        }), 400


    def unread(self):
        """
        show one user's all unread mails. """
        logged_user = user_identity()
        got_the_user = logged_user.get('user_id')
        all_unread = db.get_unread(got_the_user)

        if all_unread:
            return jsonify({
                "status": 200,
                "data": [one_msg for one_msg in all_unread]
            }), 200

        return jsonify({
            "error": "No unread messages.",
            "status": 400,
        }), 400


    def sent_emails(self):
        """
        show all user sent mails.
        """
        from_token = user_identity()
        sender_email = from_token.get('email')
        user_sent = db.fetch_sent(sender_email)

        if user_sent:
            return jsonify({
                "status": 200,
                "data": [my_sent for my_sent in user_sent]
            }), 200

        return jsonify({
            "status": 400,
            "error": "You have no sent messages."
        }), 400


    def specific_email(self, email_id):
        """
        Read an email.
        """
        one_email = db.get_a_message(email_id)

        if one_email:
            return jsonify({
                "data": [one_email],
                "status": 200
            }), 200
        return jsonify({
            "error": "No email by that ID.",
            "status": 400
        }), 400

    def delete_email(self, email_id):
        """ 
        delete an email.
        """
        found = db.get_a_message(email_id)

        if found:
            db.delete_message(email_id)
            return jsonify({
                "status": 200,
                "data": [{
                    "message": "Successfully deleted."
                }]
            }), 200
        return jsonify({
            "error": "No email by that ID.",
            "status": 400
        }), 400


""" Models' file for email_server and email messages."""
from datetime import datetime

class Identity:
    """ Base class for the message class that contains meta data.
    """
    def __init__(self, receiver_id, parent_message_id):
        """ Contsructor for the Identity class.
        """
        self.receiver_id = receiver_id
        self.parent_message_id = parent_message_id


class Data:
    """ This is the underlying class for the email class.
    """
    def __init__(self, identity, subject, message, sender_id):
        """ Data class constructor.
        """
        self.identity = identity
        self.subject = subject
        self.message = message
        self.sender_id = sender_id
        

class Email:
    """
    class for email message.
    """
    def __init__(self, data, status, sender_status, email_id):
        self.data = data
        self.status = status
        self.sender_status = sender_status
        self.email_id = email_id
        self.registered = str(datetime.now())

    def to_json(self):
        return {
            "email_id": self.email_id,
            "created_on": self.registered,
            "subject": self.data.subject,
            "message": self.data.message,
            "sender_id": self.data.sender_id,
            "receiver_id": self.data.identity.receiver_id,
            "parent_message_id": self.data.identity.parent_message_id,
            "status": self.status,
            "sender_status": self.sender_status
        }

class EmailDB:
    """
    class for storing emails.
    """
    def __init__(self):
        self.email_server = []

    def add_email(self, email):
        """
        add email to email_server.
        """
        self.email_server.append(email)

    def get_email(self, user_id, status):
        """
        get emails.
        """
        required_emails = []

        for one_email_record in self.email_server:

            if one_email_record.data.identity.receiver_id == user_id and status == 'received':
                if one_email_record.status == 'unread' or one_email_record.status == 'read':
                    required_emails.append(one_email_record)

            elif one_email_record.data.identity.receiver_id == user_id and status == 'unread':
                if one_email_record.status == 'unread':
                    required_emails.append(one_email_record)

            elif one_email_record.data.sender_id == user_id and status == 'sent':
                if one_email_record.sender_status == 'sent':
                    required_emails.append(one_email_record)

            else:
                pass

        return required_emails

    def read_message(self, message_id):
        """
        Read an email.
        """
        for from_me in self.email_server:
            if from_me.email_id == message_id:
                return from_me
        return None

    def remove_email(self, email_id):
        """ delete email from email server.
        """
        del self.email_server[email_id - 1]


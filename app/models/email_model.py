""" Models' file for email_server and email messages."""
from datetime import datetime

class Identity:
    """ Base class for the message class that contains meta data.
    """
    def __init__(self, sender_id, receiver_id, parent_message_id):
        """ Contsructor for the Identity class.
        """
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.parent_message_id = parent_message_id


class Data:
    """ This is the underlying class for the email class.
    """
    def __init__(self, identity, subject, message):
        """ Data class constructor.
        """
        self.identity = identity
        self.subject = subject
        self.message = message
        

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
            "sender_id": self.data.identity.sender_id,
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

    def get_all_emails(self):
        """
        fetch all emails in email_server
        """
        return self.email_server

    def add_email(self, email):
        """
        add email to email_server.
        """
        self.email_server.append(email)

    def get_received(self):
        """
        view received emails.
        """
        my_lst = []
        for stuff in self.email_server:
            if stuff.status == 'unread' or stuff.status == 'read':
                my_lst.append(stuff)
        # am assuming admin running this endpoint
        return my_lst

    def get_unread(self):
        """
        view received emails.
        """
        unread = []
        for not_yet in self.email_server:
            if not_yet.status == 'unread': #more functionality to be added
                unread.append(not_yet)
        return unread

    def get_sent(self):
        """
        Get sent emails.
        """
        my_sent = []
        for from_me in self.email_server:
            if from_me.sender_status == 'sent':
                my_sent.append(from_me)
        return my_sent

    def read_message(self, message_id):
        """
        Read an email.
        """
        my_sent = []
        for from_me in self.email_server:
            if from_me.email_id == message_id:
                my_sent.append(from_me)
        return my_sent[0]

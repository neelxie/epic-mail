""" Models' file for email_server and email messages."""
from datetime import datetime

class Email:
    """
    model for app email message.
    """
    def __init__(self, status, sender_status, email_id, receiver_id, parent_message_id, subject, message, sender_id):
        self.status = status
        self.sender_status = sender_status
        self.email_id = email_id
        self.registered = str(datetime.now())
        self.receiver_id = receiver_id
        self.parent_message_id = parent_message_id
        self.subject = subject
        self.message = message
        self.sender_id = sender_id

    

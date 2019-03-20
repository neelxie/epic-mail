""" emails view file."""
from flask import Blueprint
from ..controller.email_controller import EmailController

email_controller = EmailController()

email_bp = Blueprint("email_bp", __name__)

@email_bp.route('/')
def home():
    """ This is the index route.
    """
    return email_controller.index()

@email_bp.route('/messages', methods=['POST'])
def send_email():
    """ 
    compose an app email
    """
    return email_controller.compose_email()

@email_bp.route('/messages', methods=['GET'])
def inbox():
    """ 
    all received email
    """
    return email_controller.received()

@email_bp.route('/messages/unread', methods=['GET'])
def unread_messages():
    """ 
    all unread email
    """
    return email_controller.unread()

@email_bp.route('/messages/sent', methods=['GET'])
def sent_messages():
    """ 
    all sent messages
    """
    return email_controller.sent_emails()
    
@email_bp.route('/messages/<int:message_id>', methods=['GET'])
def read_one():
    """ 
    one email
    """
    return email_controller.specific_email(message_id)
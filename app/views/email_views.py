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
    
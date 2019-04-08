""" emails view file."""
from flask import Blueprint
from ..controller.email_controller import EmailController
from ..utils.auth import token_required

email_controller = EmailController()

email_bp = Blueprint("email_bp", __name__)


@email_bp.route('/messages', methods=['POST'])
@token_required
def send_email():
    """ 
    compose and send app email
    """
    return email_controller.compose_email("send")

@email_bp.route('/messages/save', methods=['POST'])
@token_required
def save_email():
    """ 
    compose and save app email
    """
    return email_controller.compose_email("save")

@email_bp.route('/messages/reply/<int:message_id>', methods=['POST'])
@token_required
def reply_email(message_id):
    """ 
    compose and reply to app email
    """
    return email_controller.compose_email(message_id)

@email_bp.route('/messages', methods=['GET'])
@token_required
def inbox():
    """ 
    all received email
    """
    return email_controller.received()

@email_bp.route('/messages/unread', methods=['GET'])
@token_required
def unread_messages():
    """ 
    all unread email
    """
    return email_controller.unread()

@email_bp.route('/messages/sent', methods=['GET'])
@token_required
def sent_messages():
    """ 
    all sent messages
    """
    return email_controller.sent_emails()
    
@email_bp.route('/messages/<int:message_id>', methods=['GET'])
@token_required
def read_one(message_id):
    """ 
    one email
    """
    return email_controller.specific_email(message_id)

@email_bp.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_one(message_id):
    """ 
    delete one email
    """
    return email_controller.delete_email(message_id)

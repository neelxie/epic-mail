""" users view file."""
from flask import Blueprint
from ..controller.user_controller import UserController

user_controller = UserController()

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route('/signup', methods=['POST'])
def sign_up():
    """ 
    register up as app user
    """
    return user_controller.register_user()

@auth_bp.route('/login', methods=['POST'])
def sign_in():
    """ 
    log in as app user
    """
    return user_controller.log_in()

@auth_bp.route('/users', methods=['GET'])
def all_app_users():
    """ 
    fetch all app users
    """
    return user_controller.app_users()

@auth_bp.route('/users/<int:user_id>', methods=['GET'])
def one_app_user(user_id):
    """ 
    fetch one app user
    """
    return user_controller.fetch_user(user_id)
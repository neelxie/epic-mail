""" users view file."""
from flask import Blueprint
from ..controller.user_controller import User_Controller

user_controller = User_Controller()

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/')
def home():
    """ This is the index route.
    """
    return user_controller.index()

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
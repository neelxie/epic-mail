""" Groups view file."""
from flask import Blueprint
from ..controller.group_controller import GroupController
from ..utils.auth import token_required

group_controller = GroupController()

group_bp = Blueprint("group_bp", __name__)

@group_bp.route('/groups', methods=['POST'])
@token_required
def make_group():
    """ 
    make new app group """
    return group_controller.add_group()

@group_bp.route('/groups', methods=['GET'])
@token_required
def all_group():
    """ 
    fetch all app groups """
    return group_controller.all_groups()

@group_bp.route('/groups/<int:group_id>', methods=['PATCH'])
@token_required
def change_group_name(group_id):
    """ 
    update an app group name """
    return group_controller.update_group_name(group_id)
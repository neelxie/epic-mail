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

@group_bp.route('/groups/<int:group_id>/name', methods=['PATCH'])
@token_required
def change_group_name(group_id):
    """ 
    update an app group name """
    return group_controller.update_group_name(group_id)

@group_bp.route('/groups/<int:group_id>', methods=['DELETE'])
@token_required
def delete_group(group_id):
    """ 
    delete a group """
    return group_controller.delete_group(group_id)

@group_bp.route('/groups/<int:group_id>', methods=['GET'])
@token_required
def get_group(group_id):
    """ 
    get a group """
    return group_controller.get_group(group_id)

@group_bp.route('/groups/<int:group_id>/users', methods=['POST'])
@token_required
def add_member_to_group(group_id):
    """ 
    Add a user as a member to a group. """
    return group_controller.adding_group_member(group_id)

@group_bp.route('/groups/<int:group_id>/users', methods=['GET'])
@token_required
def get_group_member(group_id):
    """ 
    Get a group members. """
    return group_controller.get_group_membas(group_id)

@group_bp.route('/groups/<int:group_id>/users/<int:user_id>', methods=['DELETE'])
@token_required
def remove_group_member(group_id, user_id):
    """ 
    Route to remove a user from app group. """
    return group_controller.remove_group_member(group_id, user_id)

@group_bp.route('/groups/<int:group_id>/messages', methods=['POST'])
@token_required
def add_group_message(group_id):
    """ 
    Add a message to app group. """
    return group_controller.add_group_message(group_id)

@group_bp.route('/groups/<int:group_id>/messages', methods=['GET'])
@token_required
def all_group_messages(group_id):
    """ 
    Fetch all messages from app group. """
    return group_controller.get_group_messsages(group_id)
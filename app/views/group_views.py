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
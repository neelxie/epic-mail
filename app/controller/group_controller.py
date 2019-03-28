""" Group controller file. """
from flask import request, jsonify
from ..utils.validation import Valid
from ..utils.auth import user_identity
from ..models.db import DatabaseConnection

db = DatabaseConnection()
db.create_db_tables()

class GroupController:
    """
    This is a controller class for group.
    """
    group_validation = Valid()
    def add_group(self):
        """ This method will create a new group."""
        data = request.get_json()

        name = data.get("group_name")

        error = self.group_validation.validate_string(name)

        if error:
            return jsonify({
                'error': "Group name is invalid.",
                "status": 400
            }), 400
        
        group = db.create_group(name, 'admin')

        return jsonify({
            "status": 201,
            "data": [group]
        }), 201
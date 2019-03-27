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

        from_token = user_identity()
        created_by = from_token.get('user_id')
        
        group = db.create_group(name, created_by, 'admin')

        return jsonify({
            "status": 201,
            "data": [group]
        }), 201

    def all_groups(self):
        """ Retrieve all groups. """

        get_user = user_identity()
        created_by = get_user.get('user_id')
        groups = db.all_app_groups(created_by)

        if groups:
            return jsonify({
                "data": [group for group in groups],
                "status": 200
            }), 200

        return jsonify({
            "status": 404,
            "error": "No user groups yet."
        }), 404

    def update_group_name(self, group_id):
        """
        Update group name.
        """
        group = db.return_group(group_id)

        if group is None:
            return jsonify({
                "error": "You can not update the name of a non existant group.",
                "status": 404
            }), 404
        new_group_name = request.get_json()

        name = new_group_name.get("group_name")

        wrong_name = self.group_validation.validate_string(name)

        if wrong_name is False:
            return jsonify({
                "error": "Invalid new group name.",
                "status": 400
            }), 400
        
        db.change_group_name(name, group_id)

        check_update = db.return_group(group_id)

        return jsonify({
            "status": 200,
            "data": [check_update]
        }), 200

    def delete_group(self, group_id):
        """
        delete a group you created. """
        
        created_by = user_identity()
        owner = created_by.get('user_id')

        group_exists = db.return_group(group_id)

        if group_exists is None:
            return jsonify({
                "error": "Can not delete a non existant group.",
                "status": 404
            }), 404

        db.delete_group(owner, group_id)

        return jsonify({
            "status": 200,
            "message": "Group successfully deleted."
        }), 200

    def adding_group_member(self, group_id, user_id):
        """
        Method does add a user in the system to a group. """

        find_group = db.return_group(group_id)

        if find_group is None:
            return jsonify({
                "status": 404,
                "error": "Group not found.",
            }), 404

        find_user = db.get_user(user_id)
        
        if find_user is None:
            return jsonify({
                "error": "User not found.",
                "status": 404
            }), 404

        added = db.add_user_to_group(group_id, user_id)

        return jsonify({
            "status": 201,
            "data": [added]
        }), 201


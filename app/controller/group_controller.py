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

        if error is False:
            return jsonify({
                'error': "Group name is invalid.",
                "status": 400
            }), 400

        from_token = user_identity()
        created_by = from_token.get('email')
        
        group = db.create_group(name, created_by, 'admin')

        return jsonify({
            "status": 201,
            "data": [group]
        }), 201

    def get_group_membas(self, group_id):
        groups = db.get_group_members(group_id)

        if groups:
            return jsonify({
                "data": [group for group in groups],
                "status": 200
            }), 200

        return jsonify({
            "status": 404,
            "error": "No group members yet."
        }), 404

    def all_groups(self):
        """ Retrieve all groups. """

        get_user = user_identity()
        created_by = get_user.get('email')
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

    def one_group(self, group_id):
        check_group = db.return_group(group_id)

        if check_group is None:
            return jsonify({
                "error": "Given group ID does not exist.",
                "status": 404
            }), 404
            
        return jsonify({
            "status": 200,
            "data": [check_group]
        }), 200

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
        owner = created_by.get('email')

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

    def adding_group_member(self, group_id):
        """
        Method does add a user in the system to a group. """
        new_group_name = request.get_json()

        receiver_email  = new_group_name.get("receiver_email")

        find_group = db.return_group(group_id)

        if find_group is None:
            return jsonify({
                "status": 404,
                "error": "Group not found.",
            }), 404

        find_user = db.check_email(receiver_email)
        
        if find_user is None:
            return jsonify({
                "error": "User not found.",
                "status": 404
            }), 404

        added = db.add_user_to_group(group_id, receiver_email)

        return jsonify({
            "status": 201,
            "data": [added]
        }), 201


    def remove_group_member(self, group_id, user_id):
        """
        function that gets rid of a member from a group. """

        deletee = db.get_user(user_id)
        
        if deletee is None:
            return jsonify({
                "error": "Can not delete non existant user.",
                "status": 404
            }), 404

        from_group = db.return_group(group_id)

        if from_group is None:
            return jsonify({
                "status": 404,
                "error": "No group by that ID.",
            }), 404

        receiver_email = deletee.get('email')
        db.delete_user_from_group(group_id, receiver_email)

        return jsonify({
            'message': "User successfully removed from group.",
            "status": 200
        }), 200


    def add_group_message(self, group_id):
        """ method that adds a group message. """
        verify_group = db.return_group(group_id)

        if verify_group is None:
            return jsonify({
                "status": 404,
                "error": "Given ID group does not exist.",
            }), 404

        payload = user_identity()
        current_user = payload.get('email')

        user = db.return_member(group_id, current_user)

        message_data = request.get_json()

        subject = message_data.get("subject")
        message = message_data.get("message")
        # my default value
        parent_message_id = 0

        grp_msg_error = self.group_validation.validate_group_message(subject, message)
        
        if grp_msg_error:
            return jsonify({
                "status": 400,
                "error": grp_msg_error
            }), 400

        admin = db.group_admin(group_id, current_user)

        if user or admin:
            group_message = db.add_group_message(current_user, group_id, subject, message, parent_message_id)

            return jsonify({
                "status": 201,
                "data": [group_message]
            }), 201
        
        return jsonify({
            "status": 404,
            "error": "User is not member of group."
        }), 404


    def get_group_messsages(self, group_id):
        """ get all group messages.
        """
        payload = user_identity()
        user = payload.get('email')

        check_group = db.return_group(group_id)

        if check_group is None:
            return jsonify({
                "error": "Given group ID does not exist.",
                "status": 404
            }), 404

        group_member = db.return_member(group_id, user)

        if group_member is None and user is None:
            return jsonify({
                "error": "You are not member of this group.",
                "status": 404
            }), 404

        group_messages = db.get_group_messages(group_id)

        if len(group_messages) > 0:
            return jsonify({
                "status": 200,
                "data": [message for message in group_messages]
            }), 200

        return jsonify({
            "error": "No group messages.",
            "status": 404
        }), 404

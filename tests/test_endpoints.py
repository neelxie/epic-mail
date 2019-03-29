from .test_structure import TestStructure
import json
""" File to handle tests for email endpoints. """


class TestEmail(TestStructure):
    """ Test Class for all emails endpoint"""

    def test_index_endpoint(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/api/v2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.decode(),
            '{"message":"Welcome to Epic Mail.","status":200}\n')

    def test_unauthorized_fetch_all_messages(self):
        """ Test to check route to fetch all emails."""
        response = self.app.get('/api/v2/messages')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data.decode(),
            '{"error":"Unauthorized! Token is missing.","status":401}\n')

    def test_wrong_method_error(self):
        """ Test wrong_method_error."""
        unread_error = self.app.post(
            '/api/v2/messages/unread', headers=self.headers)
        self.assertEqual(unread_error.status_code, 405)

    def test_get_wrong_url(self):
        """ Test method to check whether email is in list given its id."""
        resp = self.app.get('/api/v2/bk-em')
        self.assertEqual(resp.status_code, 404)

    def test_fetch_all_messages_empty(self):
        """ Test for getting all message while list is empty."""
        empty_list = self.app.get('/api/v2/messages', headers=self.forth_headers)
        self.assertEqual(empty_list.status_code, 400)
        

    def test_update_nonexistant_unread(self):
        """ Test method to edit message unread."""
        unread_error = self.app.get(
            '/api/v2/messages/unread', headers=self.headers)
        self.assertEqual(unread_error.status_code, 400)
        self.assertEqual(
            unread_error.data.decode(),
            '{"error":"No unread messages.","status":400}\n')

    def test_nonexistant_sent(self):
        resp = self.app.get(
            '/api/v2/messages/sent', headers=self.second_headers)
        self.assertEqual(resp.status_code, 400)

    def test_received(self):
        """ Test method to change message sent."""
        sent_error = self.app.get(
            '/api/v2/messages', headers=self.headers)
        self.assertEqual(
            sent_error.data.decode(),
            '{"error":"No messages in the inbox.","status":400}\n')
        
    def test_one_nonexistant_message(self):
        """ Test method to one message."""
        resp = self.app.get(
            '/api/v2/messages/1', headers=self.headers)
        self.assertEqual(
            resp.status_code, 400)


    def test_fetch_single_message_empty_list(self):
        """ Test for checking retrieval of one email."""
        response = self.app.get('/api/v2/messages/9', headers=self.second_headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.decode(),
            '{"error":"No email by that ID.","status":400}\n')


    def test_delete_message_nonexistent(self):
        """ Test for fetchng an item while list is empty."""
        response = self.app.delete(
            '/api/v2/messages/9',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(response.status_code, 400)


    def test_add_message(self):
        """ Add a message email."""
        sign_up = self.sign_up() 
        auth_post = self.app.post(
            "/api/v2/messages", content_type='application/json',
            headers=self.headers, data=json.dumps(self.test_message))
        self.assertEqual(auth_post.status_code, 201)
        # self.assertEqual(auth_post.data.decode(), 400)
        # would have checked for data returned but its too long
        # value from within returned response
        # messages list is empty bse user hasnt receved any
        save_msg = self.app.post(
            "/api/v2/messages/save", content_type='application/json',
            headers=self.headers, data=json.dumps(self.test_message))
        self.assertEqual(save_msg.status_code, 201)
        reply_msg = self.app.post(
            "/api/v2/messages/reply/1", content_type='application/json',
            headers=self.headers, data=json.dumps(self.test_message))
        self.assertEqual(reply_msg.status_code, 201)
        wrong_reply_msg = self.app.post(
            "/api/v2/messages/reply/x", content_type='application/json',
            headers=self.headers, data=json.dumps(self.test_message))
        self.assertEqual(wrong_reply_msg.status_code, 404)
        reply_nonexstant_msg = self.app.post(
            "/api/v2/messages/reply/200", content_type='application/json',
            headers=self.headers, data=json.dumps(self.test_message))
        self.assertEqual(reply_nonexstant_msg.status_code, 404)
        response = self.app.get(
            '/api/v2/messages', headers=self.headers)
        self.assertEqual(response.status_code, 400)
        read_msg = self.app.get(
            '/api/v2/messages/1', headers=self.headers)
        self.assertEqual(read_msg.status_code, 200)
        read_msg = json.loads(read_msg.data.decode())
        self.assertEqual(read_msg.get("status"), 200)
        add_another = self.app.post(
            "/api/v2/messages",
            content_type='application/json',
            headers=self.headers,
            data=json.dumps(self.test_other_message))
        msg_second = self.app.get(
            '/api/v2/messages/2',
            headers=self.headers)
        self.assertEqual(msg_second.status_code, 200)
        delete_msg = self.app.delete(
            '/api/v2/messages/1',
            headers=self.headers)
        self.assertEqual(delete_msg.status_code, 200)

    def test_retrieve_all_users(self):
        """ Test route for fetching all users on empty lst."""
        response = self.app.get(
            '/api/v2/auth/users',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def test_fetch_user(self):
        """ Fetch user. """
        response = self.app.get(
            '/api/v2/auth/users/1',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode(),
                         '{"error":"No user by that ID.","status":404}\n')
        

    def test_signing_up(self):
        """ Test for logging a single user."""
        exist = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_app_user))
        self.assertEqual(
            exist.status_code, 201)
        response = self.app.get(
            '/api/v2/auth/users',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(response.status_code, 200)
        email_taken = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_app_user))
        self.assertEqual(
            email_taken.data.decode(),
            '{"error":"Email already in registered.","status":401}\n')
        attribute_error = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps({}))
        self.assertEqual(attribute_error.data.decode(),
            '{"error":"You have not entered this/these user attributes.","missing attributes":"No data was entered.","status":400}\n')
        user_error = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_user_error))
        self.assertEqual(user_error.data.decode(),
            '{"error":"Firstname should have only letters between 2 and 15 charcters.","status":400}\n')
        sign_up_user_error = self.app.post(
            '/api/v2/auth/login', content_type='application/json',
            data=json.dumps(
                {
                    "user_name":"handn",
                    "password":"123456"}))
        self.assertEqual(sign_up_user_error.data.decode(),
            '{"error":"Login credentials are invalid.","status":400}\n')
        
        log_newer = self.app.post('/api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "email":"today@cia.gov",
                    "password":"asdfghj"}))
        self.assertEqual(log_newer.status_code, 200)
        sign_up_password = self.app.post('/api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "email":"today@cia.gov",
                    "password":235}))
        self.assertEqual(
            sign_up_password.data.decode(),
            '{"error":"Login credentials are invalid.","status":400}\n')
        sign_up_error = self.app.post(
            '/api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "email": 52556,
                    "password":"12dfdf"}))
        self.assertEqual(
            sign_up_error.data.decode(),
            '{"error":"Login credentials are invalid.","status":400}\n')
    

    def test_none_groups(self):
        """ Method to test no group. """
        no_group = self.app.get(
            '/api/v2/groups',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(no_group.status_code, 404)

    def test_change_group_name_for_none(self):
        """ Method change group name for none. """
        non_existant_group_name = self.app.patch(
            '/api/v2/groups/1/name',
            content_type='application/json',
            data=json.dumps(
                {
                    "group_name": "emputa"
                }
            ),
            headers=self.headers)
        self.assertEqual(non_existant_group_name.status_code, 404)

    def test_delete_for_non_existant_group(self):
        """ Method to delete for non existant group """
        non_existant_group = self.app.delete(
            '/api/v2/groups/1',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(non_existant_group.status_code, 404)

    def test_add_message_for_non_existant_group(self):
        """ Method to add message to non existant group """
        msg_non_existant_group = self.app.post(
            '/api/v2/groups/1/messages',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(msg_non_existant_group.status_code, 404)

    def test_get_messages_for_non_existant_group(self):
        """ Method to get messages from non existant group """
        msg_non_existant_group = self.app.get(
            '/api/v2/groups/1/messages',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(msg_non_existant_group.status_code, 404)

    def test_add_user_to_non_existant_group(self):
        """ Method to add users from non existant group """
        add_user_non_existant_group = self.app.post(
            '/api/v2/groups/1/users/9',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(add_user_non_existant_group.status_code, 404)

    def test_group_feature(self):
        """ test for goup feature. """
        new_group = self.app.post(
            '/api/v2/groups',
            content_type='application/json',
            headers=self.headers,
            data=json.dumps({
                "group_name": ""
            }))
        self.assertEqual(new_group.status_code, 400)
        new_group = self.app.post(
            '/api/v2/groups',
            content_type='application/json',
            headers=self.headers,
            data=json.dumps({
                "group_name": "zaweeze"
            }))
        self.assertEqual(new_group.status_code, 201)
        get_group = self.app.get(
            '/api/v2/groups',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(get_group.status_code, 200)
        get_user_group = self.app.get(
            '/api/v2/groups',
            content_type='application/json',
            headers=self.forth_headers)
        self.assertEqual(get_user_group.status_code, 404)
        group_name = self.app.patch(
            '/api/v2/groups/1/name',
            content_type='application/json',
            data=json.dumps(
                {
                    "group_name": 565625
                }),
            headers=self.headers)
        self.assertEqual(group_name.status_code, 400)
        change_group_name = self.app.patch(
            '/api/v2/groups/1/name',
            content_type='application/json',
            data=json.dumps(
                {
                    "group_name": "twazykoze"
                }),
            headers=self.headers)
        self.assertEqual(change_group_name.status_code, 200)
        add_to_group = self.app.get(
            '/api/v2/groups/1/messages',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(add_to_group.status_code, 404)
        add_non_existant_user_to_group = self.app.post(
            '/api/v2/groups/1/users/9',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(add_non_existant_user_to_group.status_code, 404)
        epc_user = self.app.post(
            "/api/v2/auth/signup", content_type='application/json', data=json.dumps(self.test_user_email))
        add_user_to_group = self.app.post(
            '/api/v2/groups/1/users/1',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(add_user_to_group.status_code, 201)
        delete_user_from_none_group = self.app.delete(
            '/api/v2/groups/9/users/1',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(delete_user_from_none_group.status_code, 404)
        delete_none_user_from_group = self.app.delete(
            '/api/v2/groups/1/users/9',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(delete_none_user_from_group.status_code, 404)
        get_group_msg = self.app.get(
            '/api/v2/groups/1/messages',
            content_type='application/json',
            headers=self.headers)
        self.assertEqual(get_group_msg.status_code, 200)
        add_group_msg = self.app.post(
            '/api/v2/groups/1/messages',
            content_type='application/json',
            data=json.dumps(
                {
                    "subject": "twakozeky",
                    "message": "zaweze zaweze"
                }
            ),
            headers=self.headers)
        self.assertEqual(add_group_msg.status_code, 201)



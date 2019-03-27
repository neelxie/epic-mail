import psycopg2
import psycopg2.extras
from pprint import pprint
import simplejson as json
import os

class DatabaseConnection:
    def __init__(self):
        
        if os.getenv('DB_NAME') == "test_flask":
            self.db_name = 'test_flask'
        else:
            self.db_name = 'flask_api'

        pprint(self.db_name)
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name, user='postgres', host='localhost', password='', port=5432)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            print('Connected to the database successfully')
    
        except:
            pprint("Failed to connect to database.")

    def create_db_tables(self):
        create_table = "CREATE TABLE IF NOT EXISTS users \
            ( first_name VARCHAR(15) NOT NULL, \
            last_name VARCHAR(15) NOT NULL, \
            phone_number VARCHAR(15), \
            email VARCHAR(20), \
            password VARCHAR(15), \
            is_admin BOOLEAN DEFAULT FALSE, \
            user_id SERIAL UNIQUE PRIMARY KEY);"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS messages \
            (message_id SERIAL UNIQUE PRIMARY KEY, \
            created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,\
            subject VARCHAR(30) NOT NULL, \
            message VARCHAR(200) NOT NULL, \
            sender_id INTEGER REFERENCES users(user_id), \
            receiver_id INTEGER NOT NULL, \
            parent_message_id INTEGER DEFAULT 0, \
            status VARCHAR DEFAULT 'unread', \
            sender_status VARCHAR DEFAULT 'sent');"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS groups \
            (group_id SERIAL UNIQUE PRIMARY KEY, \
            created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,\
            group_name VARCHAR(15) NOT NULL, \
            role VARCHAR DEFAULT 'user');"
        self.cursor.execute(create_table)


    def add_user(self, first_name, last_name, phone_number, email, password, is_admin):
        query = "INSERT INTO users (first_name, last_name, phone_number, email, password, is_admin) VALUES ('{}', '{}', '{}','{}', '{}', '{}') RETURNING *;".format(first_name, last_name, phone_number, email, password, is_admin)
        self.cursor.execute(query)
        new_user = self.cursor.fetchone()
        return new_user


    def add_message(self, subject, message, sender_id, receiver_id, parent_message_id, status, sender_status):

        query = "INSERT INTO messages (subject, message, sender_id, receiver_id, parent_message_id, status, sender_status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}')RETURNING *;".format(subject, message, sender_id, receiver_id, parent_message_id, status, sender_status)
        self.cursor.execute(query)
        email_message = self.cursor.fetchone()
        return email_message

    def create_group(self, group_name, role):
        query = "INSERT INTO groups (group_name, role) VALUES ('{}', '{}') RETURNING *;".format(group_name, role)
        self.cursor.execute(query)
        group = self.cursor.fetchone()
        return group

    def get_users(self):
        query = "SELECT * FROM users;"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users

    def all_app_groups(self):
        query = "SELECT * FROM groups;"
        self.cursor.execute(query)
        groups = self.cursor.fetchall()
        return groups

    def change_group_name(self, new_name, group_id):
        query = "UPDATE groups SET group_name = '{}' WHERE group_id = '{}' RETURNING *;".format(new_name, group_id)
        self.cursor.execute(query)

    def get_received(self, user_id):
        query = "SELECT * FROM messages WHERE receiver_id='{}' AND status='unread' OR status='read';".format(user_id)
        self.cursor.execute(query)
        messages = self.cursor.fetchall()
        return messages

    def get_a_message(self, message_id):
        query = "SELECT * FROM messages WHERE message_id= '{}';".format(message_id)
        self.cursor.execute(query)
        red_flag = self.cursor.fetchone()
        return red_flag

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = '{}';".format(user_id)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def get_unread(self, user_id):
        query = "SELECT * FROM messages WHERE receiver_id='{}' AND status='unread';".format(user_id)
        self.cursor.execute(query)
        all_unread = self.cursor.fetchall()
        return all_unread

    def fetch_sent(self, user_id):
        query = "SELECT * FROM messages WHERE sender_id='{}' AND status='sent';".format(user_id)
        self.cursor.execute(query)
        my_sent = self.cursor.fetchall()
        return my_sent

    def return_group(self, group_id):
        query = "SELECT * FROM groups WHERE group_id='{}';".format(group_id)
        self.cursor.execute(query)
        one_group = self.cursor.fetchone()
        return one_group

    def check_email(self, email):
        query = "SELECT * FROM users WHERE email='{}';".format(email)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def login(self, password, email):
        query = "SELECT email, password FROM users WHERE email='{}' and password='{}';".format(email, password)
        self.cursor.execute(query)
        user_exists = self.cursor.fetchone()
        return user_exists

    def delete_message(self, message_id):
        query = "DELETE FROM messages WHERE message_id = '{}';".format(message_id)
        self.cursor.execute(query)

    def drop_tables(self):
        query = "DROP TABLE messages;DROP TABLE users;"
        self.cursor.execute(query)
        return "Tables-dropped"

if __name__ == '__main__':
    db = DatabaseConnection()

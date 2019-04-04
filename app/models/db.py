import psycopg2
import psycopg2.extras
from pprint import pprint
import simplejson as json
import os

class DatabaseConnection:
    def __init__(self):
        
        try:
            self.connection = psycopg2.connect(
                dbname="d948o7njccndh6",
                user='bdbfssdboeprhi',
                host='ec2-54-225-242-183.compute-1.amazonaws.com',
                password='3a9b4fbe2cdf7504837c84c71ed741806a02e9441fbad891597f86b52b251d59',
                port=5432)
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
            is_admin BOOLEAN DEFAULT TRUE, \
            user_id SERIAL UNIQUE PRIMARY KEY);"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS messages \
            (message_id SERIAL UNIQUE PRIMARY KEY, \
            created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,\
            subject VARCHAR(30) NOT NULL, \
            message VARCHAR(200) NOT NULL, \
            sender_email TEXT NOT NULL, \
            receiver_email TEXT NOT NULL, \
            parent_message_id INTEGER DEFAULT 0, \
            status VARCHAR DEFAULT 'unread', \
            sender_status VARCHAR DEFAULT 'sent');"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS groups \
            (group_id SERIAL UNIQUE PRIMARY KEY, \
            created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,\
            created_by TEXT NOT NULL, \
            group_name VARCHAR(15) NOT NULL, \
            role VARCHAR DEFAULT 'admin');"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS group_members \
            (member_id SERIAL UNIQUE PRIMARY KEY, \
            added_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,\
            receiver_email TEXT NOT NULL, \
            group_id INTEGER REFERENCES groups(group_id), \
            user_role VARCHAR DEFAULT 'member');"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS group_messages \
            (message_id SERIAL UNIQUE PRIMARY KEY, \
            added_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,\
            sender_email TEXT NOT NULL, \
            group_id INTEGER NOT NULL, \
            subject VARCHAR(30) NOT NULL, \
            message VARCHAR(200) NOT NULL, \
            parent_message_id INTEGER DEFAULT 0 );"
        self.cursor.execute(create_table)

    def add_user(self, first_name, last_name, phone_number, email, password):
        query = "INSERT INTO users (first_name, last_name, phone_number, email, password) VALUES ('{}', '{}', '{}','{}', '{}') RETURNING *;".format(first_name, last_name, phone_number, email, password)
        self.cursor.execute(query)
        new_user = self.cursor.fetchone()
        return new_user


    def add_message(self, subject, message, sender_email, receiver_email, parent_message_id, status, sender_status):

        query = "INSERT INTO messages (subject, message, sender_email, receiver_email, parent_message_id, status, sender_status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}')RETURNING *;".format(
            subject, message, sender_email, receiver_email, parent_message_id, status, sender_status)
        self.cursor.execute(query)
        email_message = self.cursor.fetchone()
        return email_message

    def create_group(self, group_name, created_by, role):
        query = "INSERT INTO groups (group_name, created_by, role) VALUES ('{}', '{}', '{}') RETURNING *;".format(
            group_name, created_by, role)
        self.cursor.execute(query)
        group = self.cursor.fetchone()
        return group

    def add_user_to_group(self, group_id, receiver_email):
        query = "INSERT INTO group_members (group_id, receiver_email) VALUES ('{}', '{}') RETURNING *;".format(
            group_id, receiver_email)
        self.cursor.execute(query)
        group_member = self.cursor.fetchone()
        return group_member

    def add_group_message(self, sender_email, group_id, subject, message, parent_message_id):
        query = "INSERT INTO group_messages (sender_email, group_id, subject, message, parent_message_id) VALUES ('{}', '{}', '{}', '{}','{}')RETURNING *;".format(
            sender_email, group_id, subject, message, parent_message_id)
        self.cursor.execute(query)
        group_message = self.cursor.fetchone()
        return group_message

    def get_group_messages(self, group_id):
        query = "SELECT * FROM group_messages WHERE group_id='{}';".format(
            group_id)
        self.cursor.execute(query)
        all_group_messages = self.cursor.fetchall()
        return all_group_messages

    def get_users(self):
        query = "SELECT * FROM users;"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users

    def all_app_groups(self, created_by):
        query = "SELECT * FROM groups WHERE created_by = '{}';".format(
            created_by)
        self.cursor.execute(query)
        groups = self.cursor.fetchall()
        return groups

    def group_admin(self, group_id, user_id):
        query = "SELECT * FROM groups WHERE group_id= '{}' AND created_by = '{}';".format(
            group_id, user_id)
        self.cursor.execute(query)
        admin = self.cursor.fetchone()
        return admin

    def change_group_name(self, new_name, group_id):
        query = "UPDATE groups SET group_name = '{}' WHERE group_id = '{}';".format(
            new_name, group_id)
        self.cursor.execute(query)

    def get_received(self, receiver_email):
        query = "SELECT * FROM messages WHERE receiver_email='{}' AND status='unread';".format(
            receiver_email)
        self.cursor.execute(query)
        messages = self.cursor.fetchall()
        return messages

    def get_a_message(self, message_id):
        query = "SELECT * FROM messages WHERE message_id= '{}';".format(
            message_id)
        self.cursor.execute(query)
        red_flag = self.cursor.fetchone()
        return red_flag

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = '{}';".format(user_id)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def get_unread(self, user_id):
        query = "SELECT * FROM messages WHERE receiver_id='{}' AND status='unread';".format(
            user_id)
        self.cursor.execute(query)
        all_unread = self.cursor.fetchall()
        return all_unread

    def fetch_sent(self, sender_email):
        query = "SELECT * FROM messages WHERE sender_email='{}' AND sender_status='sent';".format(
            sender_email)
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

    def return_member(self, group_id, receiver_email):
        query = "SELECT * FROM group_members WHERE group_id='{}' AND receiver_email='{}';".format(
            group_id, receiver_email)
        self.cursor.execute(query)
        in_group = self.cursor.fetchone()
        return in_group

    def login(self, password, email):
        query = "SELECT email, password FROM users WHERE email='{}' and password='{}';".format(
            email, password)
        self.cursor.execute(query)
        user_exists = self.cursor.fetchone()
        return user_exists

    def delete_message(self, message_id):
        query = "DELETE FROM messages WHERE message_id = '{}';".format(
            message_id)
        self.cursor.execute(query)

    def delete_user_from_group(self, group_id, receiver_email):
        query = "DELETE FROM group_members WHERE group_id = '{}' AND receiver_email = '{}';".format(
            group_id, receiver_email)
        self.cursor.execute(query)

    def delete_group(self, created_by, group_id):
        query = "DELETE FROM groups WHERE created_by = '{}' AND group_id = '{}';".format(
            created_by, group_id)
        self.cursor.execute(query)

    def get_group_members(self, group_id):
        query = "SELECT * FROM group_members WHERE group_id='{}';".format(group_id)
        self.cursor.execute(query)
        members = self.cursor.fetchall()
        return members

    def drop_tables(self):
        query = "DROP TABLE group_members;DROP TABLE groups;DROP TABLE messages;DROP TABLE users;"
        self.cursor.execute(query)
        return "Tables-dropped"

if __name__ == '__main__':
    db = DatabaseConnection()

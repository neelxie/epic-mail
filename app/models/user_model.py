""" This is the Users' models file."""
from ..utils.validation import Valid

class Person:
    """ This is the base class for a person and
        holds the person's names and phone number.
    """

    def __init__(self, first_name, last_name, phone_number, password):
        """ Constructor for the base class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number #for reset feature
        self.password = password


class User:
    """ Class for Users.
    """

    def __init__(self, base, email, is_admin, user_id):
        """ Constructor for the User class.
        """
        self.base = base
        self.email = email
        self.is_admin = is_admin
        self.user_id = user_id

    def to_dict(self):
        """ Convert the user class to a JSON object at retrieval.
        """
        return {
            "first_name": self.base.first_name,
            "last_name": self.base.last_name,
            "phone_number": self.base.phone_number,
            "password": self.base.password,
            "email": self.email,
            "is_admin": self.is_admin,
            "user_id": self.user_id,
        }


class UserDB:
    """ Epic Mail users will be stored in this class.
    """

    valid = Valid()

    def __init__(self):
        """ app users will be held in a list
        """
        self.all_users = []

    def add_user(self, user):
        """ Method for creating a new user.
        """
        return self.all_users.append(user)

    def one_user(self, user_id):
        """ Method to return app user by ID.
        """
        for single_user in self.all_users:
            if single_user.user_id == user_id:
                return single_user
        return None

    def verify_email(self, email):
        """ Check whether email already exists in DB.
        """
        mail = [user for user in self.all_users if user.email == email]

        if len(mail) > 0:
            return "Email already has an account."
        return None

    def check_credentials(self, email, password):
        error = self.valid.validate_login(email, password)

        if error:
            return error

        temp = [
            user for user in self.all_users if user.email == email]

        if len(temp) != 1:
            return "Email not found. Please sign up."

        if temp[0].base.password != password:
            return "Wrong Password"

        return None

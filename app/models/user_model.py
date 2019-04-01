""" This is the Users' models file."""

class User:
    """ Class for model Users.
    """

    def __init__(self, person, email, user_id, is_admin, first_name, last_name, phone_number, password):
        """ Constructor for the User class.
        """
        self.email = email
        self.user_id = user_id
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number #for reset feature
        self.password = password

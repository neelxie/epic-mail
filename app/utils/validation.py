""" File contains a utility class for validation functions.
"""
import re

class Valid:
    """ Validation class for Epic mail app.
    """

    def valid_password(self, pass_word):
        """ Validate password.
        """
        is_valid = None
        if not isinstance(pass_word, str) or len(pass_word) < 6 or len(pass_word) > 15:
            is_valid = "Password has have 6 to 15 characters."
        return is_valid


    def valid_email(self, email):
        """ Validate email element.
        """
        bad_email = None
        if not isinstance(email, str) or self.check_for_space(email) is False or not re.match(r"[^@.]+@[a-z]+\.[a-z]+", email):
            bad_email = "Enter a valid email address."
        return bad_email
        

    def strip_token(self, token):
        """ Authentication helper function to strip the token.
        """
        new_token = token.lstrip('Bearer').strip(' ')
        return new_token


    def check_for_space(self, word):
        """ Function to check for white space in string."""
        value = word.find(' ')
        if value is not -1:
            return False


    def validate_string(self, my_string):
        """ Validation method for a valid string.
        """
        invalid_string = None

        if not isinstance(my_string, str) or my_string.isalpha() is False or self.check_for_space(my_string) is False:
            invalid_string = False

        elif my_string.isspace() or len(my_string) > 15 or len(my_string) < 2:
            invalid_string = False

        return invalid_string


    def validate_attributes(self, data, mylist):
        """Method to validate list elements.
        """
        if data is None or len(data) < 1:
            return "No data was entered or dict is empty."
        error_list = [attr for attr in mylist if data.get(attr) is None]
        if len(error_list) > 0:
            return error_list


    def check_other(self, email, pass_word, ad_min):
        """ Method to validate other user credentials.
        """
        other = None

        temp_emal = self.valid_email(email)
        if temp_emal is not None:
            other = self.valid_email(email)
        
        elif self.valid_password(pass_word) is not None:
            other = self.valid_password(pass_word)

        elif not isinstance(ad_min, bool):
            other = "is_admin must be a boolean."

        return other


    def check_base(self, first_name, last_name, phone_number):
        """ To validate the names for app user signing up.
        """
        error = None

        if self.validate_string(first_name) is False:
            error = "Firstname should have only letters between 2 and 15 chaarcters."

        elif self.validate_string(last_name) is False:
            error = "Last Name should have only letters between 2 and 15 chaarcters."

        # if not re.match(r"^[0-9]*$", phone_number):
        elif not phone_number or isinstance(int(phone_number), int) is False:
            error = "Phone number must be only digits and no white spaces."

        return error


    def validate_login(self, email, password):
        """method to check if login details are valid strings.
        """
        credential = None

        if self.valid_email(email) is not None:
            other = self.valid_email(email)
        
        elif self.valid_password(pass_word) is not None:
            other = self.valid_password(pass_word)

        return credential

    
    def check_for_invalid_function(self, func1, func2):
        """This function takes in two functions and checks if neither is none.
        """
        none_func = None

        error_one = func1
        error_two = func2

        if error_one:
            none_func = error_one
        elif error_two:
            none_func = error_two
        return none_func

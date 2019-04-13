""" File for test for the validation class."""
import unittest
from app.utils.validation import Valid

test_valid = Valid()
empty_lst = []

class TestValidClass(unittest.TestCase):
    """ Test Class for validation used in utility."""

    def test_validate_check_for_invalid_function(self):
        """ Test to validate check incident method."""
        self.assertEqual(
            test_valid.check_for_invalid_function(1, 0), 1)
        self.assertEqual(
            test_valid.check_for_invalid_function(0, 1), 1)
        self.assertEqual(
            test_valid.check_for_invalid_function(0, 0), None)

    def test_valid_phone_number(self):
        """ Test to validate check incident method."""
        self.assertEqual(
            test_valid.valid_phone_number(1), "Phone number has to be 10 numbers in quotes.")
        self.assertEqual(
            test_valid.valid_phone_number("gdhdgs"), "Phone number has to be 10 numbers in quotes.")
        self.assertEqual(
            test_valid.valid_phone_number("121"), "Phone number has to be 10 numbers in quotes.")

    def test_check_for_space(self):
        """ test check_for_space method."""
        self.assertEqual(test_valid.check_for_space('dhsh dss'), False)

    def test_validate_string(self): 
        """ test validate string."""
        self.assertEqual(test_valid.validate_string('bfhxbzchxzjvbhxzcvxvxzvzxvzx'), False)

    def test_validate_attributes(self):
        self.assertEqual(test_valid.validate_attributes("", empty_lst), "No data was entered.")

    def test_validate_composed_msg(self):
        self.assertEqual(test_valid.validate_composed_msg('', "gdshgdsh", 1), "The subject is invalid.")
        self.assertEqual(test_valid.validate_composed_msg('sdhshds', " ", 5), "Email message is has to be words.")


    def test_check_base(self):
        """ validation method check user base."""
        self.assertEqual(
            test_valid.check_base(
                "", "w2", "w22", ),
            "Firstname should have only letters between 2 and 15 charcters.")
        self.assertEqual(
            test_valid.check_base(
                "Derek", " ", "Kidrice"),
            "Last Name should have only letters between 2 and 15 charcters.")
        self.assertEqual(
            test_valid.check_base(
                "asdhddgob", "sdsdsds", "matz"),
            "Phone number has to be 10 numbers in quotes.")

    def test_check_other(self):
        """ user credentials method test."""
        
        self.assertEqual(
            test_valid.check_other(
                "asdgob", "sdsdsds"),
            "Enter a valid email address.")
        self.assertEqual(
            test_valid.check_other(
                "asd@hdd.gob", "sd"),
            "Password has have 6 to 15 characters.")


    def test_validate_login(self):
        """ validating entered login credentials."""
        self.assertEqual(
            test_valid.validate_login(
                "fake", ""),"Login credentials are invalid.")
        self.assertEqual(
            test_valid.validate_login(
                "fake@gdshh.kjk", "fafdufhdf"), None)

    def test_token_strip(self):
        """ Test stripped token."""
        self.assertEqual(
            test_valid.strip_token(
                "Bearer eyiamthe.greatestcoder.ever"), "eyiamthe.greatestcoder.ever")

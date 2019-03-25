""" File for test for the validation class."""
import unittest
from app.utils.validation import Valid

test_valid = Valid()

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
            "Phone number must be only digits and no white spaces.")

    def test_check_other(self):
        """ user credentials method test."""
        
        self.assertEqual(
            test_valid.check_other(
                "asdgob", "sdsdsds", False),
            "Enter a valid email address.")
        self.assertEqual(
            test_valid.check_other(
                "asd@hdd.gob", "sd", False),
            "Password has have 6 to 15 characters.")
        self.assertEqual(
            test_valid.check_other(
                "asd@hdd.gob", "sdsdsds", "asasas"),
            "is_admin must be a boolean.")


    def test_validate_login(self):
        """ validating entered login credentials."""
        self.assertEqual(
            test_valid.validate_login(
                "fake", ""),"Login credentials are invalid.")

    def test_token_strip(self):
        """ Test stripped token."""
        self.assertEqual(
            test_valid.strip_token(
                "Bearer eyiamthe.greatestcoder.ever"), "eyiamthe.greatestcoder.ever")

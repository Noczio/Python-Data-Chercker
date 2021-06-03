import unittest

from resources.exceptions.error import *
from src.check import check_arguments


class MyTestCase(unittest.TestCase):

    def test_float_are_valid_1(self):
        arguments = ("0.7", "0.1", "3", "5", "10.0")
        key_arguments = {"min": 0, "max": 10, "expected": float}
        are_valid = check_arguments(*arguments, **key_arguments)
        self.assertTrue(all(are_valid))

    def test_float_are_valid_2(self):
        arguments = ("0.7", "0.1", "3", "5", "10.0")
        key_arguments = {"min": 0, "max": 10, "expected": float}
        are_valid = check_arguments(*arguments, **key_arguments)
        self.assertTrue(all(are_valid))

    def test_float_are_valid_3(self):
        arguments = ("0.7", "0.1", "3", "5", "10.0")
        are_valid = check_arguments(*arguments, min=0, max=10, expected=float)
        self.assertTrue(all(are_valid))

    def test_float_are_not_valid_1(self):
        arguments = ("0.7", "0.1", "3", "5", "10.0", None, True)
        key_arguments = {"min": 0, "max": 10, "expected": str}
        are_valid = check_arguments(*arguments, **key_arguments)
        self.assertFalse(all(are_valid))

    def test_float_are_not_valid_2(self):
        arguments = ("0.7", "0.1", "3", "5", "10.0")
        key_arguments = {"min": 0, "max": 5, "expected": int}
        are_valid = check_arguments(*arguments, **key_arguments)
        self.assertFalse(all(are_valid))

    def test_raises_not_enough_args_error(self):
        with self.assertRaises(NotEnoughArgumentsError):
            arguments = ()
            key_arguments = {"min": 0, "max": 10, "expected": int}
            _ = check_arguments(*arguments, **key_arguments)

    def test_raises_key_error(self):
        with self.assertRaises(KeyError):
            arguments = ("0.7", "0.1", "3", "5", "10.0")
            key_arguments = {"left_border": 0, "max": 10, "expected": int}
            _ = check_arguments(*arguments, **key_arguments)

    def test_raises_wrong_args_error(self):
        with self.assertRaises(WrongArgumentsError):
            arguments = ("0.7", "0.1", "3", "5", "10.0")
            key_arguments = {"min": "XD", "max": 10, "expected": int}
            _ = check_arguments(*arguments, **key_arguments)


if __name__ == '__main__':
    unittest.main()

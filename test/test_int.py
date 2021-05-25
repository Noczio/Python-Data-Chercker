import unittest
from resources.concrete.int_check.arg_check import IntChecker


class MyTestCase(unittest.TestCase):
    def test_arg_are_valid(self):
        arguments = (0, "1", "2", "5")
        checker = IntChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertTrue(all(results))

    def test_arg_are_not_valid_1(self):
        arguments = (0, "1", "2.56", "5")
        checker = IntChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertFalse(all(results))

    def test_arg_are_not_valid_2(self):
        arguments = (0, "1", "2", "string")
        checker = IntChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertFalse(all(results))

    def test_arg_are_not_valid_3(self):
        arguments = ()
        checker = IntChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertFalse(all(results))


if __name__ == '__main__':
    unittest.main()

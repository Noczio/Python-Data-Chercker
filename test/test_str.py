import unittest
from resources.concrete.str_check.arg_check import StrChecker


class MyTestCase(unittest.TestCase):
    def test_arg_are_valid(self):
        arguments = (0, "1", "2", "5")
        checker = StrChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertTrue(all(results))

    def test_result_len_matches_valid_arg(self):
        arguments = (0, "1", "2", "5")
        expected = len(arguments)
        checker = StrChecker()
        results = checker.check(*arguments, low=0, high=5)
        results_len = sum(1 for _ in results)
        self.assertEqual(expected, results_len)

    def test_result_len_matches_not_valid_arg(self):
        arguments = (0, "1", bytes(1), "5")
        expected = len(arguments)
        checker = StrChecker()
        results = checker.check(*arguments, low=0, high=5)
        results_len = sum(1 for _ in results)
        self.assertEqual(expected, results_len)

    def test_arg_are_not_valid_1(self):
        arguments = (0, "1", bytes(1), "5")
        checker = StrChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertFalse(all(results))


if __name__ == '__main__':
    unittest.main()

import unittest
from resources.concrete.float_check.arg_check import FloatChecker


class MyTestCase(unittest.TestCase):
    def test_arg_are_valid(self):
        arguments = (0, "1", "2.56", "5")
        checker = FloatChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertTrue(all(results))

    def test_result_len_matches_valid_arg(self):
        arguments = (0, "1", "2.56", "5")
        expected = len(arguments)
        checker = FloatChecker()
        results = checker.check(*arguments, low=0, high=5)
        results_len = sum(1 for _ in results)
        self.assertEqual(expected, results_len)

    def test_result_len_matches_not_valid_arg(self):
        arguments = (0, "1", "nope", "5")
        expected = len(arguments)
        checker = FloatChecker()
        results = checker.check(*arguments, low=0, high=5)
        results_len = sum(1 for _ in results)
        self.assertEqual(expected, results_len)

    def test_arg_are_not_valid_1(self):
        arguments = (0, "1", "2.56", "5.1")
        checker = FloatChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertFalse(all(results))

    def test_arg_are_not_valid_2(self):
        arguments = (0, "1", "2.56", "string")
        checker = FloatChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertFalse(all(results))

    def test_arg_are_not_valid_3(self):
        arguments = ()
        checker = FloatChecker()
        results = checker.check(*arguments, low=0, high=5)
        self.assertFalse(all(results))


if __name__ == '__main__':
    unittest.main()

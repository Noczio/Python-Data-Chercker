from typing import Any

from resources.abstract.arg_check import ArgChecker


class FloatChecker(ArgChecker):

    def validate(self, value: Any, low: int, high: int) -> bool:
        """value is a variable that will be parsed to float, while low and high are the validation borders"""
        try:
            value_expected = float(value)
            return low <= value_expected <= high
        except ValueError:
            return False

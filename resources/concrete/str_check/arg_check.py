from typing import Any

from resources.abstract.arg_check import ArgChecker


class StrChecker(ArgChecker):

    def validate(self, value: Any, low: int, high: int) -> bool:
        """value is a variable that will be parsed to str, while low and high are the validation borders.
         None is not a valid input"""
        try:
            value_expected = str(value)
            return value is not None and low <= len(value_expected) <= high
        except ValueError:
            return False

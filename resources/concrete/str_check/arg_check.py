from typing import Any

from resources.abstract.arg_check import ArgChecker


class StrChecker(ArgChecker):

    def validate(self, value: Any, low: int, high: int) -> bool:
        try:
            value_expected = str(value)
            return low <= len(value_expected) <= high
        except ValueError:
            return False

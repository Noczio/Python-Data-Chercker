from typing import Any

from resources.abstract.arg_check import ArgChecker


class IntChecker(ArgChecker):

    def validate(self, value: Any, low: int, high: int) -> bool:
        try:
            value_expected = int(value)
            return low <= value_expected <= high
        except ValueError:
            return False

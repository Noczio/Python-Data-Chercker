from typing import Any

from resources.abstract.arg_check import ArgChecker


class StrChecker(ArgChecker):

    def validate(self, value: Any, low: int, high: int) -> bool:
        return low <= len(value) <= high

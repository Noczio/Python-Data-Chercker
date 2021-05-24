from typing import Any

from resources.abstract.arg_check import ArgChecker


class IntChecker(ArgChecker):

    def validate(self, value: Any, low: int, high: int) -> bool:
        return low <= int(value) <= high

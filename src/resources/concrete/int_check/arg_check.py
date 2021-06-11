from typing import Any

from resources.abstract.arg_check import ArgChecker


class IntChecker(ArgChecker):

    def validate(self, value: Any, low: int, high: int) -> bool:
        """[summary]
        value is a variable that will be parsed to int, while low and high are the validation borders

       Args:
            value (Any): [value that can be any python type]
            low (int): [integer value for left border]
            high (int): [integer value for right border]

        Returns:
            bool: [True if validation is withing range and it is a integer]
        """
        try:
            value_expected = int(value)
            return low <= value_expected <= high
        except ValueError:
            return False

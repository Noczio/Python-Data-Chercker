from abc import ABC, abstractmethod
from typing import Any, Generator


class ArgChecker(ABC):
    @abstractmethod
    def validate(self, value: Any, low: int, high: int) -> bool:
        """[summary]
        value is a variable of any type, while low and high are the validation borders. This returns either True or
        False

        Args:
            value (Any): [value that can be any python type]
            low (int): [integer value for left border]
            high (int): [integer value for right border]

        Returns:
            bool: [True if validation is withing range and ArgChecker condition is true]
        """
        pass

    def check(self, *args, low: int, high: int) -> Generator:
        """[summary]
        returns a generator based on a validation withing a range.

        Args:
            low (int): [integer value for left border]
            high (int): [integer value for right border]

        Yields:
            Generator: [generator of boolean values]
        """
        for element in args:
            yield self.validate(element, low, high)

from abc import ABC, abstractmethod
from typing import Any


class ArgChecker(ABC):

    @abstractmethod
    def validate(self, value: Any, low: int, high: int) -> bool:
        """value is a variable of any type, while low and high are the validation borders"""
        pass

    def check(self, *args, low: int, high: int):
        """returns a generator based on a validation withing a range"""
        for element in args:
            yield self.validate(element, low, high)





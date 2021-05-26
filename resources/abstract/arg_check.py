from abc import ABC, abstractmethod
from typing import Any


class ArgChecker(ABC):

    @abstractmethod
    def validate(self, value: Any, low: int, high: int) -> bool:
        pass

    def check(self, *args, low: int, high: int):
        for element in args:
            yield self.validate(element, low, high)





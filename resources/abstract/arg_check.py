from abc import ABC, abstractmethod
from typing import Any

from resources.exceptions.len_error import NotEnoughArgumentsError

from resources.exception.parse_error import CannotParseError


class ArgChecker(ABC):

    @abstractmethod
    def validate(self, value: Any, low: int, high: int) -> bool:
        pass

    def check(*args, low: int, high: int):
        try:
            if len(args):
                for element in args:
                    yield self.validate(element, low, high)
            else:
                raise NotEnoughArgumentsError("At least one argument must be provided")
        except (NotEnoughArgumentsError, CannotParseError):
            yield False

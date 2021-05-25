from typing import Any

from resources.concrete.float_check.arg_check import FloatChecker
from resources.concrete.int_check.arg_check import IntChecker
from resources.concrete.str_check.arg_check import StrChecker
from resources.exception.key_error import CheckerNotAvailable


def check_arguments(*args, left_border: int, right_border: int, expected: Any):
    options = {int: IntChecker(),
               float: FloatChecker(),
               str: StrChecker()}
    if expected in options.keys():
        checker = options[expected]
        results = checker.check(*args, low=left_border, high=right_border)
        return results
    else:
        raise KeyError("Expected type is not implemented")

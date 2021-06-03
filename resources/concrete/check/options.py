from typing import Any
from resources.concrete.float_check.arg_check import FloatChecker
from resources.concrete.int_check.arg_check import IntChecker
from resources.concrete.str_check.arg_check import StrChecker



options = {int: IntChecker(),
           float: FloatChecker(),
           str: StrChecker()}

def create_checker(checker_type: Any):
    if checker_type in options:
        return options[checker_type]
    else:
        raise KeyError(f"{checker_type} is not implemented")


def available_checkers():
    return tuple(options.keys())

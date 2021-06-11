from typing import Any

from resources.abstract.arg_check import ArgChecker
from resources.concrete.check_additionals.key_finder import find_key
from resources.concrete.float_check.arg_check import FloatChecker
from resources.concrete.int_check.arg_check import IntChecker
from resources.concrete.str_check.arg_check import StrChecker

options = {int: IntChecker(),
           float: FloatChecker(),
           str: StrChecker()}


def create_checker(checker_type: Any) -> ArgChecker:
    """[summary]
    returns an ArgChecker based on the checker type provided.

    Args:
        checker_type (Any): [any python type]

    Returns:
        ArgChecker: [implementation of ArgChecker abstract class]
    """
    return find_key(checker_type, search_dict=options, error_message=f"{checker_type} is not implemented")


def available_checkers() -> tuple:
    return tuple(options.keys())

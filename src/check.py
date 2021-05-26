from resources.concrete.float_check.arg_check import FloatChecker
from resources.concrete.int_check.arg_check import IntChecker
from resources.concrete.str_check.arg_check import StrChecker
from resources.exceptions.error import *


def check_arguments(*args, **kwargs):
    try:
        if len(args):
            minimum = kwargs["min"]
            maximum = kwargs["max"]
            expected = kwargs["expected"]

            options = {int: IntChecker(),
                       float: FloatChecker(),
                       str: StrChecker()}

            checker = options[expected]
            results = checker.check(*args, low=minimum, high=maximum)
            return results
        else:
            raise NotEnoughArgumentsError
    except KeyError:
        raise KeyError("min, max and expected must be provided")
    except NotEnoughArgumentsError:
        raise NotEnoughArgumentsError("At least one argument must be provided")

from resources.concrete.float_check.arg_check import FloatChecker
from resources.concrete.int_check.arg_check import IntChecker
from resources.concrete.str_check.arg_check import StrChecker
from resources.exceptions.error import *


def check_arguments(*args, **kwargs):
    """[summary]
    args can be Any data, but kwargs must have a min, max and expected. 
    Ex: are_valid = check_arguments(1, "2", 1.2, min=0, max=5, expected=int)
    are_valid is a generator of boolean values, which means that all(are_valid)
    will return False, because 1.2 is float, not a integer withting 0 and 5

    Raises:
        NotEnoughArgumentsError: [args len is not greater than 0]
        WrongArgumentsError: [min, max or expected have invalid values]
        KeyError: [min, max or expected kwargs were not provided]

    Returns:
        [Generator]: [a generator of boolean values. True if args are within range and expected type]
    """
    try:
        minimum = kwargs["min"]
        maximum = kwargs["max"]
        expected = kwargs["expected"]

        options = {int: IntChecker(),
                   float: FloatChecker(),
                   str: StrChecker()}

        min_max_checker = options[int]
        min_max_are_valid = min_max_checker.check(minimum, maximum, low=minimum, high=maximum)

        if len(args) == 0:
            raise NotEnoughArgumentsError("At least one argument must be provided")

        if all(min_max_are_valid) and expected in (options.keys()):
            checker = options[expected]
            results = checker.check(*args, low=minimum, high=maximum)
            return results          
        else:
            raise WrongArgumentsError("min, max or expected have invalid values")
                           
    except KeyError:
        raise KeyError("min, max and expected must be provided")
    except (NotEnoughArgumentsError, WrongArgumentsError):
        raise

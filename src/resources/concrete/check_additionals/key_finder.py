from typing import Any

from resources.exceptions.error import *


def find_key(*objective_key, search_dict: dict = None, error_message: str = "Keys not found in dict") -> Any:
    """[summary]
    returns search dict value if objective key is in the dictionary. objective key can be multiple arguments.

    Args:
        search_dict (dict, optional): [dict where keys are stored]. Defaults to None.
        error_message (str, optional): [message displayed when MissingKeyArgument is raised].
        Defaults to "Keys not found in dict".

    Raises:
        NotEnoughArgumentsError: [search dict and a objective key must be provided]
        MissingKeyArgument: [objective key was not found in search dict]

    Returns:
        Any: [value of search dict]
    """
    if search_dict is None or len(objective_key) == 0:
        raise NotEnoughArgumentsError("A search dict and a objective key must be provided")

    for key in objective_key:
        if key in search_dict.keys():
            return search_dict[key]

    raise MissingKeyArgument(error_message)

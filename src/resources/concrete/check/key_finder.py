from typing import Any

from resources.exceptions.error import *


def find_key(*objective_key, search_dict: dict = None, error_message: str = "Keys not found in dict") -> Any:
    if search_dict is None or len(objective_key) <= 0:
        raise NotEnoughArgumentsError("A search dict and a objective key must be provided")
    else:
        for key in objective_key:
            if key in search_dict.keys():
                return search_dict[key]
        raise MissingKeyArgument(error_message)

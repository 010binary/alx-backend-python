#!/usr/bin/env python3
"""
Task 10 package
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence containing anything
    """
    if lst:
        return lst[0]
    else:
        return None

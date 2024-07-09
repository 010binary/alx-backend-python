#!/usr/bin/env python3
"""
async comp collect 10 int
"""
from typing import List
from importlib import import_module as check


# Importing the other function
async_generator = check('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects the 10 valuse
    """
    result = [x async for x in async_generator()]
    return result

#!/usr/bin/env python3
"""
async comp collect 10 int
"""
from typing import List
import asyncio


# Importing the other function
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    collects the 10 valuse
    """
    random_float = [x for x in async_generator()]
    return random_float

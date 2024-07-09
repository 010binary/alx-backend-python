#!/usr/bin/env python3
"""
Task Two
"""
from importlib import import_module as check
import time
import asyncio


# Importing the previous function
async_comprehension = check('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure async_comprehension
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time

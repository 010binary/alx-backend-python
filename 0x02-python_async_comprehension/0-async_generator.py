#!/usr/bin/env python3
"""
async comprehension
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine will run 10x and
    yield random int 1-10
    so the type generator expects 3 params
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

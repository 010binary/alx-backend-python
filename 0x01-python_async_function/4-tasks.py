#!/usr/bin/env python3
"""
dolla dolla dolla
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple tasks at the same time with asyncio
    """
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
        delays = sorted(delays)
    return delays

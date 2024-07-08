#!/usr/bin/env python3
"""
creating a normal time function
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    use regular function syntax
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

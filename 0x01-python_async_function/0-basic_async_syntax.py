#!/usr/bin/env python3
import asyncio
import random
"""Using asynchronous coroutine"""


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

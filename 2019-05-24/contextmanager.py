import time
import asyncio
from contextlib import contextmanager, asynccontextmanager


async def a():
    await asyncio.sleep(3)
    return 'A'


async def b():
    await asyncio.sleep(1)
    return 'B'


async def s1():
    return await asyncio.gather(a(), b())


@contextmanager
def timed(func):
    start = time.perf_counter()
    yield asyncio.run(func())
    print(f'Cost: {time.perf_counter() - start}')


@asynccontextmanager
async def async_timed(func):
    start = time.perf_counter()
    yield await func()
    print(f'Cost: {time.perf_counter() - start}')

def sync():
    with timed(s1) as rv:
        print(f'Result: {rv}')

async def main():
    async with async_timed(s1) as rv:
        print(f'Result: {rv}')


if __name__ == '__main__':
    sync()
    asyncio.run(main())

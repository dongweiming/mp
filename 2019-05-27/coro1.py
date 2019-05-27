import asyncio
from functools import partial


async def a():
    await asyncio.sleep(1)
    return 'A'


def callback(future):
    print(f'Result: {future.result()}')


def callback2(future, n):
    print(f'Result: {future.result()}, N: {n}')


async def b1():
    task = asyncio.create_task(a())
    task.add_done_callback(callback)
    await task


async def b2():
    task = asyncio.create_task(a())
    task.add_done_callback(partial(callback2, n=1))
    await task


if __name__ == '__main__':
    for f in (b1, b2):
        asyncio.run(f())

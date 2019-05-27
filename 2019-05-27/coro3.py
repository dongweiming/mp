import time
import asyncio
import concurrent.futures
from functools import partial


def a():
    time.sleep(1)
    return 'A'


async def b():
    await asyncio.sleep(1)
    return 'B'


async def c():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, a)


def show_perf(func):
    print('*' * 20)
    start = time.perf_counter()
    asyncio.run(func())
    print(f'{func.__name__} Cost: {time.perf_counter() - start}')


async def c1():
    loop = asyncio.get_running_loop()
    await asyncio.gather(
        loop.run_in_executor(None, a),
        b()
    )


async def c2():
    await asyncio.gather(b(), c())


async def c3():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor() as e:
        print(await asyncio.gather(
            loop.run_in_executor(e, a),
            b()
        ))


if __name__ == '__main__':
    for f in (c1, c2, c3):
        show_perf(f)

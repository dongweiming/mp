import time
import asyncio


async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')


async def s1():
    await a()
    await b()


async def s2():
    await asyncio.create_task(a())
    await asyncio.create_task(b())


async def c1():
    await asyncio.gather(a(), b())


async def c2():
    await asyncio.wait([a(), b()])


async def c3():
    task1 = asyncio.create_task(a())
    task2 = asyncio.create_task(b())
    await task1
    await task2


async def c4():
    task = asyncio.create_task(b())
    await a()
    await task


async def c5():
    task = asyncio.ensure_future(b())
    await a()
    await task


async def c6():
    loop = asyncio.get_event_loop()
    task = loop.create_task(b())
    await a()
    await task


def show_perf(func):
    print('*' * 20)
    start = time.perf_counter()
    asyncio.run(func())
    print(f'{func.__name__} Cost: {time.perf_counter() - start}')


if __name__ == '__main__':
    for f in (s1, s2, c1, c2, c3, c4, c5, c6):
        show_perf(f)

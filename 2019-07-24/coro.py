import random
import asyncio


async def a():
    print('Suspending a')
    await asyncio.sleep(2)
    print('Resuming a')
    return 'A'


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')
    return 'B'


async def c1():
    task1 = asyncio.shield(a())
    task2 = asyncio.create_task(b())
    task1.cancel()
    await asyncio.gather(task1, task2, return_exceptions=True)


async def c2():
    task1 = asyncio.shield(b())
    task2 = asyncio.create_task(a())
    task1.cancel()
    await asyncio.gather(task1, task2, return_exceptions=True)


async def c3():
    task1 = asyncio.shield(a())
    task2 = asyncio.create_task(b())
    ts = asyncio.gather(task1, task2, return_exceptions=True)
    task1.cancel()
    await ts


async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()


def c4():
    loop = asyncio.get_event_loop()
    outer = asyncio.shield(a())
    outer.cancel()
    loop.create_task(stop_after(loop, 3))

    loop.run_forever()
    print(outer.cancelled())


async def cancel_after(task, when):
    await asyncio.sleep(when)
    task.cancel()


async def d(n):
    print(f'Suspending a with {n}')
    await asyncio.sleep(2)
    print(f'Resuming a with {n}')
    return 'A'


async def c5():
    loop = asyncio.get_event_loop()
    n = random.randint(1, 100)
    outer = asyncio.shield(d(n))
    loop.create_task(cancel_after(outer, 1))
    try:
        await outer
    except asyncio.CancelledError:
        print('Cancelled!')


async def c6():
    n = random.randint(1, 100)
    task1 = asyncio.shield(d(n))
    task2 = asyncio.create_task(b())
    task1.cancel()
    await asyncio.gather(task1, task2, return_exceptions=True)


def main():
    loop = asyncio.get_event_loop()
    outer = asyncio.shield(a())
    outer.cancel()
    loop.create_task(stop_after(loop, 3))

    loop.run_forever()
    print(outer.cancelled())


if __name__ == '__main__':
    main()

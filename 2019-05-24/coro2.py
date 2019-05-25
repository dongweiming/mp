import asyncio

async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')
    return 'A'


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')
    return 'B'


async def c1():
    task1 = asyncio.create_task(a())
    task2 = asyncio.create_task(b())
    task1.cancel()
    print(await asyncio.gather(task1, task2))


async def c2():
    task1 = asyncio.create_task(a())
    task2 = asyncio.create_task(b())
    task1.cancel()
    print(await asyncio.gather(task1, task2, return_exceptions=True))


async def c3():
    task1 = asyncio.shield(a())
    task2 = asyncio.create_task(b())
    task1.cancel()
    await asyncio.gather(task1, task2, return_exceptions=True)


async def c4():
    task1 = asyncio.shield(a())
    task2 = asyncio.create_task(b())
    ts = asyncio.gather(task1, task2, return_exceptions=True)
    task1.cancel()
    await ts


if __name__ == '__main__':
    for f in (c1, c2, c3, c4):
        print('*' * 20)
        try:
            asyncio.run(f())
        except asyncio.CancelledError as e:
            print(e)

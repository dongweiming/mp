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
    print(await asyncio.gather(a(), b()))


async def c2():
    print(await asyncio.wait([a(), b()]))


async def c3():
    print(await asyncio.wait(
        [a(), b()],
        return_when=asyncio.tasks.FIRST_COMPLETED))


if __name__ == '__main__':
    for f in (c1, c2, c3):
        asyncio.run(f())

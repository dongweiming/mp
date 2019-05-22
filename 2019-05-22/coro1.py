import asyncio


async def a():
    print('Suspending a')
    await asyncio.sleep(0)
    print('Resuming a')


async def b():
    print('In b')


async def main():
    await asyncio.gather(a(), b())


if __name__ == '__main__':
    asyncio.run(main())

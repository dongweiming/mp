import asyncio

async def waiting(r):
    print('Hello ', r)
    await asyncio.sleep(0.5)
    return r


async def serial():
    a = await waiting(1)
    b = await waiting(2)
    c = await waiting(a + b)
    print(c)

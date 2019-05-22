import asyncio
import random
import aiohttp

NUMBERS = random.sample(range(100), 7)
URL = 'http://httpbin.org/get?a={}'
sema = asyncio.Semaphore(3)


async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']


async def collect_result(a):
    with (await sema):
        return await fetch_async(a)


async def produce(queue):
    for num in NUMBERS:
        print('producing {}'.format(num))
        item = (num, num)
        await queue.put(item)


async def consume(queue):
    while 1:
        item = await queue.get()
        num = item[0]
        rs = await collect_result(num)
        print('consuming {}...'.format(rs))
        queue.task_done()


async def run():
    queue = asyncio.PriorityQueue()
    consumer = asyncio.ensure_future(consume(queue))
    await produce(queue)
    await queue.join()
    consumer.cancel()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()

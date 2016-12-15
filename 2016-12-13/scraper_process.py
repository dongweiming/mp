# coding=utf-8
import time
import math
import requests
import aiohttp
import asyncio
from queue import Queue
from concurrent.futures import ProcessPoolExecutor

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'

def fetch(a):
    r = requests.get(URL.format(a))
    return r.json()['args']['a']


start = time.time()

with ProcessPoolExecutor(max_workers=3) as executor:
    for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
        print('fetch({}) = {}'.format(num, result))

print('Use requests+ProcessPoolExecutor cost: {}'.format(time.time() - start))

async def run_scraper_tasks(executor):
    loop = asyncio.get_event_loop()

    blocking_tasks = []
    for num in NUMBERS:
        task = loop.run_in_executor(executor, fetch, num)
        task.__num = num
        blocking_tasks.append(task)

    completed, pending = await asyncio.wait(blocking_tasks)
    results = {t.__num: t.result() for t in completed}
    for num, result in sorted(results.items(), key=lambda x: x[0]):
        print('fetch({}) = {}'.format(num, result))

start = time.time()
executor = ProcessPoolExecutor(3)
event_loop = asyncio.get_event_loop()

event_loop.run_until_complete(
    run_scraper_tasks(executor)
)

print('Use asyncio+requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))

async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']

start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [fetch_async(num) for num in NUMBERS]
results = event_loop.run_until_complete(asyncio.gather(*tasks))

for num, result in zip(NUMBERS, results):
    print('fetch({}) = {}'.format(num, result))

# event_loop.close()

print('Use asyncio+aiohttp cost: {}'.format(time.time() - start))

start = time.time()
executor = ProcessPoolExecutor(3)

async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return a, data['args']['a']


def sub_loop(numbers):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [fetch_async(num) for num in numbers]
    results = loop.run_until_complete(asyncio.gather(*tasks))
    for num, result in results:
        print('fetch({}) = {}'.format(num, result))


async def run(executor, numbers):
    await asyncio.get_event_loop().run_in_executor(executor, sub_loop, numbers)


def chunks(l, size):
    n = math.ceil(len(l) / size)
    for i in range(0, len(l), n):
        yield l[i:i + n]


event_loop = asyncio.get_event_loop()
tasks = [run(executor, chunked) for chunked in chunks(NUMBERS, 3)]
results = event_loop.run_until_complete(asyncio.gather(*tasks))

print('Use asyncio+aiohttp+ThreadPoolExecutor cost: {}'.format(time.time() - start))

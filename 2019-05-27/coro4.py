import asyncio
from functools import partial
from threading import Thread


async def a():
    await asyncio.sleep(1)
    return 'A'


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def shutdown(loop):
    loop.stop()


async def b1():
    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()

    future = asyncio.run_coroutine_threadsafe(a(), new_loop)
    print(future)
    print(f'Result: {future.result(timeout=2)}')
    new_loop.call_soon_threadsafe(partial(shutdown, new_loop))


if __name__ == '__main__':
    for f in (b1,):
        asyncio.run(f())

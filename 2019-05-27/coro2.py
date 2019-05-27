import asyncio
from functools import partial


def mark_done(future, result):
    print(f'Set to: {result}')
    future.set_result(result)


async def b1():
    loop = asyncio.get_event_loop()
    fut = asyncio.Future()
    loop.call_soon(mark_done, fut, 'the result')
    loop.call_soon(partial(print, 'Hello', flush=True))
    loop.call_soon(partial(print, 'Greeting', flush=True))
    print(f'Done: {fut.done()}')
    await asyncio.sleep(0)
    print(f'Done: {fut.done()}, Result: {fut.result()}')


async def b2():
    loop = asyncio.get_event_loop()
    fut = asyncio.Future()
    loop.call_later(2, mark_done, fut, 'the result')
    loop.call_later(1, partial(print, 'Hello'))
    loop.call_later(1, partial(print, 'Greeting'))
    print(f'Done: {fut.done()}')
    await asyncio.sleep(2)
    print(f'Done: {fut.done()}, Result: {fut.result()}')


async def b3():
    loop = asyncio.get_event_loop()
    now = loop.time()
    fut = asyncio.Future()
    loop.call_at(now + 2, mark_done, fut, 'the result')
    loop.call_at(now + 1, partial(print, 'Hello', flush=True))
    loop.call_at(now + 1, partial(print, 'Greeting', flush=True))
    print(f'Done: {fut.done()}')
    await asyncio.sleep(2)
    print(f'Done: {fut.done()}, Result: {fut.result()}')


if __name__ == '__main__':
    for f in (b1, b2, b3):
        asyncio.run(f())

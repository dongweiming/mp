import asyncio
import functools


def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def test(locker, lock):
    print('{} waiting for the lock'.format(locker))
    with await lock:
        print('{} acquired lock'.format(locker))
    print('{} released lock'.format(locker))


async def main(loop):
    lock = asyncio.Lock()
    await lock.acquire()
    loop.call_later(0.1, functools.partial(unlock, lock))
    await asyncio.wait([test('l1', lock), test('l2', lock)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()

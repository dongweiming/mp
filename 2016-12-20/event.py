import asyncio
import functools


def set_event(event):
    print('setting event in callback')
    event.set()


async def test(name, event):
    print('{} waiting for event'.format(name))
    await event.wait()
    print('{} triggered'.format(name))


async def main(loop):
    event = asyncio.Event()
    print('event start state: {}'.format(event.is_set()))
    loop.call_later(
        0.1, functools.partial(set_event, event)
    )
    await asyncio.wait([test('e1', event), test('e2', event)])
    print('event end state: {}'.format(event.is_set()))

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()

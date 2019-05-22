import asyncio
import functools


async def consumer(cond, name, second):
    await asyncio.sleep(second)
    with await cond:
        await cond.wait()
        print('{}: Resource is available to consumer'.format(name))



async def producer(cond):
    await asyncio.sleep(2)
    for n in range(1, 3):
        with await cond:
            print('notifying consumer {}'.format(n))
            cond.notify(n=n)
        await asyncio.sleep(0.1)

async def producer2(cond):
    await asyncio.sleep(2)
    with await cond:
        print('Making resource available')
        cond.notify_all()

async def main(loop):
    condition = asyncio.Condition()

    task = loop.create_task(producer(condition))
    consumers = [consumer(condition, name, index)
                 for index, name in enumerate(('c1', 'c2'))]
    await asyncio.wait(consumers)

    task = loop.create_task(producer2(condition))
    consumers = [consumer(condition, name, index)
                 for index, name in enumerate(('c1', 'c2'))]
    await asyncio.wait(consumers)
    task.cancel()


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()

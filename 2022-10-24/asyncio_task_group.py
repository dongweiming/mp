import asyncio

async def core_success():
    print('success')


async def core_value_error():
    raise ValueError


async def core_type_error():
    raise TypeError


async def core_long():
    try:
        await asyncio.sleep(1)
        print('long task done!')
    except asyncio.CancelledError:
        print('cancelled!')
        raise


async def gather():
    results = await asyncio.gather(
        core_success(),
        core_value_error(),
        core_type_error(),
        return_exceptions=True)
    for r in results:
        match r:
            case ValueError():
                print('value_error')
            case TypeError():
                print('type_error')
            case _:
                print(r)


async def task_group1():
    try:
        async with asyncio.TaskGroup() as g:
            task1 = g.create_task(core_success())
            task2 = g.create_task(core_value_error())
            task3 = g.create_task(core_type_error())
        results = [task1.result(), task2.result(), task3.result()]
    except* ValueError as e:
        raise
    except* TypeError as e:
        raise


async def task_group2():
    try:
        async with asyncio.TaskGroup() as g:
            task1 = g.create_task(core_success())
            task2 = g.create_task(core_value_error())
            task3 = g.create_task(core_long())
        results = [task1.result(), task2.result(), task3.result()]
    except* ValueError as e:
        print(f'{e=}')
    except* TypeError as e:
        print(f'{e=}')

    for r in [task1, task2, task3]:
        if not r.done():
            r.cancel()


asyncio.run(task_group2())

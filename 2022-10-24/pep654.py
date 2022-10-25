import aiohttp
import asyncio

async def core_success():
    return('success')


async def core_error1():
    raise asyncio.TimeoutError


async def core_error2():
    raise aiohttp.ClientOSError


async def core_error3():
    raise aiohttp.ClientConnectionError


async def raise_errors():
    results = await asyncio.gather(
        core_success(),
        core_error1(),
        core_error2(),
        core_error3(),
        return_exceptions=True)
    for r in results:
        match r:
            case asyncio.TimeoutError():
                print('timeout_error')
            case aiohttp.ClientOSError():
                print('client_os_error')
            case aiohttp.ClientConnectionError():
                print('client_connection_error')
            case _:
                print(r)


asyncio.run(raise_errors())

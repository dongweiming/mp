import aiofiles
import asyncio
import aiohttp

url = 'https://movie.douban.com/top250?start='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'  # noqa
}


async def fetch(session, page):
    r = await session.get(f'{url}{page*25}', headers=headers)
    async with aiofiles.open(f'top250-{page}.html', mode='w') as f:
        await f.write(await r.text())


async def main():
    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [asyncio.ensure_future(fetch(session, p)) for p in range(25)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

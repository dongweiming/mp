import requests

url = 'https://movie.douban.com/top250?start='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'  # noqa
}


def fetch(session, page):
    with (session.get(f'{url}{page*25}', headers=headers) as r,
          open(f'top250-{page}.html', 'w') as f):
        f.write(r.text)


def main():
    with requests.Session() as session:
        for p in range(25):
            fetch(session, p)


if __name__ == '__main__':
    main()

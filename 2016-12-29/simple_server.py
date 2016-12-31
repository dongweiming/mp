from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)


@app.route('/get')
async def test(request):
    a = request.args.get('a')
    return json({'args': {'a': a}})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

from multiprocessing.managers import BaseManager

host = '127.0.0.1'
port = 9030
authkey = 'secret'

shared_list = []


class RemoteManager(BaseManager):
    pass


RemoteManager.register('get_list', callable=lambda: shared_list)
mgr = RemoteManager(address=(host, port), authkey=authkey)
server = mgr.get_server()
server.serve_forever()


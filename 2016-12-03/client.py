from multiprocessing.managers import BaseManager

host = '127.0.0.1'
port = 9030
authkey = 'secret'


class RemoteManager(BaseManager):
    pass


RemoteManager.register('get_list')
mgr = RemoteManager(address=(host, port), authkey=authkey)
mgr.connect()

l = mgr.get_list()
print l
l.append(1)
print mgr.get_list()



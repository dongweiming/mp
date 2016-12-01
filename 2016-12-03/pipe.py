from multiprocessing import Process, Pipe


def f(conn):
    conn.send(Pipe())
    conn.close()


parent_conn, child_conn = Pipe()
p = Process(target=f, args=(child_conn,))
p.start()
print parent_conn.recv()
p.join()

#coding=utf-8
from multiprocessing import Pool, Process, Pipe
from itertools import izip


def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)


def hasmultiprocess():
    pool = Pool(2)
    print pool.map(fib, [35] * 2)

# hasmultiprocess() 执行正常

def spawn(f):
    def func(pipe, item):
        pipe.send(f(item))
        pipe.close()
    return func


def parmap(f, items):
    pipe = [Pipe() for _ in items]
    proc = [Process(target=spawn(f),
                    args=(child, item))
            for item, (parent, child) in izip(items, pipe)]
    [p.start() for p in proc]
    [p.join() for p in proc]
    return [parent.recv() for (parent, child) in pipe]


class CalculateFib(object):
    @classmethod
    def fib(cls, n):
        if n<= 2:
            return 1
        return cls.fib(n-1) + cls.fib(n-2)

    def map_run(self):
        pool = Pool(2)
        print pool.map(self.fib, [35] * 2)

    def parmap_run(self):
        print parmap(self.fib, [35] * 2)


cl = CalculateFib()
# cl.map_run()  # 执行报错

cl.parmap_run()

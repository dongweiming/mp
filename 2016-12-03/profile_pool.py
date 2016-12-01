# coding=utf-8
import time
import multiprocessing


def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        print 'COST: {}'.format(end - start)
    return wrapper


def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)


@profile
def nomultiprocess():
    fib(35)
    fib(35)


@profile
def hasmultiprocess():
    pool = multiprocessing.Pool(2)
    pool.map(fib, [35] * 2)


nomultiprocess()
hasmultiprocess()

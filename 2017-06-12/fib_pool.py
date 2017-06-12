# coding=utf-8
import time
from multiprocessing.pool import Pool

NUMBERS = range(25, 38)


def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)


start = time.time()

pool = Pool(3)
for num, result in zip(NUMBERS, pool.map(fib, NUMBERS)):
    print('fib({}) = {}'.format(num, result))

print('COST: {}'.format(time.time() - start))





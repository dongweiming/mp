# coding=utf-8
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

NUMBERS = range(25, 38)


def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)


start = time.time()

with ProcessPoolExecutor(max_workers=3) as executor:
    chunksize, extra = divmod(len(NUMBERS), executor._max_workers * 4)
    for num, result in zip(NUMBERS, executor.map(fib, NUMBERS,
                                                 chunksize=chunksize)):
        print('fib({}) = {}'.format(num, result))

print('COST: {}'.format(time.time() - start))





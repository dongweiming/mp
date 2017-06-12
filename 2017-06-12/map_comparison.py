# coding=utf-8
import time
from multiprocessing.pool import Pool
from concurrent.futures import as_completed, ProcessPoolExecutor

NUMBERS = range(1, 100000)
K = 50


def f(x):
    r = 0
    for k in range(1, K+2):
        r += x ** (1 / k**1.5)
    return r


print('multiprocessing.pool.Pool:\n')
start = time.time()

l = []
pool = Pool(3)
for num, result in zip(NUMBERS, pool.map(f, NUMBERS)):
    l.append(result)
print(len(l))
print('COST: {}'.format(time.time() - start))

print('ProcessPoolExecutor without chunksize:\n')
start = time.time()

l = []
with ProcessPoolExecutor(max_workers=3) as executor:
    for num, result in zip(NUMBERS, executor.map(f, NUMBERS)):
        l.append(result)

print(len(l))

print('COST: {}'.format(time.time() - start))

print('ProcessPoolExecutor with chunksize:\n')
start = time.time()

l = []
with ProcessPoolExecutor(max_workers=3) as executor:
    # 保持和multiprocessing.pool的默认chunksize一样
    chunksize, extra = divmod(len(NUMBERS), executor._max_workers * 4)

    for num, result in zip(NUMBERS, executor.map(f, NUMBERS, chunksize=chunksize)):
        l.append(result)

print(len(l))

print('COST: {}'.format(time.time() - start))

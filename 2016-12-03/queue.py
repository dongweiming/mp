# coding=utf-8
import time
from multiprocessing import Process, JoinableQueue, Queue
from random import random


tasks_queue = JoinableQueue()
results_queue = Queue()


def double(n):
    return n * 2


def producer(in_queue):
    while 1:
        wt = random()
        time.sleep(wt)
        in_queue.put((double, wt))
        if wt > 0.9:
            in_queue.put(None)
            print 'stop producer'
            break


def consumer(in_queue, out_queue):
    while 1:
        task = in_queue.get()
        if task is None:
            break
        func, arg = task
        result = func(arg)
        in_queue.task_done()
        out_queue.put(result)

processes = []

p = Process(target=producer, args=(tasks_queue,))
p.start()
processes.append(p)

p = Process(target=consumer, args=(tasks_queue, results_queue))
p.start()
processes.append(p)

tasks_queue.join()

for p in processes:
    p.join()

while 1:
    if results_queue.empty():
        break
    result = results_queue.get()
    print 'Result:', result

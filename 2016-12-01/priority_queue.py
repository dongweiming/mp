# coding=utf-8
import time
import threading
from random import randint
from Queue import PriorityQueue


q = PriorityQueue()


def double(n):
    return n * 2


def producer():
    count = 0
    while 1:
        if count > 5:
            break
        pri = randint(0, 100)
        print 'put :{}'.format(pri)
        q.put((pri, double, pri))  # (priority, func, args)
        count += 1


def consumer():
    while 1:
        if q.empty():
            break
        pri, task, arg = q.get()
        print '[PRI:{}] {} * 2 = {}'.format(pri, arg, task(arg))
        q.task_done()
        time.sleep(0.1)


t = threading.Thread(target=producer)
t.start()
time.sleep(1)
t = threading.Thread(target=consumer)
t.start()


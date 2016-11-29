import time
import threading

def consumer(cond):
    t = threading.currentThread()
    with cond:
        cond.wait()
        print '{}: Resource is available to consumer'.format(t.name)



def producer(cond):
    t = threading.currentThread()
    with cond:
        print '{}: Making resource available'.format(t.name)
        cond.notifyAll()


condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()

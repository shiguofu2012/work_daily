#!/usr/bin/python
import time


def consumer():
    n = 0
    while True:
        n = yield (n + 1)
        print 'consumer: %d' % n
        time.sleep(1)


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        r = c.send(n)
        print 'producing %s' % r
if __name__ == '__main__':
    c = consumer()
    producer(c)

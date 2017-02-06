#!/usr/bin/python
import time


def consumer1():
    a = 0
    while True:
        time.sleep(3)
        t = yield a
        if isinstance(t, tuple):
            for i in range(t[1]):
                a += i + t[0]


def producer(c):
    c.send(None)
    t = (1, 50)
    r = c.send(t)
    print r
    t = (51, 50)
    r = c.send(t)
    print r

if __name__ == '__main__':
    c = consumer1()
    producer(c)

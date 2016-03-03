#!/usr/bin/python


def gen():
    a = 1
    while True:
        if a % 3 == 0:
            a = yield a
        a += 1


if __name__ == '__main__':
    g = gen()
    g.send(None)
    print g.send(100)

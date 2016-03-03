#!/usr/bin/python


from rq import Queue
from rqwork import conn
from redis import Redis
from task import count_words
import time
l = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.baidu.com/']
q = Queue(connection=Redis())
rs = []
for i in l:
    r = q.enqueue(count_words, i)
    rs.append(r)
print rs
for result in rs:
    print result.status
time.sleep(5)
for result in rs:
    print result.status

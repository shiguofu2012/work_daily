#!/usr/bin/python


from rq import Queue
from rqwork import conn
from redis import Redis
from task import count_words
import time
l = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com']
q = Queue(connection=Redis())
r = []
for i in l:
    r.append(q.enqueue(count_words, i))
time.sleep(10)
for result in r:
    print result.result

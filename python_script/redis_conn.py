#!/usr/bin/env python
# coding=utf-8

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='1q2w3e4r')
r = redis.Redis(connection_pool=redis_pool)
r.set('name1', 'lili')
name1 = r.get('name1')
print(name1)
name = r.hget('student1','name')
print(name)

for item in r.lrange('num1',0,-1):
    print(str(item))


def list_iter(name):
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name, index)

for item in list_iter('num1'):
    print(item)


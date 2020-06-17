#!/usr/bin/env python
# coding=utf-8

import redis

test_login_host = '10.26.14.46'
test_login_port = 10028

redis_pool = redis.ConnectionPool(host=test_login_host, port=test_login_port)
redis_conn = redis.StrictRedis(connection_pool=redis_pool)
pipe = redis_conn.pipeline()
pipe_size = 100

key_len = 0
key_list = []
for key in redis_conn.scan_iter(match='PASSPORT:TGTSCOPE:*', count=1000):
    key_list.append(key)
    print key, pipe.get(key)
    key_len += 1
    #if key_len % pipe_size == 0:
    #    pipe.execute()
    #else:
    #    for (k, v) in zip(key_list, pipe.execute()):
    #        print k, v
#sample_value = redis_conn.get('PASSPORT:TGTSCOPE:web:1000000023109692')

#print("value: "+sample_value)

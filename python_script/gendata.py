#!/usr/bin/env python
# coding: utf-8

from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')
test_data = []
for i in range(randint(5, 10)):
    dtint = randint(0, maxint -1)
    dtstr = ctime(dtint)

    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(lowercase)

    data_line = '%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)
    test_data.append(data_line)

with open(r'd:\test\data.txt', 'a+') as df:
    for line in test_data:
        print data_line,
        df.write(line)

#!/usr/bin/env python
# coding: utf-8
from os import popen
from re import split

f = popen('who', 'r')
for eachLine in f:
    print split(r'\s\s+|\t', eachLine.strip())
f.close()

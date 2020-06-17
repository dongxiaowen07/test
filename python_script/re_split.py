#!/usr/bin/env python
# coding: utf-8

import re

file_path = r'd:\test\data.txt'
pat_str = r'(\d+-\d+-\d+)'
rsl = []
with open(file_path, 'r') as fr:
    for line in fr:
        print line,
        rs = re.search(pat_str, line).group()
        rsl.append(rs)

for item in rsl:
    print item

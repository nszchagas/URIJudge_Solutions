# -*- coding: utf-8 -*-
cases = int(input())

for cont in range(cases):
    lines = int(input())
    sum = 0
    for i in range(lines):
        sum += 2**i
    print(sum)
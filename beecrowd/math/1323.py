# -*- coding: utf-8 -*-

N = 1

while N != 0:
    N = int(input())
    if N > 0:
        cont = 1
        squares = 0
        for cont in range(N+1):
            squares += cont**2
        print(squares)



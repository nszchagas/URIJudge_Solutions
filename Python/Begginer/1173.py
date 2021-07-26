# -*- coding: utf-8 -*-
valor = int(input())
N = [None]*10
for i in range(10):
    N[i] = valor*2**i
    print(f'N[{i}] = {N[i]}')

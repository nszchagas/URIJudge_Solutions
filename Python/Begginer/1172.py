# -*- coding: utf-8 -*-
vetor = [0]*10
for i in range(10):
    entrada = int(input())
    if entrada > 0:
        vetor[i] = entrada
    else:
        vetor[i] = 1
for i in range(10):
    print(f"X[{i}] = {vetor[i]}")

# -*- coding: utf-8 -*-

n = 0
cont = 1
while n != -1:
    n = int(input())
    if (n!=-1):
        print(f"Experiment {cont}: {n//2} full cycle(s)")
        cont+=1
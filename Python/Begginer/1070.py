# -*- coding: utf-8 -*-
num = int(input())

if (num % 2 == 0):
    impar = num+1
else:
    impar = num

for i in range(6):
    print(impar)
    impar += 2
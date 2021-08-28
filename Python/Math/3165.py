# -*- coding: utf-8 -*-

def isPrimo(num):
    cont = 2
    while cont**2 <= num:
        if num % cont == 0: 
            return False
        cont+=1

    return True

def getPrimosProx(n):
    primos = []
    while len(primos) != 2:
        if isPrimo(n):
            primos.append(n)
        n -=1
    return primos

n = int(input())
primos = getPrimosProx(n)
while primos[0]-primos[1] != 2:
    primos = getPrimosProx(primos[1])
print(f"{primos[1]} {primos[0]}")





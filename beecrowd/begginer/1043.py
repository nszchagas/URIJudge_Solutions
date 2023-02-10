# -*- coding: utf-8 -*-

lados = input().strip().split(' ')

for i in range(len(lados)):
    lados[i] = float(lados[i])

def isTriangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)

if isTriangle(*lados):
    print(f"Perimetro = {lados[0]+lados[1]+lados[2]:.1f}")
else:
    print(f"Area = {(lados[0]+lados[1])*lados[2]/2 :.1f}")


    
    




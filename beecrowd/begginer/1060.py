# -*- coding: utf-8 -*-

valores = []
positivos = 0 

while (len(valores) < 6):
    valor = float(input())
    if valor != 0:
        valores.append(valor)
        if valor > 0:
            positivos += 1
    else:
        continue


print(f'{positivos} valores positivos')
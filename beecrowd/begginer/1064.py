# -*- coding: utf-8 -*-

valores = []
positivos = 0 
media = 0

while (len(valores) < 6):
    valor = float(input())
    if valor != 0:
        if (valor > 0):
            media += valor
            positivos += 1
        valores.append(valor)
    else:
        continue

print(f'{positivos} valores positivos')
print(f"{media/positivos:.1f}")
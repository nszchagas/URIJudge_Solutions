# -*- coding: utf-8 -*-

valores = []
pares = 0
positivos = 0
negativos = 0

while (len(valores) < 5):
    entrada = int(input())
    valores.append(entrada)
    if entrada % 2 == 0:
        pares += 1
    if entrada > 0:
        positivos += 1
    elif entrada < 0:
        negativos += 1

print(f'{pares} valor(es) par(es)')
print(f'{len(valores) - pares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
# -*- coding: utf-8 -*-
idades = []
entrada = int(input())
media = 0
quantidade = 0
while entrada >= 0:
    media += entrada
    quantidade += 1
    entrada = int(input())
if (quantidade > 0):    
  print(f'{media/quantidade:.2f}')
else:
  print(f'{media:.2f}')

# -*- coding: utf-8 -*-

cod, qtd = input().split(' ') 

qtd = int(qtd)
preco = 0

if cod == '1': 
    preco = 4.0
elif cod == '2':
    preco = 4.5
elif cod == '3':
    preco = 5.0
elif cod == '4':
    preco = 2.0
elif cod == '5':
    preco = 1.5
    
print(f"Total: R$ {preco*qtd}")
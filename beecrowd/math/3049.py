# -*- coding: utf-8 -*-

tamanho_nota = (160, 70) #(base, altura)
corte = [] #(B, T) = corte na base e no topo
corte.append(int(input()))
corte.append(int(input()))
Area_T = tamanho_nota[0]*tamanho_nota[1]
Area_F = (corte[0]+corte[1])*tamanho_nota[1]/2 # área do trapézio

if Area_F / Area_T > 0.5:
    print(1)
elif Area_F / Area_T < 0.5:
    print(2)
elif Area_F / Area_T == 0.5:
    print(0)
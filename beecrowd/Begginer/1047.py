# -*- coding: utf-8 -*-

horasI, minutosI, horasF, minutosF = input().split(' ')

horasI = int(horasI)
minutosI = int(minutosI)
horasF = int(horasF)
minutosF = int(minutosF)

duracao_min = 0
duracao_horas = 0

if minutosF >= minutosI:
    duracao_min = minutosF - minutosI
else:
    horasF = horasF - 1
    minutosF = 60 + minutosF
    duracao_min = minutosF - minutosI
if horasF > horasI:
    duracao_horas = horasF - horasI
elif horasF < horasI:
    duracao_horas = 24 + horasF - horasI
elif horasF == horasI:
    if duracao_min == 0:
        duracao_horas = 24
    else:
        duracao_horas = 0
        
        

    
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_min} MINUTO(S)")


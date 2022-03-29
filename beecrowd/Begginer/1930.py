#uma das réguas é ligada na tomada
#as outras 3 réguas são ligadas nas outras
#expressão: total de tomadas - 3 espaços para ligar as outras réguas

t1, t2, t3, t4 = input().split(' ')
t1 = int(t1)
t2 = int(t2)
t3 = int(t3)
t4 = int(t4)

print(t1+t2+t3+t4-3)
entrada = ' '
while entrada != 'sair':
    entrada = input("Nome do arquivo:")
    if entrada == 'sair':
        break
    with open (f'{entrada}.py', 'w') as f: 
        f.write('# -*- coding: utf-8 -*-')

salario = float(input())

if(salario >= 0 and salario <= 400):
    perc = 15
elif(salario > 400 and salario <= 800):
    perc = 12
elif(salario > 800 and salario <= 1200):
    perc = 10
elif(salario > 1200 and salario <= 2000):
    perc = 7
elif(salario > 2000):
    perc = 4

print(f"Novo salario: {salario*(1+perc/100):.2f}")
print(f"Reajuste ganho: {salario*perc/100:.2f}")
print(f"Em percentual: {perc} %")

valor = int(input())

qtd100 = valor // 100
qtd50 = (valor % 100) // 50
qtd20 = ((valor % 100) % 50) // 20
qtd10 = (((valor % 100) % 50) % 20) // 10
qtd5 = ((((valor % 100) % 50) % 20) % 10) // 5
qtd2 = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
qtd1 = (((((valor % 100) % 50) % 20) % 10) % 5) % 2

print(f"{valor}")
print(f"{qtd100} nota(s) de R$ 100,00")
print(f"{qtd50} nota(s) de R$ 50,00")
print(f"{qtd20} nota(s) de R$ 20,00")
print(f"{qtd10} nota(s) de R$ 10,00")
print(f"{qtd5} nota(s) de R$ 5,00")
print(f"{qtd2} nota(s) de R$ 2,00")
print(f"{qtd1} nota(s) de R$ 1,00")

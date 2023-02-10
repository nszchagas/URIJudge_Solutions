valor_inteiro, valor_centavos = input().split('.')
valor_inteiro = int(valor_inteiro)
valor_centavos = int(valor_centavos)

qtd100 = valor_inteiro // 100
qtd50 = (valor_inteiro % 100) // 50
qtd20 = ((valor_inteiro % 100) % 50) // 20
qtd10 = (((valor_inteiro % 100) % 50) % 20) // 10
qtd5 = ((((valor_inteiro % 100) % 50) % 20) % 10) // 5
qtd2 = (((((valor_inteiro % 100) % 50) % 20) % 10) % 5) // 2
qtd1 = (((((valor_inteiro % 100) % 50) % 20) % 10) % 5) % 2 

qtd50cents = valor_centavos // 50
qtd25cents = (valor_centavos % 50) // 25
qtd10cents = ((valor_centavos % 50) % 25 ) // 10
qtd5cents = (((valor_centavos % 50) % 25 ) % 10 ) // 5
qtd1cent = ((((valor_centavos % 50) % 25 ) % 10 ) % 5)

print("NOTAS:")
print(f"{qtd100} nota(s) de R$ 100.00")
print(f"{qtd50} nota(s) de R$ 50.00")
print(f"{qtd20} nota(s) de R$ 20.00")
print(f"{qtd10} nota(s) de R$ 10.00")
print(f"{qtd5} nota(s) de R$ 5.00")
print(f"{qtd2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{qtd1} moeda(s) de R$ 1.00")
print(f"{qtd50cents} moeda(s) de R$ 0.50")
print(f"{qtd25cents} moeda(s) de R$ 0.25")
print(f"{qtd10cents} moeda(s) de R$ 0.10")
print(f"{qtd5cents} moeda(s) de R$ 0.05")
print(f"{qtd1cent} moeda(s) de R$ 0.01")


# Programa para descompoñer unha cantidade en billetes e moedas

total = int(input("Introduce a cantidade en euros:"))

billetes_100 = total // 100
resto = total % 100

billetes_20 = resto // 20
resto = resto % 20

billetes_5 = resto // 5
resto = resto % 5

moedas_1 = resto

print("O desglose é o seguinte:")
print("Billetes de 100€:", billetes_100)
print("Billetes de 20€:", billetes_20)
print("Billetes de 5€:", billetes_5)
print("Moedas de 1€:", moedas_1)
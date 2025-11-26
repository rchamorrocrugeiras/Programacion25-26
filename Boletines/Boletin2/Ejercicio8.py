# Programa para calcular o total en euros a partir de billetes e moedas

billetes_100 = int(input("Introduce o número de billetes de 100€: "))
billetes_20 = int(input("Introduce o número de billetes de 20€: "))
billetes_5 = int(input("Introduce o número de billetes de 5€: "))
moedas_1 = int(input("Introduce o número de moedas de 1€: "))

total = billetes_100 * 100 + billetes_20 * 20 + billetes_5 * 5 + moedas_1 * 1

print("O total en euros é:", total, "€")
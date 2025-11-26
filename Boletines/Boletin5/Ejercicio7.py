# Programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.

for n in range(7):
    for m in range(n, 7):
        print("A ficha é:", n, '|', m)

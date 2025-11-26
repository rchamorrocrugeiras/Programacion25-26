# Programa que tome una cantidad y calcule el factorial e o imprima en pantalla

import math

n = int(input("Cantos números queres ingresar?: "))

for i in range(1, n + 1):
    n = int(input(f"Introduce o número {i}: "))
    print(i, "-", math.factorial(n))

# Programa que pregunta por los números ganadores de la loteria primitiva,
# los almacene en una lista y los muestre de menor a mayor

numeros_ganadores_loteria = []

for i in range(5): # Añadimos 5 números de loteria
    numero = int(input("Número ganador de la primitiva?: "))
    numeros_ganadores_loteria.append(numero)

numeros_ganadores_loteria.sort()

print("Los numeros ganadores ordenados de menor a mayor son: ")
print(numeros_ganadores_loteria)
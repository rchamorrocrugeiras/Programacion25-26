# Calcular a cantidade de números negativos, positivos e ceros que hau nun grupo de 10 números enteiros

print("Introduce un intervalo de 10 números enteiros")
numeros = []

for i in range(10):
    numero = int(input(f"Número {i+1}: "))
    numeros.append(numero)

def contar_numeros(lista):
    positivos = 0
    negativos = 0
    ceros = 0

    for numero in lista:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1

    return positivos, negativos, ceros

positivos, negativos, ceros = contar_numeros(numeros)

print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Ceros:", ceros)
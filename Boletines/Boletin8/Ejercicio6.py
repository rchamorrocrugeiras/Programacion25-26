# Programa que dada una lista de numeros enteros tenemos que escribir una función que:
# Devuelva una lista con todos los que sean primos.
# Devuelva el sumatorio y el promedio de los valores.
# Devuelva una lista con el factorial de cada uno de esos números.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def analizar_lista(lista_numeros):
    primos = [num for num in lista_numeros if es_primo(num)]
    
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros) if lista_numeros else 0
    
    factoriales = [factorial(num) for num in lista_numeros]
    
    return primos, suma, promedio, factoriales

numeros = [2, 3, 4, 5, 6, 7]
primos, suma, promedio, factoriales = analizar_lista(numeros)

print("Números primos:", primos)
print("Suma:", suma)
print("Promedio:", promedio)
print("Factoriales:", factoriales)
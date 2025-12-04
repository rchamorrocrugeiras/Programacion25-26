# Programa que dada una lista de números enteiros e un enteiro k, escribir una función que:
# Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
# Devuelva una lista con aquellos que son múltiplos de k.

def clasificar_por_k(lista, k):
    menores = []
    iguales = []
    mayores = []
    multiplos = []

    for num in lista:
        if num < k:
            menores.append(num)
        elif num > k:
            mayores.append(num)
        else:
            iguales.append(num)

        if k != 0 and num % k == 0:
            multiplos.append(num)

    return menores, iguales, mayores, multiplos


lista_numeros = [3, 7, 10, 2, 15, 9, 5, 20]
k = 5

menores, iguales, mayores, multiplos = clasificar_por_k(lista_numeros, k)

print("Menores que k:", menores)
print("Iguales a k:", iguales)
print("Mayores que k:", mayores)
print("Múltiplos de k:", multiplos)

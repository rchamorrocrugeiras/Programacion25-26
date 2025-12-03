# Programa en el que tenemos que escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor.

def esta_ordenada(tupla):
    for i in range(len(tupla) - 1):
        if tupla[i] > tupla[i + 1]:
            return False
    return True


tupla1 = (1, 2, 3, 4, 5)
tupla2 = (1, 3, 2, 4, 5)

print(f"Está ordenada de menor a mayor la tupla1?: {esta_ordenada(tupla1)}")
print(f"Está ordenada de menor a mayor la tupla2?: {esta_ordenada(tupla2)}")
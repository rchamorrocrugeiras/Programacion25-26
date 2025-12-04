# Programa en el que tenemos que escribir una función empaquetar para una lista, donde empaquetar significa indicar la repetición 
# de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por ejemplo, 
# empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].

def empaquetar(lista):
    if not lista:  
        return []

    resultado = []
    actual = lista[0]
    contador = 1

    for elemento in lista[1:]:
        if elemento == actual:
            contador += 1
        else:
            resultado.append((actual, contador))
            actual = elemento
            contador = 1

    resultado.append((actual, contador))

    return resultado


valores = [1, 1, 1, 3, 5, 1, 1, 3, 3]
print(empaquetar(valores))
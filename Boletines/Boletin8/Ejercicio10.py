# Programa de matrices en el cual tenemos que:
# Escribir una función que reciba dos matrices y devuelva la suma.
# Escribir una función que reciba dos matrices y devuelva el producto.


def sumar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Las matrices no tienen el mismo tamaño"

    resultado = []

    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)

    return resultado


def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        return "No se pueden multiplicar: columnas(A) ≠ filas(B)"

    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])

    resultado = [[0] * columnas_B for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

C = [
    [1, 0],
    [0, 1],
    [2, 1]
]

print("Suma A + B:")
print(sumar_matrices(A, B))

print("\nProducto A · C:")
print(multiplicar_matrices(A, C))

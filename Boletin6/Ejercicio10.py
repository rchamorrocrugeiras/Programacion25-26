# Programa que almacene matrices en una lista y muestre por pantalla su producto

a = [
    (1, 2, 3),
    (4, 5, 6)
]
b = [
    (-1, 0),
    (0, 1),
    (1, 1)
]

filas_a = len(a)
columnas_a = len(a[0])
filas_b = len(b)
columnas_b = len(b[0])

resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

for i in range(filas_a):
    for j in range(columnas_b):
        for k in range(columnas_a):  
            resultado[i][j] += a[i][k] * b[k][j]

resultado_tuplas = [tuple(fila) for fila in resultado]

print("O produto das matrices é:")
for fila in resultado_tuplas:
    print(fila)
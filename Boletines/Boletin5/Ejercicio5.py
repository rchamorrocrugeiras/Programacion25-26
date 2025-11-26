# Programa que reciba un número n por parámetro e imprima os primeiros n números triangulares

# usando a ecuación n ∗ (n + 1) / 2
n = int(input("Introduce o número de números triangulares: "))

print("\nÍndice - Número triangular (con fórmula)")
for i in range(1, n + 1):
    triangular = i * (i + 1) // 2
    print(f"{i} - {triangular}")

#sen usar a ecuación n * (n + 1) / 2
n = int(input("Introduce o número de números triangulares: "))

print("Índice - Número triangular (sen fórmula)")
for i in range(1, n + 1):
    triangular = sum(range(1, i + 1))
    print(f"{i} - {triangular}")

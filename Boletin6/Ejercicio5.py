# Programa que almacene el abecedario en una lista y se cree otra lista con las letras
# que ocupen posiciones de múltiplos de 3, luego muestra por pantalla el resultado

abecedario = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", 
    "j", "k", "l", "m", "n", "ñ", "o", "p", "q", 
    "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
multiplos_de_3 = []

for i in range(len(abecedario)):
    if (i + 1) % 3 == 0:
        multiplos_de_3.append(abecedario[i])

print(f"As letras que están en posición de múltiplo de 3 son: {multiplos_de_3}")
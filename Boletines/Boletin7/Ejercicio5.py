# Programa que cuenta las vocales y las consonantes del String "Python Python Python"

texto = "Python Python Python"

texto_limpio = texto.lower()

vocales = "aeiou"
numero_vocales = 0
numero_consonantes = 0

for caracter in texto_limpio:
    if caracter.isalpha():
        if caracter in vocales:
            numero_vocales += 1
        else:
            numero_consonantes += 1

print(f"Vocales: {numero_vocales}")
print(f"Consonantes: {numero_consonantes}")

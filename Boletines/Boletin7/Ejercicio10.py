# Programa que dado un String cuente diferentes tipos de caracteres, en particular el número de letras, dígitos y espacios

def contar_tipos(texto):
    letras = 0
    digitos = 0
    espazos = 0

    for caracter in texto:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            digitos += 1
        elif caracter.isspace():
            espazos += 1

    print(f"Texto analizado: {texto}")
    print(f"Número de letras: {letras}")
    print(f"Número de dígitos: {digitos}")
    print(f"Número de espacios en blanco: {espazos}")


texto = "Ola, son alumno de DAM1, e son programador desde o 2025"

contar_tipos(texto)
# Programa en el que tenemos que escribir una función que permita validar una contraseña, recibiendo la contraseña como parámetro.
# La contraseña tiene que cumplir las condiciones de mínimo 8 caracteres, al menos una mayúscula, una minúscula y un número.
# La función tiene que retornar un booleano especificando si se valida o no.

contraseña = input("Introduce la contraseña: ")

def validar_contraseña(contraseña):
    mayúsculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    minúsculas = "abcdefghijklmnñopqrstuvwxyz"
    números = "0123456789"

    tiene_mayus = False
    tiene_minus = False
    tiene_num   = False

    if len(contraseña) < 8:
        return False

    for caracter in contraseña:
        if caracter in mayúsculas:
            tiene_mayus = True
        elif caracter in minúsculas:
            tiene_minus = True
        elif caracter in números:
            tiene_num = True

    print(f"Tiene mayúsculas?: {tiene_mayus}")
    print(f"Tiene minúsculas?: {tiene_minus}")
    print(f"Tiene números?: {tiene_num}")


print(validar_contraseña(contraseña))
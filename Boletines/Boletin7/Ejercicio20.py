# Programa en el que tenemos que escribir funciones que hagan lo siguiente:
# 1. Recibiendo una cadena de caracteres y un caracter, retorne una nueva cadena formada exclusivamente por el nuevo caracter. 
# Esta nueva cadena tendrá la longitud de la cadena pasada por parámetro.
# 2. Recibiendo una cadena de caracteres y un caracter, la función tendrá que comprobar si el caracter está en la cadena. 
# La función retornará un String en el que aparezcan guiones y el caracter en la posición o posiciones donde coincida en la cadena.


def repetir_caracter(cadena, caracter):
    nova_cadea = caracter * len(cadena)
    return nova_cadea


def marcar_caracter(cadena, caracter):
    resultado = ""
    for c in cadena:
        if c == caracter:
            resultado += c
        else:
            resultado += "-"
    return resultado


cadena1 = "Python"
caracter1 = "*"

cadena2 = "banana"
caracter2 = "a"

print("Resultado función 1:", repetir_caracter(cadena1, caracter1)) 
print("Resultado función 2:", marcar_caracter(cadena2, caracter2))  
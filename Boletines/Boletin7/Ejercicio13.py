# Programa que modificando las funciones anteriores para que reciban un parámetro 
# que indique la cantidad máxima de reemplazos o inserciones a realizar

cadena_reemplazar_espacios = "mi archivo de texto.txt"
cadena_insertar_caracter = "separar"
cadena_reemplazar_dígitos = "su clave es: 1540"
cadena_insertar_cada_3_dígitos = "2552552550"

def reemplazar_espacios(texto, máximo_de_reemplazos=5):
    texto_reemplazado = ""
    contador = 0
    for caracter in texto:
        if caracter == " " and (máximo_de_reemplazos == 10 or contador < máximo_de_reemplazos):
            texto_reemplazado += "\_"
            contador += 1
        else:
            texto_reemplazado += caracter
    print(f"Reemplazando los espacios: {texto_reemplazado}")

def insertar_caracter(texto, máximo_de_reemplazos=3):
    texto_insertado = ""
    operaciones = 0
    for i in range(len(texto)):
        texto_insertado += texto[i]
        if i != len(texto) - 1:
            if máximo_de_reemplazos == 3 or operaciones < máximo_de_reemplazos:
                texto_insertado += ","
                operaciones += 1
            else:
                pass
    print(f"Insertando entre cada caracter: {texto_insertado}")

def reemplazar_dígitos(texto, máximo_de_reemplazos=3):
    texto_reemplazado = ""
    digitos = "0123456789"
    contador = 0
    for caracter in texto:
        if caracter in digitos and (máximo_de_reemplazos == 3 or contador < máximo_de_reemplazos):
            texto_reemplazado += "X"
            contador += 1
        else:
            texto_reemplazado += caracter
    print(f"Reemplazando dígitos: {texto_reemplazado}")

def insertar_cada_3_dígitos(texto, máximo_de_reemplazos=3):
    texto_insertado = ""
    contador_digitos = 0
    operaciones = 0
    for caracter in texto:
        if caracter.isdigit():
            if contador_digitos > 0 and contador_digitos % 3 == 0 and (máximo_de_reemplazos == 3 or operaciones < máximo_de_reemplazos):
                texto_insertado += "."
                operaciones += 1
            texto_insertado += caracter
            contador_digitos += 1
        else:
            texto_insertado += caracter
            contador_digitos = 0
    print(texto_insertado)


reemplazar_espacios(cadena_reemplazar_espacios)
insertar_caracter(cadena_insertar_caracter)
reemplazar_dígitos(cadena_reemplazar_dígitos)
insertar_cada_3_dígitos(cadena_insertar_cada_3_dígitos)
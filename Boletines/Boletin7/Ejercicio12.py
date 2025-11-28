# Programa en el que tenemos que escribir funciones que dada una cadena y un caracter:
# Reemplace todo slos espacios por el caracter. Ej: "mi archivo de texto.txt" e "\_" debería devolver "mi\_archivo\_de\_texto.txt"
# Inserte el caracter entre cada letra de la cadena. Ej: "separar" y "," debería devolver "s,e,p,a,r,a,r"
# Reemplace todos los dígitos en la cadena por el caracter. Ej: "su clave es: 1540" y "X" debería devolver "su clave es: XXXX"
# Inserte el caracter cada 3 dígitos en la cadena. Ej. "2552552550" y "." debería devolver "255.255.255.0"

cadena_reemplazar_espacios = "mi archivo de texto.txt"
cadena_insertar_caracter = "separar"
cadena_reemplazar_dígitos = "su clave es: 1540"
cadena_insertar_cada_3_dígitos = "2552552550"

def reemplazar_espacios(texto):
    texto_reemplazado = texto.replace(" ", "\_")
    print(f"Reemplazando los espacios: {texto_reemplazado}")

def insertar_caracter(texto):
    texto_insertado = ""
    for i in range(len(texto)):
        texto_insertado += texto[i]
        if i != len(texto) -1:
            texto_insertado += ","
    print(f"Insertando entre cada caracter: {texto_insertado}")

def reemplazar_dígitos(texto):
    texto_reemplazado = ""
    digitos = "0123456789"
    for caracter in texto:
        if caracter in digitos:
            texto_reemplazado += "X"
        else:
            texto_reemplazado += caracter
    print(f"Reemplazando dígitos: {texto_reemplazado}")

def insertar_cada_3_dígitos(texto):
    texto_insertado = ""
    contador = 0
    for caracter in texto:
        if caracter.isdigit():
            if contador > 0 and contador % 3 == 0:
                texto_insertado += "."
            texto_insertado += caracter
            contador += 1
        else:
            texto_insertado += caracter 
            contador = 0
    print(texto_insertado)


reemplazar_espacios(cadena_reemplazar_espacios)
insertar_caracter(cadena_insertar_caracter)
reemplazar_dígitos(cadena_reemplazar_dígitos)
insertar_cada_3_dígitos(cadena_insertar_cada_3_dígitos)
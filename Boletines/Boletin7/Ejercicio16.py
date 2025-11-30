# Programa en el que tenemos que escribir una función que dada una xadena de caracteres
# Devuelva solamente las letras consonantes. Por ejemplo, se recibe "algoritmos" ou "logaritmos" debe devolver "lgrtms". 	 	
# Devuelva solamente las letras vocales. Por ejemplo, se recibe "sin consonantes" debe devoltar "i ooae". 	
# Sustituya cada vocal por su siguinte vocal. Por ejemplo, se recibe "vestiario" debe devolver "vistoerou". 

consonantes = "bcdfghjklmnñpqrstvwxyz"
vocales = "aeiou"

cadena_devolver_consonantes = "algoritmos"
cadena_devolver_vocales = "sin consonantes"
cadena_sustituir_vocales = "vestiario"


def devolver_consonantes (texto):
    texto_consonantes = ""
    for caracter in texto.lower():
        if caracter in consonantes:
            texto_consonantes += caracter
    print(texto_consonantes)


def devolver_vocales(texto):
    texto_vocales = ""
    for caracter in texto.lower():
        if caracter in vocales:
            texto_vocales += caracter
    print(texto_vocales)


def sustituir_vocales(texto):
    texto_sustituir_vocales = ""
    for caracter in texto.lower():
        if caracter in vocales:
            posicion = vocales.index(caracter)
            nueva_vocal = vocales[(posicion + 1) % len(vocales)]
            texto_sustituir_vocales += nueva_vocal
        else:
            texto_sustituir_vocales += caracter
    print(texto_sustituir_vocales)


devolver_consonantes(cadena_devolver_consonantes) 
devolver_vocales(cadena_devolver_vocales)
sustituir_vocales(cadena_sustituir_vocales)
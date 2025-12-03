# Programa en el que tenemos que crear una función que permita realizar un analisis simple de texto.
# El analizador tiene la función de contar palabras, caracteres y encontrar la palabra más larga.
# Mostrar los resultados por pantalla

def analisis_texto(texto):
    numero_caracteres = len(texto)


    palabras = texto.split()
    numero_palabras = len(palabras)


    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    
    print("Número de caracteres:", numero_caracteres)
    print("Número de palabras:", numero_palabras)
    print("Palabra más larga:", palabra)

texto_usuario = input("Introduce un texto: ")
analisis_texto(texto_usuario)
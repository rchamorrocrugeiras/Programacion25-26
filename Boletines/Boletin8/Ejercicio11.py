# Programa en el que tenemos que escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas 
# de como máximo esa longitud. Las líneas deben cortarse correctamente en los espacios (sin cortar las palabras)

def dividir_texto(texto, longitud_max):
    palabras = texto.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if len(linea_actual) + len(palabra) + (1 if linea_actual else 0) > longitud_max:
            lineas.append(linea_actual)
            linea_actual = palabra
        else:
            if linea_actual:
                linea_actual += " "
            linea_actual += palabra

    if linea_actual:
        lineas.append(linea_actual)

    return lineas


texto = "Este es un ejemplo de cómo dividir un texto en líneas sin cortar las palabras."
longitud_max = 20

resultado = dividir_texto(texto, longitud_max)

for i, linea in enumerate(resultado, 1):
    print(f"Línea {i}: {linea}")
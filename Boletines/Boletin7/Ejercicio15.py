# Programa en el que tenemos que escribir una función que dada una cadena de caracteres devuelva:
# La primera letra de cada palabra. Por ejemplo, si recibe "Universal Serial Bus" debe devolver "USB". 	
# Una cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe "república arxentina" debe devolver "República Argentina". 		
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe "Antes de abrir" debe devolver "Antes abrir".

cadena_obtener_iniciales = "Universal Serial Bus"

def obtener_iniciales(texto):
    texto_iniciales = ""
    primera_letra = True
    
    for caracter in texto:
        if caracter != " " and primera_letra:
            texto_iniciales += caracter.upper()
            primera_letra = False
        elif caracter == " ":
            primera_letra = True
    
    print(f"Las iniciales del texto son: {texto_iniciales}")


obtener_iniciales(cadena_obtener_iniciales)
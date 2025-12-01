# Programa en el que tenemos que escribir funciones que dadas dos cadenas de caracteres
# Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, "cadena" é unha subcadena de "subcadena". 	 	
# Devuelva a que sea anterior en orden alfábetico. Por ejemplo, si recibe "kde" e "gnome" debe devoltar "gnome".

def es_subcadena(texto, sub):
    if sub in texto:
        return True
    else:
        return False


def anterior_alfabetica(cadena1, cadena2):
    if cadena1 < cadena2:
        return cadena1
    else:
        return cadena2


texto1 = "subcadena"
texto2 = "cadena"

print("¿Es subcadena?:", es_subcadena(texto1, texto2))

cadena_a = "kde"
cadena_b = "gnome"

print("Anterior alfabéticamente:", anterior_alfabetica(cadena_a, cadena_b))
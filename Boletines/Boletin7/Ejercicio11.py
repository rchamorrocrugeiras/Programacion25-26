# Programa en el que tenemos que escribir funciones que dada una cadena de caracteres:
# Imprima los dos primeros caracteres. 	
# Imprima los tres últimos caracteres. 	
# Imprima dicha cadena cada dos caracteres. Ex: recta debería imprimir rca 	 	
# Imprima la cadena en un sentido e en sentido inverso. Ex: reflejo imprime reflejoojelfer.

cadena = "reflejo"


def dos_primeros(texto):
    print("Dos primeros caracteres:", texto[:2])

def tres_ultimos(texto):
    print("Tres últimos caracteres:", texto[-3:])

def cada_dos_caracteres(texto):
    print("Cada dos caracteres:", texto[::2])

def sentido_e_inverso(texto):
    texto_inverso = texto[::-1]
    print("Cadena en sentido e inverso:", texto + texto_inverso)


dos_primeros(cadena)
tres_ultimos(cadena)
cada_dos_caracteres(cadena)
sentido_e_inverso(cadena)
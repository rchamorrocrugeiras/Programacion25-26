# Programa en el que tenemos que escribir una función que permita formatear de nombres.
# La función tiene que eliminar los espacios en blanco y poner en mayúsculas el primer caracter del nombre y apellido pasado como parámetro
# Finalmente retornará una cadena con el nombre y apellidos con el formato solicitado.

nombre = input("Introduce el nombre: ")
apellido = input("Introduce el apellido ")

def formatear_nombre (nombre, apellido):
    nombre_limpio = nombre.replace(" ", "")
    apellido_limpio = apellido.replace(" ", "")

    nombre_limpio = nombre_limpio[0].upper() + nombre_limpio[1:].lower()
    apellido_limpio = apellido_limpio[0].upper() + apellido_limpio[1:].lower()
    
    print(nombre_limpio + apellido_limpio)

formatear_nombre(nombre, apellido)
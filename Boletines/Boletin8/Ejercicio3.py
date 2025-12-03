# Programa en el que tenemos que escribir una función que reciba una tupla con nombres 
# Y para cada nombre imprima un mensaje "Estimado don/doña Nombre"

def mensaje(texto):
    for nombre in texto:
        print("Estimado don/dona", nombre)
    return texto

texto = ("Manuel", "Sergio", "Alex", "Pedro", "Pablo")

mensaje(texto)
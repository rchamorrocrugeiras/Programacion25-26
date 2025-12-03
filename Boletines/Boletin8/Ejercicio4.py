# Programa en el que tenemos que escribir una función que reciba una tupla con nombres, una posición de origen p
# y una cantidad n, e imprima el mensaje anterior (ejercicio3) para los n nombres que se encuentran a partires de la posición p.

def mensaje_parcial(tupla_nombres, p, n):
    sub_nombres = tupla_nombres[p:p+n]
    
    for nombre in sub_nombres:
        print("Estimado don/doña", nombre)


texto = ("Manuel", "Sergio", "Alex", "Pedro", "Pablo")

mensaje_parcial(texto, 1, 3)
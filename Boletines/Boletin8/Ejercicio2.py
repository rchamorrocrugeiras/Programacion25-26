# Programa en el que tenemos que escribir una función que indique si dos fichas de dominó encajan.
# Las fichas son recibidas en dos tuplas. Por ejemplo: (3,4) y (5,4)
# La función devuelve un booleano con el resultado del encaje.

def fichas_encajan(ficha1, ficha2):
    return ficha1[0] in ficha2 or ficha1[1] in ficha2


f1 = (3, 4)
f2 = (5, 4)
f3 = (1, 2)

print(fichas_encajan(f1, f2))
print(fichas_encajan(f1, f3))
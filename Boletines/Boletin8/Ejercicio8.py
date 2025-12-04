# Programa en el que tenemos que escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_nombre) 
# y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto y luego el apellido

def formatear_nombres(lista_personas):
    resultado = []
    
    for apellido, nombre, inicial in lista_personas:
        cadena = f"{nombre} {inicial}. {apellido}"
        resultado.append(cadena)
    
    return resultado


personas = [
    ("Chamorro", "René", "R"),
    ("Guimarey", "Manuel", "M"),
    ("Fernández", "Paco", "P"),
]

resultado = formatear_nombres(personas)

for r in resultado:
    print(r)
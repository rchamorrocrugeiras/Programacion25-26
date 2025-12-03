# Programa en el que tenemos que hacer una función que reciba una cadena de unos y ceros
# y devuelva el valor decimal correspondiente

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0

    for dígito in binario[::-1]:
        if dígito == "1":
            decimal += 2 ** potencia
        potencia += 1

    return decimal


cadena = "101101"
resultado = binario_a_decimal(cadena)
print(f"El número decimal correspondiente es: {resultado}")
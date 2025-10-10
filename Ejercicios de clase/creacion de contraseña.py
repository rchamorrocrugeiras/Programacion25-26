import random
def generar_contraseña():
    letras_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minus = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()-_=+[]{};:,.<>?/"

    todos = letras_mayus + letras_minus + numeros + simbolos

    longitud = random.randint(6, 12)

    contraseña = ""
    for _ in range(longitud):
        contraseña += random.choice(todos)

    return contraseña

# Verificamos se funciona
print ("Contraseña generada:", generar_contraseña())

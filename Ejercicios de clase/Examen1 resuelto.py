# 1. 

usuarioContrasinal = [["Manuel", "canMorto"], ["Pepe", "usuaya"]]

def comprobar_usuario(lista_usuario_contrasinal):
    existe_usuario = False
    nome_usuario = input("Cal é o nome de usuario?: ")
    contrasinal = input ("Cal é o contrasinal?: ")
    for usuario_contrasinal in lista_usuario_contrasinal:
        if usuario_contrasinal[0] == nome_usuario:
            if usuario_contrasinal[1] == contrasinal:
                existe_usuario = True

    return existe_usuario

existe = comprobar_usuario(usuarioContrasinal)
if existe:
    print("Usuario validado ")
else:
    print("Usuario ou contrasinal erroneo")


# 2.

def comprobar_caracteres(contrasinal):
    if len(contrasinal) > 8:
        return True
    else:
        return False

if comprobar_caracteres("wefwefewfw"):
    print("Maior que 8")
else:
    print("Menor que 8")


# 3.

def comprobar_maiusculas_contrasinal(contrasinal): # Opción 1
    maiusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for letra in contrasinal:
        for maiuscula in maiusculas:
            if maiuscula == letra:
                return True


def comprobar_maiusculas_contrasinal2(contrasinal): # Opción 2
    maiusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for letra in contrasinal:
        if letra in maiusculas:
            return True


def comprobar_maiusculas_contrasinal3(contrasinal): # Opción 3
    for letra in contrasinal:
        if letra == letra.upper():
            return True


# 3.

def comprobar_numero_contrasinal(contrasinal): # Opción 1
    numeros = "0123456789"
    for numero in contrasinal:
        for existe in numeros:
            if existe == numero:
                return True


def comprobar_numero_contrasinal2(contrasinal): # Opción 2
    for caracter in contrasinal:
        if caracter.isdecimal():
            return True


# 4.

def comprobar_caracteres_especiais(contrasinal):
    caracteres_especiais = "|@#$%&*_"
    for caracter in contrasinal:
        for especial in caracteres_especiais:
            if caracter == especial:
                return True


# 5.

def ver_caracter(contrasinal):
    caracter_especial = "!@#$%&*_."
    valido = False
    for char in contrasinal:
        if char in caracter_especial:
            valido = True

    return valido

t1 = "abcd1"
t2 = "A2!d"
t3 = "#Bcd"
t4 = "a1%&"
print(ver_caracter(t1))
print(ver_caracter(t2))
print(ver_caracter(t3))
print(ver_caracter(t4))


# 6.

def contraseña_valida():
    nom = str(input("Ingresa tu nombre: "))
    cont = str(input("Ingresa tu contraseña: "))
    nome_cont = [nom, cont]
    nome_contrasinal = []
    caracteres = ["!","@","#","$","%","&","*","_","."]
    valido = False
    digit = False
    mayus = False
    carac = False
    while valido == False and cont != "":
        if len(cont) >= 8:
            for char in cont:
                if char.isdigit():
                    digit = True
                elif char in caracteres:
                    carac = True
                elif char == char.upper():
                    mayus = True
            valido = (digit and carac and mayus)
        else:
            print(False)
            print("Contraseña invalida")
            print("Numero:", digit)
            print("Caracteres:", carac)
            print("Mayus:", mayus)
            cont = str(input("Ingresa tu contraseña: "))

    nome_contrasinal.append(nome_cont)
    return True

print(contraseña_valida())
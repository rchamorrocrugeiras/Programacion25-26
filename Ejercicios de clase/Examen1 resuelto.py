# 1. 

usuarioContrasinal = [["Manuel", "canMorto"], ["Pepe", "usuaya"]]

def comprobar_usuario (lista_usuario_contrasinal):
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


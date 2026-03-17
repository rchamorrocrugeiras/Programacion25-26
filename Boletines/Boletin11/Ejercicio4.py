class Cliente():
    with open("clientes.txt","r") as clientes:
        idcount = len(clientes.readlines())

    def __init__(self, nome, telefono):
        self.id = Cliente.idcount
        self.nome = nome
        self.telefono = telefono

        Cliente.idcount += 1

    def __str__(self):
        return f"{self.id},{self.nome},{self.telefono}\n"


while True:
    print('''
    1. Gardar cliente.

    2. Listar clientes.

    0. Saír e gardar.
    ''')

    opcion = input("Ingrese una opción: ")

    if opcion == "0":
        break

    elif opcion == "1":
        cliente = Cliente(input("Nome: "),input("Teléfono: "))
        with open("clientes.txt","a") as f:
            f.write(str(cliente))

    elif opcion == "2":
        with open("clientes.txt","r") as f:
            contido = f.readlines()

            for linea in contido:
                print(linea)
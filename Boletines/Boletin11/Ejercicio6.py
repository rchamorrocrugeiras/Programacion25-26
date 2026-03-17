import json

class Contacto:
    def __init__(self, nome, telefonos, email):
        self.nome = nome

        if isinstance(telefonos, list):
            self.telefonos = telefonos
        else:
            self.telefonos = [telefonos]
        self.email = email

    def to_dict(self):

        return {
            'nome': self.nome,
            'telefonos': self.telefonos,
            'email': self.email
        }


lista_contactos = []
try:
    with open("axenda.json", "r") as ficheiro:
        lista_contactos = json.load(ficheiro)

except (FileNotFoundError, json.JSONDecodeError):
    lista_contactos = []

while True:
    try:
        print("\n--- AXENDA DE CONTACTOS ---")
        print("1. Engadir contacto.")
        print("2. Listar contactos.")
        print("0. Saír e gardar.")

        entrada = input("\nOpción: ")
        if not entrada.isdigit():
            print("Por favor, introduce un número.")
            continue

        opcion = int(entrada)

        if opcion == 0:
            # Gardar toda a lista ao saír
            with open("axenda.json", "w") as ficheiro:
                json.dump(lista_contactos, ficheiro, indent=4)

            print("Datos gardados. Adeus!")
            break

        elif opcion == 1:
            nome = input("Nome: ")
            telefonos = []
            while True:
                tel = input("Teléfono (escribe 'cancel' para rematar): ")
                if tel.lower() != "cancel":
                    if tel.strip():
                        telefonos.append(tel)

                else:
                    break

            email = input("Email: ")

            novo_contacto = Contacto(nome, telefonos, email)
            lista_contactos.append(novo_contacto.to_dict())
            print("Contacto engadido á lista (gárdase ao saír).")

        elif opcion == 2:
            if not lista_contactos:
                print("\nA axenda está baleira.")

            else:
                print("\nLISTA DE CONTACTOS:")
                for c in lista_contactos:
                    tels = ", ".join(c['telefonos'])
                    print(f"Nome: {c['nome']} | Tels: {tels} | Email: {c['email']}")

        else:
            print("Opción inválida.")

    except Exception as error:
        print(f"Ocorreu un erro inesperado: {error}")
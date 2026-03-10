arquivo = "notas.txt"

while True:
    print("1 Engadir nota")
    print("2 Listar notas")
    print("3 Buscar nota")
    print("4 Saír")

    opcion = input("Opción: ")

    if opcion == "1":
        nota = input("Nota: ")
        f = open(arquivo, "a")
        f.write(nota + "\n")
        print("Nota gardada")
        f.close()

    elif opcion == "2":
        try:
            f = open(arquivo, "r")
            for liña in f:
                print(liña.strip())
            f.close()
        except:
            print("Non hai notas")

    elif opcion == "3":
        palabra = input("Palabra: ")
        try:
            f = open(arquivo, "r",)
            for liña in f:
                if palabra.lower() in liña.lower():
                    print(liña.strip())
                else:
                    print("A palabra non se encuentra en esta linea")
            f.close()
        except:
            print("Non hai notas")

    elif opcion == "4":
        break
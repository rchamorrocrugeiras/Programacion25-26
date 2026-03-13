while True:
    print('''Opcións: 
    1. Agregar nova tarefa.
    2. Borrar tarefa.
    3. Modificar tarefa.
    4. Listar tarefas.
    5. Pechar programa.''')

    opcion = input("Opción: ")

    if opcion == "5":
        exit()

    elif opcion == "1":
        nome = {input("Nome de tarefa: ")}
        descricion = {input("Descrición de tarefa: ")}
        data = {input("Data de tarefa (dd-mm-aaaa): ")}
        hora = {input("Hora de tarefa (hh:mm): ")}
        duracion = {input("Duración de tarefa (hh:mm): ")}
        estado = {input("Estado de tarefa (feita/non feita): ")}
        with open("tarefas.dat", "a", encoding="utf-8") as tarefa:
            tarefa.write(f'''{nome},{descricion},{data},{hora},{duracion},{estado}\n''')

    elif opcion == "2":
        with open("tarefas.dat", "a+", encoding="utf-8") as tarefa:
            nome = input("Nome de tarefa a borrar: ")
            with open("tarefas.dat", "r") as f:
                lineas = f.readlines()

            with open("tarefas.dat", "w") as f:
                for linea in lineas:
                    if nome not in linea:
                        f.write(linea)

    elif opcion == "3":
        nome = input("Nome de tarefa: ")
        nome2 = input("Nome novo de tarefa: ")
        with open("tarefas.dat", "r") as f:
            lineas = f.readlines()

        with open("tarefas.dat", "w") as f:
            for linea in lineas:
                linea = linea.replace(nome, nome2)

    elif opcion == "4":
        with open("tarefas.dat", "r", encoding="utf-8") as tarefa:
            for linea in tarefa.readlines():
                print(linea.strip("\n"))
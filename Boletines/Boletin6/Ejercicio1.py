# Generar codigo que almacene asignaturas en una lista y se le pida al usuario la nota de cada una, 
# luego mostrar por pantalla cada asignatura con su nota

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota sacaste en {asignatura}?: "))
    notas.append(nota)

print("Tus notas son:")
for i in range(len(asignaturas)):
    print(f"{asignaturas[i]}: {notas[i]}")
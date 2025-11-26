# Programa que almacene asignaturas en una lista, pregunte al usuario la nota
# y elimine de la lista las asignaturas aprobadas, al final se muestra la lista

asignaturas = ["Matemáticas", "Castellano", "Gallego", "Inglés", "Tecnología"]
suspensas = []

for i in range(len(asignaturas)):
    nota = float(input(f"¿Qué nota sacaste en {asignaturas[i]}?:"))
    if nota < 5:
        suspensas.append(asignaturas[i])

print(f"Tes que repetir: {suspensas}")
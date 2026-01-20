import csv

with open("exemplo.csv", "r") as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow (["Nome", "Edade", "Xénero"])
    writer.writerow (["Pedro", "23", "Home"])
    writer.writerow (["Rosa", "25", "Muller"])

with open("exemplo.csv", "r") as ficheiro:
    ficheiro.write ("Nome" + "," + "Edade" + "," + "Xénero"+ "\n")
    ficheiro.write ("Pedro" + "," + "23" + "," + "Home"+ "\n")
    ficheiro.write ("Rosa" + "," + "25" + "," + "Muller"+ "\n")

with open("exemplo.csv", "r") as ficheiro:
    reader = csv.reader(ficheiro)
    for fila in reader:
        print(fila)
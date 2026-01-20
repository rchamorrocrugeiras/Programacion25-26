import json

# Escritura
datos = {"nome": "Jose", "edad": 30, "xenero": "Home"}
with open ("exemplo.json", "w") as ficheiro:
    json.dump (datos, ficheiro)

# Lectura
with open ("exemplo.json", "r") as ficheiro:
    datoJson = json.load(ficheiro)
    print (datoJson)

    with open("exemplo.csv", "a") as ficheiro:
        writer = csv.writer(ficheiro)
        writer.writeheader(datoJson[0].keys)
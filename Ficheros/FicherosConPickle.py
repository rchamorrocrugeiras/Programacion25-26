import pickle
import datetime

data_hora = (datetime.datetime.now())
data, hora = str(data_hora).split()
print(data, hora)

amd = data.split("-")
hms = hora.split(":")

fecha_hora = {"ano": amd[0],
              "mes": amd[1],
              "dia": amd[2],
              "hora": hms[0],
              "minuto": hms[1],
              "segundo": hms[2]}

with open ("data.dat", "wb") as ficheiro:
    pickle.dump (fecha_hora, ficheiro)

with open ("data.dat", "rb") as ficheiro:
    dic = pickle.load (ficheiro)
    print (dic["hora"])
    print (dic["minuto"])


opcionsUsuario =  { "theme:": "dark",
                    "font-size": 14,
                    "show_line_numbers": True}

with open ("opcions.dat", "wb") as ficheiro:
    pickle.dump (opcionsUsuario, ficheiro)


with open ("opcions.dat", "rb") as ficheiro:
    ops = pickle.load(ficheiro)
    print(ops)
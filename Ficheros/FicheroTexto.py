import datetime
ficheiro = None
try:
    ficheiro = open ('/home/dam/Programacion25-26/Boletines/Boletin2/Ejercicio1.py')
except FileNotFoundError as e:
    print("Erro o abrir o ficheiro" + srt(e))
else:
    for linea in ficheiro:
        print (linea)
finally:
    if ficheiro is not None:
        ficheiro.close()

data_hora = (datetime.datetime.now())
data, hora = str(data_hora).split()

ficheiro = open('saudo.txt', 'a')

ficheiro.write ("Ola, son René\n")
ficheiro.write (data)
ficheiro.write ("\n")
ficheiro.write (hora)
ficheiro.write ("\n")
ficheiro.write ("Remato e pecho o ficheiro\n")
ficheiro.write ("\n")

ficheiro.close

ficheiro = open ("saudo.txt", "r")
lectura = ficheiro.read()
print(lectura)
ficheiro.close()

ficheiro = open ("saudo.txt", "r")
linea = ficheiro.readline()
while linea != "":
    print(linea)
    linea = ficheiro.readline()
ficheiro.close()

ficheiro = open ("saudo.txt", "r")
lectura = ficheiro.readlines()
print(lectura)
ficheiro.close()

with open ("saudo.txt", "r") as ficheiro:
    l= 0
    for linea in ficheiro:
        l += 1
    print (f"O ficheiro ten {l} lineas.")
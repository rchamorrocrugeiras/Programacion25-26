# Programa que mostre todos os números pares que hai entre dous números que se elixen por pantalla

inicio = int(input("Introduce o número de inicio:"))
fin = int(input("Introduce o número do final"))

print ("Números pares entre", inicio, "e", fin, ":")

for numero in range (inicio, fin +1):
    if numero % 2 == 0:
        print (numero, end=" ")
for numero in range (fin, inicio +1):
    if numero % 2 == 0:
        print (numero, end=" ")
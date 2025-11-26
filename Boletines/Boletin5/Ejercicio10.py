# Programa que calcule o área dun rectángulo cuxa base e altura pides por teclado, validando que a basee e a altura sexan positivos

while True:
    base = float(input("Introduce a base do rectángulo:"))
    if base > 0:
        break
    else:
        print("O valor da bas ten que ser positivo")

while True:
    altura = float(input("Introduce a altura do rectángulo:"))
    if altura > 0:
        break
    else:
        print("O valor da altura ten que ser positivo")

area = base * altura
print("O área do rectángulo é:", area,"m²")
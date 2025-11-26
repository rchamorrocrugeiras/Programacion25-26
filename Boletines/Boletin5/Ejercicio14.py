# 14. Codificar o programa que solicite 10 números por consola e calcule a súa suma.
# Si o usuario introduce en calquera momento o número 999, deixa de solicitar máis números e presenta
#  o valor da súma acadada ata ese momento.

suma = 0
for numero in range(10):
    numero = int(input('Ingrese un numero: '))
    if numero == 999:
        break
    suma += numero

print(suma)
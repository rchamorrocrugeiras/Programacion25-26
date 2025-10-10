# Programa que le dous números e calcula suma, resta, produto e cociente

num1 = float(input("Introduce o primeiro número: "))
num2 = float(input("Introduce o segundo número: "))

suma = num1 + num2
resta = num1 - num2
produto = num1 * num2

print("A suma é:", suma)
print("A resta é:", resta)
print("O produto é:", produto)

if num2 != 0:
    cociente = num1 / num2
    print("O cociente é:", "{:.2f}".format(cociente))
else:
    print("O cociente é: Erro, non se pode dividir entre 0")
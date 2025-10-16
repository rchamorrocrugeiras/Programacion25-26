# Programa no que se escriben dous numeros e visualizamos a resta se o primeiro é maior igual ca o segundo, e a suma

num = float(input("Introduce o primeiro número:"))
num2 = float(input("Introduce o segundo número"))

if num >= num2:
    resta = num - num2
    print ("A resta é:", resta)

suma = num + num2
print ("A suma é:", suma)
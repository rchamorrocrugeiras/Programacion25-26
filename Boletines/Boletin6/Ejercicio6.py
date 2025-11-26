# Programa que pida una palabra y muestre por pantalla si es un palíndromo

palabra = input("Escriba una palabra:")

palabra_limpia = palabra.lower()

if palabra_limpia == palabra_limpia[::-1]:
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")
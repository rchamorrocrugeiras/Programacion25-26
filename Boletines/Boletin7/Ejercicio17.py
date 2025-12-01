# Programa que indique si se trata de un palíndromo

palabra = "anita lava la tina"

palabra_limpia = palabra.replace(" ", "")

if palabra_limpia == palabra_limpia[::-1]:
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")
# Programa que pida una palabra y muestre por pantalla las veces que contiene cada vocal

palabra = input("Escribe una palabra:")

palabra_limpia = palabra.lower()

vocales = ["a", "e", "i", "o", "u"]

contadores = {}

for vocal in vocales:
    contadores[vocal] = palabra.count(vocal)

for vocal, contador in contadores.items():
    print(f"La vocal '{vocal}' aparece {contador} veces")
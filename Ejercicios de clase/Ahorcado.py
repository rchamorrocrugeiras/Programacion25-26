import random

palabras = ["python", "ahorcado", "programacion", "juego", "computadora", "teclado", "raton"]

palabra = random.choice(palabras)
letras_adivinadas = []
intentos = 7

print("Benvido ao xogo do Ahorcado!")
print("Adiviña a palabra secreta.")

while intentos > 0:
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"

    print("Palabra:", palabra_mostrada)
    print("Intentos restantes:", intentos)

    if "_" not in palabra_mostrada:
        print("Parabéns! Adiviñaches a palabra:", palabra)
        break

    letra = input("Introduce unha letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Introduce só unha letra válida.")
        continue

    if letra in letras_adivinadas:
        print("Xa probaches esa letra. Tenta outra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra:
        print("Ben! A letra está na palabra.")
    else:
        print("A letra non está na palabra.")
        intentos -= 1

if intentos == 0:
    print("Perdeches! A palabra era:", palabra)

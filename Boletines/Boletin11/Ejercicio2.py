frase = input("Introduce unha frase: ")
frecuencia = {}

frase = frase.lower()

for signo in ".,;:!?¡¿'-_":
    frase = frase.replace(signo, "")

palabras = frase.split()

for p in palabras:
    if p in frecuencia:
        frecuencia[p] += 1
    else:
        frecuencia[p] = 1

for palabra in frecuencia:
    print(palabra, ":", frecuencia[palabra])

with open("resumo_palabras.txt", "w", encoding="utf-8") as f:
    for palabra in frecuencia:
        f.write(palabra + ": " + str(frecuencia[palabra]) + "\n")
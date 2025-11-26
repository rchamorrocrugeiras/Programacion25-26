# Programa que desmenuce el String "Python" mostrándolo por pantalla carácter a carácter

texto = "Python"
palabra = []

for i in range(len(texto)):
    palabra.append(texto[i])
    print(palabra[i])
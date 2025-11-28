# Programa que sobre la cadena de texto "Jeve Jeve Jeve" substituya las vocales 
# dando como resultado "java java java"

texto = "Jeve Jeve Jeve"

texto_limpio = texto.lower()

texto_substituido = texto_limpio.replace("e", "a")

print(texto_substituido)
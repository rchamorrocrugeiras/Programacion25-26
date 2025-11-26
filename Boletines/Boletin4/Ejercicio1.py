# Programa que indica o tipo do articulo coñecendo as suas ventas

articulo = input("Introduce o nome do articulo:")
ventas = float(input("Introduce o número de ventas anuais do articulo:"))

if ventas <= 100:
    tipo = "baixo"
elif ventas <= 500:
    tipo = "medio"
elif ventas <= 1000:
    tipo = "alto"
else:
    tipo = "primeira necesidade"

print ("O artigo", articulo, "é de tipo", tipo)
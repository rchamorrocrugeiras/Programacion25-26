# Otra manera de hacer el ejercicio de RaizCuadrada

numero = float(input("Introduce un número: "))

raiz = numero ** 0.5
raiz_entera = round(raiz)
resto = numero -(raiz_entera ** 2)

print("Número:", numero)
print("Raíz cuadrada aproximada:", raiz)
print("Raíz cuadrada entera más cercana:", raiz_entera)
print("Resto (diferencia con su cuadrado):", resto)
# Programa que calcule la raiz cuadrada más cercana de un número y su resto

def main():
    n = int(input("Escriba un número natural para saber su raíz cuadrada entera y su resto (si lo tiene): "))

    if n < 0:
        print("Error: la raíz cuadrada no está definida para números negativos.")
        return

    raiz_entera = 0
    while (raiz_entera + 1) ** 2 <= n:
        raiz_entera += 1

    cuadrado = raiz_entera ** 2
    resto = n - cuadrado

    if resto == 0:
        print(f"La raíz cuadrada de {n} es exacta: {raiz_entera}")
    else:
        print(f"La raíz entera más cercana de {n} es: {raiz_entera}")
        print(f"El cuadrado de {raiz_entera} es: {cuadrado}")
        print(f"El resto es: {resto}")

if __name__ == "__main__":
    main()

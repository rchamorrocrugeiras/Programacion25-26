# Programa que utilizando un menú de opcións calcule a superficie de distintas figuras

print('''
[1] Superficie de triángulo
[2] Superficie de cuadrado
[3] Superficie del círculo
[4] Salir''')

opcion = (int(input('Elija una opcion: ')))

if opcion == 1:
    lado = (float(input('Lado del triángulo: ')))
    altura = (float(input('Altura del triángulo: ')))
    area_triangulo = (lado * altura)/2
    print('El área del triángulo es: ', area_triangulo)
else:
    if opcion == 2:
        lado_cuadrado = (float(input('Lado del cuadrado: ')))
        area_cuadrado = lado_cuadrado*lado_cuadrado
        print('El área del cuadrado es: ', area_cuadrado)
    else:
        if opcion == 3:
            radio = (float(input('Radio del círculo: ')))
            pi = 3.14
            area_circulo = (pi * (radio**2))
            print('El área del círculo es: ', area_circulo)
        else:
            if opcion == 4:
                print('Hasta otra')
            else:
                if opcion > 4:
                    print('Opción incorrecta')
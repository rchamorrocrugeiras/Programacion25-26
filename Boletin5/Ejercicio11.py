# Programa que pida un número y se enseñe su tabla de multiplicar, el programa seguirá pidiendo números hasta que se le ponga el 0

while True:
    numero = int(input("Introduce un número:"))
    
    if numero == 0:
        print("Programa finalizado.")
        break
    
    print(f"\nTabla de multiplicar del {numero}:")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()

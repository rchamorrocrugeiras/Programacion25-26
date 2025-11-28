# Programa en el que tenemos que escribir una función que reciba una cadena que contiene un número entero largo
# y devuelva una cadena con el número y las separaciones de miles 

cadena = input("Introduce un número entero largo: ")

def separacion_de_miles(numero):
    numero_str = str(numero)
    numero_en_miles = ""
    
    for i in range(len(numero_str)):
        numero_en_miles += numero_str[i]
        
        resto = len(numero_str) - i - 1
        if resto > 0 and resto % 3 == 0:
            numero_en_miles += "."
    
    print(f"El número separado en miles es: {numero_en_miles}")

separacion_de_miles(cadena)
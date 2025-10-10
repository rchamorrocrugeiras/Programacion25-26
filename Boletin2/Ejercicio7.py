# Programa que converte unha temperatura en graos Celsius

celsius = float(input("Introduce a temperatura en graos Celsius:"))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"A temperatura en Fahrenheit é: {fahrenheit:.2f} °F")
print(f"A temperatura en Kelvin é: {kelvin:.2f} K")
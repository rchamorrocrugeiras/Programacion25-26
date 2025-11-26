# Programa que pregunte por una muestra de números, separados por comas,
# los guarde en una lista y muestre por pantalla su media y desviación típica

entrada = input("Introduce una muestra de números separados por comas: ")

numeros = [float(x) for x in entrada.split(",")]

media = sum(numeros) / len(numeros)

desviacion = (sum((x - media) ** 2 for x in numeros) / len(numeros)) ** 0.5

print(f"Lista de números: {numeros}")
print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")
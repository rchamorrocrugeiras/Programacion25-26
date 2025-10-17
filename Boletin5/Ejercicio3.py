# Programa que genera unha táboa dende 0ºF ata 120ºF de 10 en 10

temperatura = 0
t = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)

for i in (t):
    conversion = (9/5 * temperatura) + 32
    temperatura += 10
    print(conversion)
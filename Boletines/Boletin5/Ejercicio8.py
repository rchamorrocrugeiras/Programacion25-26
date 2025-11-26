# Programa que según o anterior xenera fichas dun xogo que pode ter de 0 a n

n = int(input("Introduce o número máximo das fichas: "))

for i in range(n + 1):
    for m in range(i, n + 1):
        print("A ficha é:", i, "|", m)

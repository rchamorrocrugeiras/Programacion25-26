try:
    baixo_stock = []
    with open("produtos.csv","r") as f:
        next(f)
        for linea in f.readlines():
            lineadividida = linea.split(',')
            print(f"{lineadividida[1]}: {int(lineadividida[2]) * int(lineadividida[3])}")
            baixo_stock.append(linea + "\n")

    with open("baixo_stock.csv","w") as f:
        for line in baixo_stock:
            f.write(line)

except FileNotFoundError:
    print("Ficheiro produtos.csv non atopado.")
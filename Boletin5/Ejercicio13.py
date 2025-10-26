# 13 Solicita o usuario un número n e debuxa un triángulo de base e altura n.
#   Si o usuario teclea o número 4 o triángulo sería da seguinte forma

def main():

    num = int(input("Como de alto va a ser la piramide?:"))
    for x in range(1, num+1):
        espacio = " " * (num-x)
        punto = "* " * x
        print(espacio + punto.strip())

if __name__ == "__main__":
    main()
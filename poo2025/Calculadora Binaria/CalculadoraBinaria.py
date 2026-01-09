class CalculadoraBinaria:
    def __init__(self, a, b):
        self.set_a(a)
        self.set_b(b)

# Setters
    def set_a(self, a):
        if isinstance (a, int) or isinstance (a, float) or isinstance (a, complex):
            self.__a = a
        else:
            self.__a = 0

    def set_b(self, b):
        if isinstance (b, int) or isinstance (b, float) or isinstance (b, complex):
            self.__b = b
        else:
            self.__b = 0

# Getters
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b

# Métodos
    def operacion(self, operando):
        if operando == "+":
            return self.__a + self.__b
        elif operando == "-":
            return self.__a - self.__b
        elif operando == "*":
            return self.__a * self.__b
        elif operando == "/":
            return self.__a / self.__b
        else:
            raise ValueError("Operando non válido")


    a = property(get_a, set_a)
    b = property(get_b, set_b)

if __name__ == "__main__":
    c1 = CalculadoraBinaria(2, 3)
    c1.a = 1
    print(c1.operacion("+"))
    c1.set_a(10)
    print(c1.operacion("-"))
    c2 = CalculadoraBinaria(2, 0)
    print(c2.operacion("+"))

    try:
        print(c2.operacion("/"))
    except ZeroDivisionError:
        print("Non se pode dividir por cero")
        b = int(input("Introduce un divisor que non sexa 0:" ))
        while c2.set_b == 0:
            b = int(input("Introduce un divisor que non sexa 0:" ))
        c2.b = b
        print(c2.operacion("/"))
    finally:
        print("Fin do programa")
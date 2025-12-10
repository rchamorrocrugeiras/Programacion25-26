class Bombilla():
    def __init__(self):
        self.__encendida = False


# Métodos
    def enciende(self):
        self.__encendida = True

    def apaga(self):
        self.__encendida = False

    def estado(self):
        return self.__encendida

    def __str__(self):
        return "Encendida" if self.__encendida else "Apagada"


# Pruebas
b1 = Bombilla()

print("Estado inicial:", b1.__str__())

b1.enciende()
print("Estado actual:", b1.__str__())

b1.apaga()
print("Estado actual:", b1.__str__())
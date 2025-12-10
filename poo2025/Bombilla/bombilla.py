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

    def conmuta(self):
        self.__encendida = not self.__encendida

    def __str__(self):
        return "La bombilla está encendida" if self.__encendida else "La bombilla está apagada"


# Pruebas
b1 = Bombilla()
b2 = Bombilla()

print(b1)
print(b2)
b1.enciende()
print(b1)
print(b2)
b1.conmuta()
print(b1)
print(b2)
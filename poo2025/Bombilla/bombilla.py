class Bombilla():
    interruptorGeneral = False

    def __init__(self):
        self.__encendida = False


# Métodos
    def enciende(self):
        self.__encendida = True

    def apaga(self):
        self.__encendida = False

    def conmuta(self):
        self.__encendida = not self.__encendida

    def estado(self):
        return self.__encendida

    def estaEncendida(self):
        return self.__encendida and Bombilla.interruptorGeneral

    def __str__(self):
        return "La bombilla está encendida" if self.__encendida and Bombilla.interruptorGeneral else "La bombilla está apagada"


# Pruebas
b1 = Bombilla()
b2 = Bombilla()

print(b1)
print(b2)
b1.enciende()
Bombilla.interruptorGeneral = True
print(b1)
print(b2)
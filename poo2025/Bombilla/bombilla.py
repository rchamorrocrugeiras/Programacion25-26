class Bombilla():
    def __init__(self, ):
        self.__encendida = False


# Métodos
    def enciende(self):
        self.__encendida = True
        print("La bombilla está encendida.")

    def apaga(self):
        self.__encendida = False
        print("La bombilla está apagada.")

    def estado(self):
        return "Encendida" if self.__encendida else "Apagada"


# Pruebas
bombilla = Bombilla()

print("Estado inicial", bombilla.estado())

bombilla.enciende()
print("Estado actual:", bombilla.estado())

bombilla.apaga()
print("Estado actual:", bombilla.estado())
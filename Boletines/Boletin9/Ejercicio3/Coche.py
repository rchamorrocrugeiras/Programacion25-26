class Coche:
    def __init__(self):
        self.velocidad = 0

# Métodos
    def getVelocidad(self):
        return self.velocidad

    def acelerar(self, valor):
        self.velocidad += valor
        return self.velocidad

    def frenar(self, menos):
        self.velocidad -= menos
        if self.velocidad < 0:
            self.velocidad = 0
        return self.velocidad


class Boletin_9_3:
    def __init__(self):
        mi_coche = Coche()

        print("Velocidad inicial:", mi_coche.getVelocidad())

        print("Velocidad después de acelerar:", mi_coche.acelerar(100))

        print("Velocidad después de frenar:", mi_coche.frenar(30))

Boletin_9_3()
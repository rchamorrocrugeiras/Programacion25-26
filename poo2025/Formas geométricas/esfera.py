from circulo import Circulo

class Esfera(Circulo):
    def __init__(self, x, y, radio):
        super().__init__(x, y, radio)

    def calcularArea(self):
        return 4 * super().calcularArea()

    def calcularVolume(self):
        #volume = 4/3 * math.pi * radio ** 3
        #volume = (4/3) * math.py * self.radio ** 3
        #volume = (self.calcularArea() * self.radio / 3
        volume = (4/3) * super().calcularArea() * self.radio #herencia
        return volume
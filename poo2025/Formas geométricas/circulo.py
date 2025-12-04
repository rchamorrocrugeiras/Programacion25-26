import math

from punto import Punto

class Circulo(Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = abs(radio)

    def obtenerDiametro(self):
        return self.radio * 2

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

    def calcularArea(self):
        return math.pi * (self.radio**2)

    def tostring(self):
        cadea = super().toString() + " \n\t Radio : " + str(self.radio)
        return cadea
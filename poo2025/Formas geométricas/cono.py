import math

from punto import Punto

class Cono(Punto):
    def __init__(self, x, y, radio, altura):
        super().__init__(x, y)
        self.radio = abs(radio)
        self.altura = altura

    def calcularArea(self):
        return math.pi * self.radio * (self.radio + (math.sqrt(self.radio**2 + self.altura**2)))

    def calcularVolument(self):
        return (1/3) * math.pi * (self.radio**2) * self.altura

    def toString(self):
        cadena = super().toString() + "Cono: " + str(self.x) + " " + str(self.y)
        return cadena
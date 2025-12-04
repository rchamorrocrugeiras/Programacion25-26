import math

from punto import Punto

class Cilindro(Punto):
    def __init__(self, x, y, radio, altura):
        super().__init__(x, y)
        self.radio = abs(radio)
        self.altura = altura

    def calcularArea(self):
        return (2*math.pi*self.radio(self.radio+self.altura))

    def calcularVolument(self):
        return (math.pi*(self.radio**2)*self.altura)

    def toString(self):
        cadena = super().toString() + "Cilindro: " + str(self.x) + " " + str(self.y)
        return cadena
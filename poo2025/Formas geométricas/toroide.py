from circulo import Circulo
from punto import Punto
import math

class Toroide(Circulo):
    def __init__(self, x, y, radio, centro):
        super().__init__(x,y,radio)
        self.centroToroX = centro.x
        self.centroToroY = centro.y


    def cacularRadioMaior(self):
        return self.distancia(Punto(self.centroToroX, self.centroToroY))

    def calcularRadioMenor(self):
        return self.distancia (Punto (self.centroToroX, self.centroToroY))

    def calcularArea(self):
        # R = distacia centro circunferencia e centro toroide
        # r = R - radio circunferencia
        radioMaior = self.cacularRadioMaior()
        radioMenor = self.calcularRadioMenor()
        return 4 * math.pi **2 * radioMenor * radioMaior

    def calcularVolume(self):
        return 2 *  math.pi * self.cacularRadioMaior() * self.calcularArea()
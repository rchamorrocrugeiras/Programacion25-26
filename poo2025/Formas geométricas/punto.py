class Punto:
    def __init__(self, x, y):
        self.x = abs(x)
        self.y = abs(y)

    def toString(self):
        cadeaPunto = "As coordenadas do punto son: \n\t x = " + str(self.x) + " \n\t y = " + str(self.y)
        return cadeaPunto

    def __str__(self):
        return self.toString()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
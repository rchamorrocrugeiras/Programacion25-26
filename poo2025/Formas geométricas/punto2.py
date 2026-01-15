class Punto2:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def setX(self, x):
        if type(x) == int or type(x) == float:
            if x >= 0:
                self.__x = x
            else:
                self.__x = 0
        else:
            raise TypeError ("O tipo non é válido")

    def setY(self, y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self.__y = y
            else:
                self.__y = 0
        else:
            raise TypeError ("O tipo non é válido")

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def toString(self):
        cadeaPunto = "As coordenadas do punto son: \n\t x = " + str(self.__x) + " \n\t y = " + str(self.__y)
        return cadeaPunto

    def __str__(self):
        return self.toString()

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    x=property(getX, setX)
    y=property(getY, setY)



class Punto3:
    def __init__(self, x ,y):
        self.setX(x)
        self.setY(y)
    
    def setX (self, x):
        if type(x) == int or type(x) == float:
            if x > 0:
                self.__x = x
            else:
                self.__x = 0
        else: raise TypeError ("O tipo da coordenada x ten que ser int ou float")
    
    def setY (self, y):
        if type(y) == int or type(y) == float:
            if y > 0:
                self.__y = y
            else:
                self.__y = 0
        else: raise TypeError ("O tipo da coordenada x ten que ser int ou float")

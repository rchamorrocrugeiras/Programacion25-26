class Xogador():
    def __init__(self, nome, puntuacion=0):
        self.__nome = nome
        self.__puntuacion = puntuacion
    
    def get_nome(self):
        return self.__nome
    
    def get_puntuacion(self):
        return self.__puntuacion
    
    def set_puntos(self, p):
        if p:
            self.__puntuacion = self.__puntuacion + p
            return self.__puntuacion
    
    def __str__(self):
        return f"{self.__nome} - Puntos {self.__puntuacion}"
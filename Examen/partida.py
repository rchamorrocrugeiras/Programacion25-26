from xogador import Xogador
class Partida:
    def __init__(self, num_xogadores):
        self.__xogadores = []
        self.__num_max_xogadores = num_xogadores

    def add_xogador(self, xogador):
        if len(self.__xogadores) < self.__num_max_xogadores:
            self.__xogadores.append(xogador)
            return len(self.__xogadores)-1
        else:
            return -1

    def get_xogador(self, nome):
        for xogador in self.__xogadores:
            if xogador.get_nome() == nome:
                return xogador
        return None
    
    def get_xogadores(self):
        return self.__xogadores
    
    def get_xogador_con_min_puntos(self, puntos):
        for xogador in self.__xogadores:
            if xogador.get_puntuacion() >= puntos:
                return xogador
        return None
    
    def add_puntos_a_xogador(self, nome_e_puntos):
        nome, puntos = nome_e_puntos.split()
        xogador = self.get_xogador(nome)
        if xogador is not None:
            xogador.sumar_puntos(int(puntos))
            return xogador.get_puntuacion()
        else:
            raise XogadorNonExisteError("Erro, non hai xogador con ese nome")


if __name__ == "__main__":
    x1 = Xogador ("Pepe")
    x2 = Xogador ("Ana")
    x3 = Xogador ("Xoan")
    x4 = Xogador ("Mario")
    p1 = Partida (4)
    p1.add_xogador (x1)
    p1.add_xogador (x2)
    p1.add_xogador (x3)
    p1.add_xogador (x4)
class Data:
    def __init__(self, dd, mm, aaaa):
        self.setAno(aaaa)
        self.setMes(mm)
        self.setDia(dd)

    def setAno(self, aaaa):
        if aaaa>=0:
            self.__ano=aaaa
        else:
            self.__ano = None
            self.__mm = None
            self.__dd = None

    def getAno(self):
        return self.__ano
    
    def se
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
    
    def setMes(self, mm):
        if mm > 0 and mm <= 12:
            self.__mm=mm
        else:
            self.__ano = None
            self.__mm = None
            self.__dd = None
        
    def getMes(self):
        return self.__mm
    
    def setDia(self, dd):
        if dd > 0 and dd <= 31:
            self.__dd = dd
        else:
            self.__ano = None
            self.__mm = None
            self.__dd = None
    
    def getDia(self):
        return self.__dd
    
    def __str__(self):
        match self.__mm:
            case 1:  mes = "Enero"
            case 2:  mes = "Febrero"
            case 3:  mes = "Marzo"
            case 4:  mes = "Abril"
            case 5:  mes = "Mayo"
            case 6:  mes = "Junio"
            case 7:  mes = "Julio"
            case 8:  mes = "Agosto"
            case 9:  mes = "Septiembre"
            case 10: mes = "Octubre"
            case 11: mes = "Noviembre"
            case 12: mes = "Diciembre"
            case _:  return "Fecha inválida"

        return f"{self.__dd} de {mes} de {self.__ano}"

fecha = Data(5, 6, 3298)
print(fecha)
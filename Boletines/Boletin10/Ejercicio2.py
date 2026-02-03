class FormatoDataError(Exception):
    pass

class Data():
    def __init__(self, dia, mes, ano):
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia) 

    def getDia(self):
        return self._dia

    def setDia(self, dia):
        dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        limite = dias_mes[self._mes]
        
        if self._mes == 2 and self.eBisiesto():
            limite = 29

        if not (1 <= dia <= limite):
            raise FormatoDataError(f"Día {dia} non válido para o mes {self._mes}.")
        self._dia = dia

    def getMes(self):
        return self._mes

    def setMes(self, mes):
        if not (1 <= mes <= 12):
            raise FormatoDataError(f"O mes {mes} non é válido. Debe ser entre 1 e 12.")
        self._mes = mes

    def getAno(self):
        return self._ano

    def setAno(self, ano):
        if not (1970 <= ano <= 2999):
            raise FormatoDataError(f"Ano {ano} fóra de rango (1970-2999).")
        self._ano = ano

    def eBisiesto(self):
        return (self._ano % 4 == 0 and self._ano % 100 != 0) or (self._ano % 400 == 0)
    
    def mostrarData(self):
        print(f"{self._dia:02d}/{self._mes:02d}/{self._ano}")


if __name__ == "__main__":
    try:
        d1 = Data(15, 10, 2026)
        d1.mostrarData()

        d2 = Data(29, 2, 2025) 
    except FormatoDataError as e:
        print(f"Erro capturado: {e}")

    try:
        d3 = Data(1, 1, 1960)
    except FormatoDataError as e:
        print(f"Erro capturado: {e}")
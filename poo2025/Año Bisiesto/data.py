from calendar import month


class Data:
    def __init__(self, day, month, year):
        self.setDia(day)
        self.setMes(month)
        self.setAno(year)

    def setDia(self, day):
        diasmes = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        for mes in diasmes.keys():
            if day > 0 and day <= diasmes[mes]:
                self.__day = day
            else:
                if mes == 2 and self.eBisiesto(self.year):
                    if day == 29:
                        self.__day = 29
                else:
                    self.__year = None
                    self.__month = None
                    self.__day = None




    def getDia(self):
        return self.__day

    def setMes(self, month):
        if month>0 and month<13 and self.__year is not None:
            self.__month = month
        else:
            self.__month = None

    def getMes(self):
        return self.__month

    def setAno(self, year):
        if year >= 0:
            self.__year

    def getAno(self):
        return self.__year

    def eBisiesto(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __str__(self):
        return f"A data é {self.__day}/{self.__month}/{self.__year}"
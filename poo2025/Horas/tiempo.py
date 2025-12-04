from datetime import time

class Tiempo:
    def __init__(self, s, m, h):
        self.setS(s)
        self.setM(m)
        self.setH(h)

    '''
    def __init__(self, hora = 0, *minutoSegundo ):
        if isinstance (hora, int):
            self.__asignacionHoraInt(hora, minutoSegundo)
                    
        if type = (hora) == str:
            self.__asignacionHoraStr (hora)
        
        if isinstance (hora, list) or isinstance (hora, tuple):
            self.__asignacionHoraColeccion(hora)
            
        if isinstance (hora, float):
            self.__asignacionHoraFloat (hora)      
            
            
    def __asignacionHoraInt(self, hora):
        self.setHora (hora)
        if len(minutoSegundo) == 1:
            if isinstance (minutoSegundo[0], int):
                self.setMinuto (minutoSegundo[0])
        elif len(minutoSegundo) == 2:
            if isinstance (minutoSegundo[0], int):
                self.setMinuto (minutoSegundo[0])
            if isinstance (minutoSegundo[1], int):
                self.setMinuto (minutoSegundo[1])
                
    def __asignacionHoraStr(self, hora):
        self.setHora (hora)
        if len(hora) == 8:
            if hora[2] == ":2 and hora[5] == ":":
                hms = hora.split(":")
                if hms[0].isnumeric():
                    h = int(hms[0])
                    if h >=0 and h < 24:
                        self.setHora (h)
                if hms[1].isnumeric():
                    m = int(hms[1])
                    if m >= 0 and m < 60:
                        self.setMinuto (m)
                if hms[2].isnumeric():
                    s = int(hms[2])
                    if s >= 0 and s < 60:
                        self.setSegundo (s)
                        
    def __asignacionHoraColeccion(self, hora):
        self.setHora (hora) 
        if len(hora) == 3:
            h = int(hora[0])
            if h >= 0 and h < 24:
                self.setHora (h)
            m = int(hms[1])
            if m >= 0 and m < 60:
                self.setMinuto (m)
            s = int(hms[2])
            if s >= 0 and s < 60:
                self.setSegundo (s)         
                        
                        
                        
    def __asignacionHoraFloat(self, hora):
        h = int(hora)
        self.setHora(h)

        resto = (hora - h) * 60
        m = int(resto)
        self.setMinuto(m)

        s = int((resto - m) * 60)
        self.setSegundo(s)               
                        '''

    def __str__(self):
        return f"{self.__h:02d}:{self.__m:02d}:{self.__s:02d}"

    def setS(self, s):
        if type(s) == int:
            if s < 60 and s >= 0:
                self.__s = s
            else:
                self.__s = 0
        else: self.__s = 0
        return self.__s

    def setM(self, m):
        if type(m) == int:
            if m < 60 and m >= 0:
                self.__m = m
            else:
                self.__m = 0
        else:
            self.__m = 0
        return self.__m

    def setH(self, h):
        if type(h) == int:
            if h < 24 and h >= 0:
                self.__h = h
            else:
                self.__h = 0
        else:
            self.__h = 0
        return self.__h


    def getS(self):
        return self.__s

    def getM(self):
        return self.__m

    def getH(self):
        return self.__h

    def AS(self):
        return self.__h * 3600 + self.__m * 60 + self.__s

    def AM(self):
        return self.__h * 60 + self.__m + self.__s / 60

    def AH(self):
        return self.__h + self.__m / 60 + self.__s / 3600


    def incremetoS(self, s):

        total = self.__h * 3600 + self.__m * 60 + self.__s + s

        total = total % (24 * 3600)

        self.__h = total // 3600
        total = total % 3600
        self.__m = total // 60
        self.__s = total % 60

    '''PROFE
        def incremetoSeg(self, s):

            s = s % 60
            self.__s = self.__s + s
            if self.__s >= 60:
                self.__s = self.__s % 60
                self.__m += 1
                if self.__m >= 60:
                    self.__m = self.__m % 60
                    self.__h += 1
                    if self.__h >= 24:
                        self.__h = self.__h % 24
            m = s // 60
            self.__m = self.__m + m
            if self.__m >= 60:
                self.__m = self.__m % 60
                self.__h += 1
                if self.__h >= 24:
                    self.__h = self.__h % 24
            h = s // 3600
            self.__h = self.__h + h
            if self.__h > 23:
                self.__h = self.__h % 24
    '''

    def incremetoM(self, m):


        total = self.__h * 3600 + self.__m * 60 + self.__s + m * 60

        total = total % (24 * 3600)

        self.__h = total // 3600
        total = total % 3600
        self.__m = total // 60
        self.__s = total % 60


    def incremetoH(self, h):

        total = self.__h * 3600 + self.__m * 60 + self.__s + h * 3600

        total = total % (24 * 3600)

        self.__h = total // 3600
        total = total % 3600
        self.__m = total // 60
        self.__s = total % 60
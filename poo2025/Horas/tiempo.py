from datetime import time

class Tiempo:
    """Clase que representa un tiempo en formato HH:MM:SS"""

    def __init__(self, hora=0, *extra):
        self.__h = 0
        self.__m = 0
        self.__s = 0

        if isinstance(hora, int):
            self.__asignacionHoraInt(hora, extra)
        elif isinstance(hora, str):
            self.__asignacionHoraStr(hora)
        elif isinstance(hora, (list, tuple)):
            self.__asignacionHoraColeccion(hora)
        elif isinstance(hora, float):
            self.__asignacionHoraFloat(hora)

    # Asignaciones
    def __asignacionHoraInt(self, h, extra):
        self.setH(h)
        if len(extra) >= 1:
            self.setM(extra[0])
        if len(extra) == 2:
            self.setS(extra[1])

    def __asignacionHoraStr(self, hora):
        if len(hora) == 8 and hora[2] == ":" and hora[5] == ":":
            h, m, s = hora.split(":")
            if h.isdigit(): self.setH(int(h))
            if m.isdigit(): self.setM(int(m))
            if s.isdigit(): self.setS(int(s))

    def __asignacionHoraColeccion(self, col):
        h = int(col[0]) if len(col) > 0 else 0
        m = int(col[1]) if len(col) > 1 else 0
        s = int(col[2]) if len(col) > 2 else 0
        self.setH(h)
        self.setM(m)
        self.setS(s)

    def __asignacionHoraFloat(self, hora):
        h = int(hora)
        self.setH(h)
        resto = (hora - h) * 60
        m = int(resto)
        self.setM(m)
        s = int((resto - m) * 60)
        self.setS(s)

    # Setters
    def setS(self, s): self.__s = s if isinstance(s,int) and 0 <= s < 60 else 0
    def setM(self, m): self.__m = m if isinstance(m,int) and 0 <= m < 60 else 0
    def setH(self, h): self.__h = h if isinstance(h,int) and 0 <= h < 24 else 0

    # Getters
    def getS(self): return self.__s
    def getM(self): return self.__m
    def getH(self): return self.__h

    # Conversiones
    def AS(self): return self.__h*3600 + self.__m*60 + self.__s
    def AM(self): return self.__h*60 + self.__m + self.__s/60
    def AH(self): return self.__h + self.__m/60 + self.__s/3600

    # Incrementos
    def incrementarSegundos(self, s):
        total = self.AS() + s
        total %= 24*3600
        self.__h = total//3600
        total %= 3600
        self.__m = total//60
        self.__s = total%60

    def incrementarMinutos(self, minutos):
        segundos = int(minutos*60)
        self.incrementarSegundos(segundos)

    def incrementarHoras(self, horas):
        segundos = int(horas*3600)
        self.incrementarSegundos(segundos)

    # Representación
    def __str__(self):
        return f"{self.__h:02d}:{self.__m:02d}:{self.__s:02d}"


# PRUEBAS

h1 = Tiempo(23, 59, 59)
h2 = Tiempo()
h3 = Tiempo(12)
h4 = Tiempo(12, 10, 30)
h4.incrementarMinutos(10.5)
h5 = Tiempo([230,240,560,56])
h5.incrementarMinutos(5.5)

print(h1)  
print(h2)  
print(h3)  
print(h4)  
print(h5)  

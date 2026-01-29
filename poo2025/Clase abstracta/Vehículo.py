from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia):
        self.matricula = matricula
        self.velocidadeMaxima = velocidadeMaxima
        self.autonomia = autonomia

    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def velocidadeMaxima(self):
        return self._velocidadeMaxima
    
    @velocidadeMaxima.setter
    def velocidadeMaxima(self, velocidadeMaxima):
        self._velocidadeMaxima = velocidadeMaxima

    @property
    def autonomia(self):
        return self._autonomia
    
    @autonomia.setter
    def autonomia(self, autonomia):
        self._autonomia = autonomia
    
    @abstractmethod
    def arrincar(self):
        pass

    def deter(self):
        print(f"O vehículo {self._matricula} está detido")
    
    @abstractmethod
    def mostrar_datos(self):
        pass

class Terrestre(Vehiculo, ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numero_rodas):
        super().__init__(matricula, velocidadeMaxima, autonomia)
        self.numero_rodas = numero_rodas
    
    @property
    def numero_rodas(self):
        return self._numero_rodas
    
    @numero_rodas.setter
    def numero_rodas(self, numero_rodas):
        self._numero_rodas = numero_rodas

class Aereo(Vehiculo, ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia, altitude_maxima):
        super().__init__(matricula, velocidadeMaxima, autonomia)
        self.altitude_maxima = altitude_maxima
    
    @property
    def altitude_maxima(self):
        return self._altitude_maxima
    
    @altitude_maxima.setter
    def altitude_maxima(self, altitude_maxima):
        self._altitude_maxima = altitude_maxima

class CocheAutonomo(Terrestre):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numero_rodas, numero_prazas):
        super().__init__(matricula, velocidadeMaxima, autonomia, numero_rodas)
        self.numero_prazas = numero_prazas

    @property
    def numero_prazas(self):
        return self._numero_prazas
    
    @numero_prazas.setter
    def numero_prazas(self, numero_prazas):
        self._numero_prazas = numero_prazas
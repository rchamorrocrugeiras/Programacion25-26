class Consumo():
    def __init__(self, km=0, litros=0, vMed=0, pGas=0):
        self.__km = km
        self.__litros = litros
        self.__vMed = vMed
        self.__pGas = pGas
    
# Getters
    def getKm(self):
        return self.__km
    
    def getLitros(self):
        return self.__litros
    
    def getVMed(self):
        return self.__vMed
    
    def getPGas(self):
        return self.__pGas

# Setters
    def setKms(self, km):
        self.__km = km
    
    def setLitros(self, litros):
        self.__litros = litros

    def setVMed(self, vMed):
        self.__vMed = vMed

    def setPGas(self, pGas):
        self.__pGas = pGas


# Métodos
    def getTiempo(self):
        if self.__vMed > 0:
            return self.__km / self.__vMed
        else:
            return 0
    
    def consumoMedio(self):
        if self.__litros > 0:
            return (self.__litros / self.__km) * 100
        else:
            return 0
    
    def consumoLitros(self):
        return self.consumoMedio * self.__pGas / 100


# Clase principal
def main():
    coche1 = Consumo()
    coche1.setLitros(50)
    coche1.setPGas(1.57)
    print(f"Litros: {coche1.getLitros()} L")
    print(f"Prezo gasolina: {coche1.getPGas()} €/L")

    coche2 = Consumo(km=500, litros=40, vMed=100, pGas=1.57)

    print(f"Consumo medio: {coche2.consumoMedio():.2f} L/100 km")

    coche2.setLitros(45)
    print(f"Consumo medio tras cambiar litros: {coche2.consumoMedio():.2f} L/100 km")

    print(f"Velocidade media: {coche2.getVMed()} km/h")


# Ejecutar
if __name__ == "__main__":
    main()
class Cuenta:
# Método inicializador
    def __init__(self, cliente="", cuenta="", interes=0.0, saldo=0.0):
        self.__cliente = cliente
        self.__cuenta = cuenta
        self.__interes = interes
        self.__saldo = saldo

# Getters
    def getCliente(self):
        return self.__cliente
    
    def getCuenta(self):
        return self.__cuenta
    
    def getInteres(self):
        return self.__interes
    
    def getSaldo(self):
        return self.__saldo

# Setters
    def setCliente(self, cliente):
        self.__cliente = cliente
    
    def setCuenta(self, cuenta):
        self.__cuenta = cuenta
    
    def setInteres(self, interes):
        self.__interes = interes
    
    def setSaldo(self, saldo):
        self.__saldo = saldo

# Métodos
    def ingreso(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return self.__saldo
        else:
            return "Error"
    
    def reintegro(self, cantidad):
        if cantidad > 0:
            self.__saldo -= cantidad
            if self.__saldo >= 0:
                return self.__saldo
            else:
                return "El saldo no puede ser negativo"
        else:
            return "La cantidad a retirar no puede ser negativa"
    
    def transferencia(self, cuenta_destino, importe):
        if importe < 0:
            return "Error"
        if importe > self.__saldo:
            return "Error, saldo insuficiente"
        self.__saldo -= importe
        cuenta_destino.ingreso(importe)
        return f"Transferencia de {importe}€ realizada a {cuenta_destino.getCliente()}"

# Clase principal
def main():
    cuenta1 = Cuenta("René", "ES123456789", 1.5, 1000)
    cuenta2 = Cuenta("Borja", "ES987654321", 1.2, 500)

    print(f"Cuenta1: {cuenta1.getCliente()}, Saldo: {cuenta1.getSaldo()}€")
    print(f"Cuenta2: {cuenta2.getCliente()}, Saldo: {cuenta2.getSaldo()}€")

    cuenta1.ingreso(100)
    cuenta2.ingreso(300)
    cuenta1.transferencia(cuenta2, 200)

    print("Después de los ingresos y las transferencias:")

    print(f"Saldo final Cuenta1: {cuenta1.getSaldo()}€")
    print(f"Saldo final Cuenta2: {cuenta2.getSaldo()}€")


# Ejecutar
if __name__ == "__main__":
    main()
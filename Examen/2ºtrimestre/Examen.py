import csv

# Ejercicio 1
class Barco:
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes):
        self.set_nome = nome
        self.set_matricula(matricula)
        self.set_bandeira(bandeira)
        self.set_salvavidas(salvavidas)
        self.set_eslora(eslora)
        self.set_volume(volume)
        self.set_tripulantes(tripulantes)

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_bandeira(self):
        return self.__bandeira

    def set_bandeira(self, bandeira):
        self.__bandeira = bandeira

    def get_salvavidas(self):
        return self.__salvavidas

    def set_salvavidas(self, salvavidas):
        self.__salvavidas = salvavidas

    def get_eslora(self):
        return self.__eslora

    def set_eslora(self, eslora):
        self.__eslora = eslora

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    def get_tripulantes(self):
        return self.__tripulantes

    def set_tripulantes(self, tripulantes):
        if tripulantes > self.__salvavidas:
            raise ValueError("A tripulación non pode superar os salvavidas")
        self.__tripulantes = tripulantes

    def calculo_facturacion(self):
        pass

    def __str__(self):
        return f"Nome: {self.__nome}, Matricula: {self.__matricula}, Bandeira: {self.__bandeira}, Salvavidas: {self.__salvavidas}, Eslora: {self.__eslora}, Volume: {self.__volume}, Tripulantes: {self.__tripulantes}"

class BarcoPasaxeiros(Barco):
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera, prazas_turista):
        super().__init__(nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes)
        self.set_prazas_primera(prazas_primera)
        self.set_prazas_turista(prazas_turista)

    def get_prazas_primera(self):
        return self.__prazas_primera

    def set_prazas_primera(self, valor):
        if (valor + self.get_tripulantes()) > self.get_salvavidas():
            raise ValueError("Superase a capacidade de salvavidas")
        self.__prazas_primera = valor

    def get_prazas_turista(self):
        return self.__prazas_turista

    def set_prazas_turista(self, valor):
        if (valor + self.get_tripulantes()) > self.get_salvavidas():
            raise ValueError("Supérase a capacidade de salvavidas")
        self.__prazas_turista = valor

    def calculo_facturacion(self, millas, porcentaxe_ocupacion):
        facturacion_primera = self.__prazas_primera * porcentaxe_ocupacion * millas * 0.7
        facturacion_turista = self.__prazas_turista * porcentaxe_ocupacion * millas * 0.55
        return facturacion_primera + facturacion_turista

    def __str__(self):
        return super().__str__() + f", 1ª Clase: {self.__prazas_primera}, Turista: {self.__prazas_turista}"

class BarcoPasaxeirosVehiculos(BarcoPasaxeiros):
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera, prazas_turista, prazas_turismos):
        super().__init__(nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera, prazas_turista)
        self.set_prazas_turismos(prazas_turismos)

    def get_prazas_turismos(self):
        return self.__prazas_turismos

    def set_prazas_turismos(self, valor):
        self.__prazas_turismos = valor

    def calculo_facturacion(self, millas, porcentaxe_ocupacion):
        base = super().calculo_facturacion(millas, porcentaxe_ocupacion)
        return base + (self.__prazas_turismos * porcentaxe_ocupacion * millas * 1.5)

    def __str__(self):
        return super().__str__() + f", Turismos: {self.__prazas_turismos}"

class BarcoPasaxeirosCompleto(BarcoPasaxeirosVehiculos):
    def __init__(self, nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera, prazas_turista, prazas_turismos, prazas_camions):
        super().__init__(nome, matricula, bandeira, salvavidas, eslora, volume, tripulantes, prazas_primera, prazas_turista, prazas_turismos)
        self.set_prazas_camions(prazas_camions)

    def get_prazas_camions(self):
        return self.__prazas_camions

    def set_prazas_camions(self, valor):
        self.__prazas_camions = valor

    def __str__(self):
        return super().__str__() + f", Camións: {self.__prazas_camions}"

# Ejercicio 2
class Barco2:
    def __init__(self, matricula):
        self.__matricula = self.__verificar_matricula(matricula)

    def get_matricula(self):
        return self.__matricula

    def __verificar_matricula(self, matricula):
        partes = matricula.split("-")
        if len(partes) != 4:
            raise ValueError("Formato de matricula incorrecto")
        
        inicio = partes[0].split(" ")
        if len(inicio) != 2 or not inicio[0].endswith("ª"):
            raise ValueError("Erro na lista de actividade ou provincia")
        
        if not (partes[1].isdigit() and partes[2].isdigit() and len(partes[3]) == 2):
            raise ValueError("Erro nos díxitos de distrito, folio ou ano")
        
        return matricula

# Ejercicio 3
class LinhaTren:
    def __init__(self, numero: str, orixe: str, destino: str, capacidade: int):
        self.numero = numero
        self.orixe = orixe
        self.destino = destino
        self.capacidade = capacidade

def xestionar_linhas():
    linhas = []
    while True:
        print("\n1. Alta | 2. Buscar por orixe | 3. Borrar por numero | 4. Sair")
        opcion = input("Opción: ")
        
        if opcion == "1":
            numero = input("Numero: ")
            orixe = input("Orixe: ")
            destino = input("Destino: ")
            capacidade = int(input("Capacidade: "))
            linhas.append(LinhaTren(numero, orixe, destino, capacidade))
        elif opcion == "2":
            busqueda = input("Orixe a buscar: ")
            for linha in linhas:
                if linha.orixe == busqueda:
                    print(f"Liña {linha.numero} con destino {linha.destino}")
        elif opcion == "3":
            borrar = input("Numero de liña a borrar: ")
            linhas = [linha for linha in linhas if linha.numero != borrar]
        elif opcion == "4":
            break
    return linhas

# Ejercicio 4
def ler_ficheiro_tren(suposto4):
    lista_tren = []
    try:
        with open(suposto4.txt, 'r') as f:
            for linea in f:
                if linea.strip():
                    parte_num, resto = linea.split(":")
                    parte_ruta, parte_prazas = resto.strip().split("Prazas:")
                    orixe, destino = parte_ruta.strip().split("-")
                    
                    obxecto = LinhaTren(
                        parte_num.strip(),
                        orixe.strip(),
                        destino.strip(),
                        parte_prazas.strip()
                    )
                    lista_tren.append(obxecto)
    except FileNotFoundError:
        print("Ficheiro non atopado")
    return lista_tren

# Probas
if __name__ == "__BarcoPasaxeirosVehiculos__":
    b1 = Barco("Titanic", "0000AAA", "española", 500, 50, 200, 350)
    b1.calculo_facturacion

if __name__ == "__Barco2__":
    b2 = Barco2("7ª VI-2-63-19")
    b2.__verificar_matricula

if __name__ == "__LinhaTren__":
    l1 = LinhaTren("100", "Galicia", "Brasil", 200)

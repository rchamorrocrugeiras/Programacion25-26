import re

class DniNonValido(Exception):
    pass

class LicenciaIncorrecta(Exception):
    pass

class Persoa():
    def __init__(self, nome="", direccion="", dni=""):
        self._nome = nome
        self._direccion = direccion
        self._dni = ""
        if dni:
            self.setDNI(dni)

    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome

    def getDireccion(self):
        return self._direccion
    
    def setDireccion(self, direccion):
        self._direccion = direccion

    def getDNI(self):
        return self._dni
    
    def setDNI(self, dni):
        if type(dni) == str:
            if len(dni) == 9 :
                int(dni[:-1])
                if dni[:-1].isdigit():
                    if dni[-1:].isalpha():
                        letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
                        resto = int(dni[:-1]) % 23
                        letra_correcta = letraDni[resto]
                        if letra_correcta == dni[-1].upper():

                            self.__dni = dni.upper()
                        else:
                            raise DniError(f"La letra no es ta entre las selecionadas para un DNI")
                    else:
                        raise DniError(f"Los 9 primeros digitos no son numeros")
                else:
                    raise DniError(f"El ultimo dígito no es una letra")
            else:
                raise DniError(f"El numero de carateres no es el adecuado")
        else:
            raise TypeError(f"el tipo de {type(dni)} tiene que ser str")
    def getDni(self):
        return self.__dni


class Deportista(Persoa):
    def __init__(self, nome="", direccion="", dni="", deporte="", clube="", licencia=""):
        super().__init__(nome, direccion, dni)
        self._deporte = deporte
        self._clube = clube
        self._licencia = licencia
    
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte):
        self._deporte = deporte

    def getClube(self):
        return self._clube
    
    def setClube(self, clube):
        self._clube = clube

    def getLicencia(self):
        return self._licencia
    
    def setLicencia(self, licencia):
        self._licencia = licencia


if __name__ == "__main__":
    try:
        print("Probando Deportista")
        d = Deportista()
        d.setNome("Ana")
        d.setDNI("12345678Z")
        print(f"DNI establecido: {d.getDni()}")
        
        d.setLicencia("2024fut000001") 
        print(f"Licencia establecida: {d.getLicencia()}")
        
        d.setLicencia("licencia_mala") 

    except (DniNonValido, LicenciaIncorrecta) as e:
        print(f"Error capturado: {e}")
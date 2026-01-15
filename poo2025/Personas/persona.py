from ErrorDNi import DniError
class persoa:
    def __init__(self,nome,dni,idade):
        self.setNome(nome)
        self.setDni(dni)
        self.setIdade(idade)

    def setNome(self,nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            self.__nome = ("Error")
    def getNome(self):
        return self.__nome

    def setIdade(self,idade):
        if type(idade) == int:
            if idade >=0:
                self.__idade = idade
            else:
                self.__idade = ("Error")
        else:
            self.__idade = ("Error")
    def getIdade(self):
        return self.__idade

    def setDni(self,dni):
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


    def __str__(self):
        return (f"El nombre es: {self.__nome}, o DNI es: {self.__dni} y la edad es: {self.__idade}")
if __name__=='__main__':
    try:
        alan = persoa("Alan","00000000T",20)
        print("DNI válido:",alan)
    except DniError as e:
        print("Error con p1: ",e)
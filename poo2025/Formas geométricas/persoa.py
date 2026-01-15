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
                raise ValueError(f"O valor {idade} tenque ser maior que cero ")
        else:
            raise TypeError(f"el tipo de {type(idade)} tiene que ser int")
    def getIdade(self):
        return self.__idade

    def setDni(self,dni):
        if len(dni)== 9:
            if dni[-1:].isalpha():
                if dni[:-1].isalpha():
                    letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
                    resto = int(dni[:-1]) % 23
                    if letraDni[resto] == dni[-1:].upper():
                        return True
                    else:
                        return False
                else:
                    raise ValueError("Letra del dni incorecta")
            else:
                raise ValueError("Los 8 primeros caracteres tien que ser numeros")
        else:
            raise ValueError("Lonxitude incorecta")
    def getDni(self):
        return self.__dni

    nome = property(getNome,setNome)
    idade = property(getIdade,setIdade)
    dni = property(getDni,setDni)

    def __str__(self):
        return self.__nome + " " + str(self.__dni) + " " + str(self.__idade)
if __name__=='__main__':
    try:
        p = persoa("Alan","554380238","10")
    except ValueError as e:
        print("Error: " + str(e))
        intentos = 0
        edade = int(input("Introduce la edad: "))
        while edade < 0 and intentos < 2:
            intentos += 1
            print("Edade non valida")
            edade = int(input("Introduce un número la edada: "))
        p = persoa("Alan","554380238",edade)
        print(p)

    except TypeError as t:
        print("Error: "+ str(t))


    finally:
        print("Fin del programa")
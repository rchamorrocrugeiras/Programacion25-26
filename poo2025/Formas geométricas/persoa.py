class Persoa:
    def __init__(self, nome, idade, dni, direccion, nacionalidade):
        self.nome = nome
        if self.comprobarIdade(idade):
            self.idade = idade
        else:
            self.idade = 0
        if self.comprobarDni(dni):
            self.dni = dni
        else:
            self.dni = "00000000X"
        self.direccion = direccion
        self.nacionalidade = nacionalidade

    def comprobarIdade(self, idade):
        if idade >= 0 and idade <= 150:
            return True
        else:
            return False


    def comprobarDni(self, dni):
        if len(dni) == 9 and dni[:-1].isDigit() and dni[-1:].isAlpha():
            letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
            resto = int(dni[:-1]) % 23
            if letraDni[resto] == dni[-1:].upper():
                return True
            else:
                return False
        else: 
            return False
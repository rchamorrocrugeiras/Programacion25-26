from persona import persoa
from NussError import NussError
class trabajador(persoa):
    def __init__(self,nome,dni,idade,nuss):
        super().__init__(nome,dni,idade)
        self.setNUSS(nuss)

    def setNUSS(self,nuss):
        if len(nuss) != 16:
            raise NussError("La longitud de NUSS es inadecuada(16)")
        elif nuss[:2]!="/" or nuss[-3]!="/":
            raise NussError ("O formato é nn/nnnnnnnnn/nn. Error de formato")
        elif not nuss[:2].isdigit() or not nuss[3:-3].isdigit() or not nuss[-2:].isdigit():
            raise NussError("Formato de NUSS incorecto, error en los digitos")
        self.nuss=nuss
    def getNUSS(self):
        return self.nuss
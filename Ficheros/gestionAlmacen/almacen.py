import csv



class Almacen:
    def __init__(self, rutaFicheiro):
        self.listaProdutos = []
        self.cargarProdutos(rutaFicheiro)

    def cargarProdutos(self, ficheiro):
        with open (ficheiro, 'r', newline='') as fich:
            readerProdutos = csv.DictReader(fich)
            for linhaproduto in readerProdutos:
                p = Produto (linhaproduto['Nome'],
                             linhaproduto['Cantidade'],
                             linhaproduto['Prezo'])
                self.listaProdutos.append(p)

if __name__ == "__main__":

import csv
from produto import Produto


class Almacen:
    def __init__(self, rutaFicheiro):
        self.listaProdutos = []
        self.cargarProdutos(rutaFicheiro)

    def engadirProduto(self, produto):
        self.listaProdutos.append(produto)

    def cargarProdutosFicheiro(self, rutaFicheiro):
        with open (rutaFicheiro, 'r', newline='') as fich:
            readerProdutos = csv.DictReader(fich)
            for linhaproduto in readerProdutos:
                p = Produto (linhaproduto['Nome'],
                            linhaproduto['Cantidade'],
                            linhaproduto['Prezo'])
                self.listaProdutos.append(p)

    def gardarProdutosFicheiro(self, rutaFicheiro):
        with open (rutaFicheiro, 'r', newline='') as fich:
            writerProdutos = csv.DictWriter(fich)
            

if __name__ == "__main__":

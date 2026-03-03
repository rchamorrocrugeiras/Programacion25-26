class GestionAlmacen:
    def __init__(self):
    
    
    
    def menuPrincipal(self):


        while True:






            print("2. Engadir produto")
            print("3. Sair")
            match opcion:
                case '1':
                    self.mostrarProdutos()
                case '2':
                    self.dialogoEngadirProduto()
                case '3':
                    break
    
        def mostrarProdutos(self):
          for produto in self.almacen.listaProdutos:
                print(f" Cantidade {produto.nombre}: {produto.cantidad}: {produto.precio}")
                print(f" Precio: {produto.precio}")


        def dialogoEngadirProduto(self):
            nombre = input("Introduza nome de produto: ")
            cantidad = int(input("Introduza cantidade de produto: "))
            precio = float(input("Introduza cantidade de produto: "))
            print(f"Vai a introducir {cantidad} unidades do produto {produto} ")
            correcto = input("É correcto? (s/n)")
            if correcto == 's':
                 self.almacen.introducirProduto(Produto(nombre, cantidad, precio))


if __name__ = "__main__":
    gestor = GestionAlmacen()
    gestor.menuPrincipal()
class GestionAlmacen:
    def __init__(self):
    
    
    
    def menuPrincipal(self):








                case '1':
                    self.mostrarProdutos()
                case '2':
                    break
    
        def mostrarProdutos(self):
          for produto in self.almacen.listaProdutos:
                print(f" Cantidade {produto.nombre}: {produto.cantidad}: {produto.precio}")
                print(f" Precio: {produto.precio}")

if __name__ = "__main__":
    gestor = GestionAlmacen()
    gestor.menuPrincipal()
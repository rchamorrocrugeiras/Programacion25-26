'''
Crea unha clase chamada Libro que conteña os seguintes atributos:
titulo
autor
ano
numPaginas
valoracion


A clase debe de ter o método de inicialización.
Establecer os métodos de acceso para todos os atributos (geters). 
Crear os métodos de asignación dos atributos (seters)
Establecer as propiedades de forma que só se poida acceder os atributos mediante os métodos adicados a elo (geters e seters).
Codificar o metodo amosarLibro, que devolte unha cadea e visualiza tódalas característica dun libro. 
Crear unha clase Principal co método main. Crear un libro con cada construtor e mostrar por consola a súa información. 
'''


class Libro:
    def __init__(self, titulo, autor, ano, numPaginas, valoracion):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__numPaginas = numPaginas
        self.__valoracion = valoracion

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano(self):
        return self.__ano

    def get_numPaginas(self):
        return self.__numPaginas

    def get_valoracion(self):
        return self.__valoracion

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_ano(self, ano):
        self.__ano = ano

    def set_numPaginas(self, numPaginas):
        self.__numPaginas = numPaginas

    def set_valoracion(self, valoracion):
        self.__valoracion = valoracion

    # Propiedades
    titulo = property(get_titulo, set_titulo)
    autor = property(get_autor, set_autor)
    ano = property(get_ano, set_ano)
    numPaginas = property(get_numPaginas, set_numPaginas)
    valoracion = property(get_valoracion, set_valoracion)

    # Método para amosar libro
    def amosarLibro(self):
        return (
            f"Título: {self.__titulo}\n"
            f"Autor: {self.__autor}\n"
            f"Año: {self.__ano}\n"
            f"Número de páxinas: {self.__numPaginas}\n"
            f"Valoración: {self.__valoracion}/5"
        )


class Principal:
    def main():
        libro1 = Libro("Aprender Python", "Manuel Guimarey", 2018, 417, 4.9)
        libro2 = Libro("El fútbol", "René Chamorro", 2025, 328, 4.8)

        print("Información do libro 1:")
        print(libro1.amosarLibro())
        print("\nInformación do libro 2:")
        print(libro2.amosarLibro())


# Executar o programa
if __name__ == "__main__":
    Principal.main()
# Gestión de una biblioteca

class Libro:
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.__disponible = True

# Getters
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getAno(self):
        return self.__año

    def estaDisponible(self):
        return self.__disponible

# Métodos
    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "DISPONIBLE" if self.__disponible else "PRESTADO"
        return f"{self.__titulo} ({self.__autor}, {self.__año}) - {estado}"


class Usuario:
    def __init__(self, nome, idUsuario):
        self.__nome = nome
        self.__id = idUsuario
        self.__librosPrestados = []

    def getNome(self):
        return self.__nome
    
    def getId(self):
        return self.__id
    
    def getLibrosPrestados(self):
        return self.__librosPrestados
    
    def engadirLibro(self, libro):
        self.__librosPrestados.append(libro)
    
    def quitarLibro(self, libro):
        if libro in self.__librosPrestados:
            self.__librosPrestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.__nome} (ID: {self.__id})"


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []

    def engadirLibro(self, libro):
        self.__libros.append(libro)

    def engadirUsuario(self, usuario):
        self.__usuarios.append(usuario)

    def prestarLibro(self, libro, usuario):
        if not libro.estaDisponible():
            print(f"❌ O libro '{libro.getTitulo()}' xa está prestado.")
            return False
        
        libro.prestar()
        usuario.engadirLibro(libro)
        print(f"✔ Préstamo realizado: '{libro.getTitulo()}' → {usuario.getNome()}")
        return True

    def devolverLibro(self, libro, usuario):
        if libro not in usuario.getLibrosPrestados():
            print(f"❌ O usuario {usuario.getNome()} non ten ese libro.")
            return False
        
        libro.devolver()
        usuario.quitarLibro(libro)
        print(f"✔ Devolución realizada: '{libro.getTitulo()}' ← {usuario.getNome()}")
        return True

    def listarLibros(self):
        print("\n=== LISTA DE LIBROS ===")
        for l in self.__libros:
            print(l)

    def listarUsuarios(self):
        print("\n=== LISTA DE USUARIOS ===")
        for u in self.__usuarios:
            print(u)


# Pruebas
def main():
    biblio = Biblioteca()

    u1 = Usuario("Ana", 1)
    u2 = Usuario("Pedro", 2)

    biblio.engadirUsuario(u1)
    biblio.engadirUsuario(u2)

    l1 = Libro("O Señor dos Aneis", "Tolkien", 1954)
    l2 = Libro("1984", "George Orwell", 1949)
    l3 = Libro("O Principiño", "Saint-Exupéry", 1943)

    biblio.engadirLibro(l1)
    biblio.engadirLibro(l2)
    biblio.engadirLibro(l3)

    biblio.listarLibros()
    biblio.listarUsuarios()

    print("\n--- PROBAS DE PRÉSTAMOS ---")
    biblio.prestarLibro(l1, u1)
    biblio.prestarLibro(l1, u2) 

    print("\n--- PROBAS DE DEVOLUCIÓN ---")
    biblio.devolverLibro(l1, u2)  
    biblio.devolverLibro(l1, u1)  

    print("\n--- ESTADO FINAL ---")
    biblio.listarLibros()


# Ejecutar
if __name__ == "__main__":
    main()
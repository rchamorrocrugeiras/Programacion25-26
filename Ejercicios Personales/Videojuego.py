# Simulación de un videojuego

class Arma:
    def __init__(self, tipo, dano, durabilidad):
        self.__tipo = tipo
        self.__dano = dano
        self.__durabilidad = durabilidad

    def getDano(self):
        return self.__dano

    def usar(self):
        """Reduce la durabilidad al usar el arma en un ataque."""
        if self.__durabilidad > 0:
            self.__durabilidad -= 1
            return True
        return False

    def estaRota(self):
        return self.__durabilidad <= 0

    def __str__(self):
        estado = "ROTA" if self.estaRota() else f"Durabilidad: {self.__durabilidad}"
        return f"Arma: {self.__tipo} (Daño: {self.__dano}, {estado})"


class Personaje:
    def __init__(self, nombre, vida=100, fuerza=10, defensa=5):
        self.__nombre = nombre
        self.__vida = vida
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__nivel = 1
        self.__arma = None

    # Métodos principales
    def equiparArma(self, arma):
        self.__arma = arma
        print(f"🔧 {self.__nombre} ha equipado {arma}")

    def atacar(self, monstruo):
        if self.__arma is None:
            dano = self.__fuerza
        else:
            if self.__arma.estaRota():
                print(f"❌ ¡El arma de {self.__nombre} está rota! Ataca sin arma.")
                dano = self.__fuerza
            else:
                dano = self.__fuerza + self.__arma.getDano()
                self.__arma.usar()

        danoFinal = max(0, dano - monstruo.getDefensa())
        monstruo.recibirDano(danoFinal)

        print(f"⚔️ {self.__nombre} ataca a {monstruo.getNombre()} y causa {danoFinal} de daño.")

    def recibirDano(self, dano):
        self.__vida -= dano
        print(f"💥 {self.__nombre} recibe {dano} puntos de daño. Vida restante: {self.__vida}")

    def subirNivel(self):
        self.__nivel += 1
        self.__vida += 10
        self.__fuerza += 2
        self.__defensa += 1
        print(f"⬆️ {self.__nombre} ha subido al nivel {self.__nivel}!")

    def estaVivo(self):
        return self.__vida > 0

    def __str__(self):
        arma = str(self.__arma) if self.__arma else "Sin arma"
        return (f"Personaje: {self.__nombre} | Vida: {self.__vida} | "
                f"Fuerza: {self.__fuerza} | Defensa: {self.__defensa} | "
                f"Nivel: {self.__nivel} | {arma}")


class Monstruo:
    def __init__(self, nombre, vida, defensa, dificultad):
        self.__nombre = nombre
        self.__vida = vida
        self.__defensa = defensa
        self.__dificultad = dificultad

    def getNombre(self):
        return self.__nombre
    
    def getDefensa(self):
        return self.__defensa
    
    def recibirDano(self, dano):
        self.__vida -= dano
        print(f"👹 {self.__nombre} recibe {dano} de daño. Vida restante: {self.__vida}")

    def estaVivo(self):
        return self.__vida > 0

    def __str__(self):
        return f"Monstruo: {self.__nombre} (Vida: {self.__vida}, Defensa: {self.__defensa}, Dificultad: {self.__dificultad})"


# Combate
def combate(personaje, monstruo):
    print("\n🔥 ¡COMIENZA EL COMBATE! 🔥")
    print(personaje)
    print(monstruo)
    print()

    while personaje.estaVivo() and monstruo.estaVivo():
        personaje.atacar(monstruo)
        if not monstruo.estaVivo():
            print(f"🏆 ¡{personaje._Personaje__nombre} ha derrotado al monstruo {monstruo.getNombre()}!")
            personaje.subirNivel()
            break

        # El monstruo ataca
        dano = max(0, monstruo._Monstruo__dificultad * 2 - personaje._Personaje__defensa)
        personaje.recibirDano(dano)

        if not personaje.estaVivo():
            print(f"💀 {personaje._Personaje__nombre} ha sido derrotado por el monstruo.")
            break


# Pruebas
def main():
    # Crear personaje
    heroe = Personaje("Arthas")
    
    # Crear arma
    espada = Arma("Espada Larga", dano=15, durabilidad=3)
    
    # Equipar arma
    heroe.equiparArma(espada)
    
    # Crear monstruo
    orco = Monstruo("Orco Salvaje", vida=50, defensa=5, dificultad=3)

    # Simular combate
    combate(heroe, orco)


# Ejecutar
if __name__ == "__main__":
    main()
from punto import Punto
from circulo import Circulo
from persoa import Persoa
from punto2 import Punto2
from esfera import Esfera

'''
p3 = Punto2(5,6)
p3.setX(7)
p3.x = 6
print(p3)
print(p3.x)
print(p3.getY())

p1 = Punto(-2, 3)
print(p1)
p2 = Punto(9, 1)
p2.x = 2
p2.y = 3

print(p1.toString())
print(p2)
'''

esfera1 = Esfera(2,3,5)
print(esfera1.calcularArea())
print(esfera1.calcularVolume())

'''
print(p1.x)

manuel = Persoa ( "Manuel",dni="00000000T", nacionalidad="Española",direccion="Su casa",edad=18)
manuela = Persoa ( "Manuela",dni="00000000T", nacionalidad="Española",direccion="Su casa",edad=21)
print(manuel)
print(manuela == manuel)
print(manuela > manuel)
print(manuela < manuel)
'''

# Punto 2
def prueba_punto():
    # Creando punto (3, 4)
    p = Punto2(3, 4)
    print(p)

    # Probando setters con valores válidos
    p.x = 10
    p.y = 20
    print(p)

    # Probando setters con valores negativos (deben ponerse a 0)
    p.x = -5
    p.y = -8
    print(p)

    # Probando getters
    print("x =", p.x)
    print("y =", p.y)

    # Probando error de tipo
    try:
        p.x = "hola"
    except TypeError as e:
        print("Error,", e)

if __name__ == "__main__":
    prueba_punto()
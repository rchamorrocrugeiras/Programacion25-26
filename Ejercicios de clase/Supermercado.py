# Supermercado donde hay cajas donde hay dinero en efectivo, que está almacenado en una lista
# efectivo[['1',(valor do billete-moneda, numero),(200,1),(50,13),(0,50,12)...]], ['2',]
# facer unha aplicacion que me de o importe por caixa e o total
# - calculo importe por caixa -> funcion
# - calculo importe total -> funcion
# - impresion contido caixa -> funcion
# - impresion contido total -> funcion
# hacer un programa con una funcion general

efectivo = [
    ['1', [200,2],[100,4],[50,8],[5,15],[0.05,20]], 
    ['2', [100,1],[50,15],[10,5],[2,10],[0.20,5],[0.10,5]],
    ['3', [50,10],[20,10],[1,5],[0.50,10]]
    ]

def efectivo_cajas(efectivos):
    for caja in efectivos:
        mostrador = caja[1:]
        suma = 0
        for lista in mostrador:
            multiplicacion = lista[0] * lista[1]
            suma += multiplicacion
        print(suma)

def efectivo_cajas_total(efectivos):
    suma = 0
    for caja in efectivos:
        mostrador = caja[1:]
        for lista in mostrador:
            multiplicacion = lista[0] * lista[1]
            suma += multiplicacion
    print(suma)

def contenido_cajas(efectivos):
    for caja in efectivos:
        mostrador = caja[1:]
        for lista in mostrador:
            existe = lista[0], lista[1]
            print(existe)
        print()    

def contenido_cajas_total(efectivos):
    for caja in efectivos:
        mostrador = caja[1:]
        suma = 0
        for lista in mostrador:
            suma = lista[0], lista[1]
            print(suma)
        print()    


print(efectivo_cajas(efectivo))
print(efectivo_cajas_total(efectivo))
print(contenido_cajas(efectivo))
print(contenido_cajas_total(efectivo))
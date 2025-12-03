# Programa en el que tenemos que modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
# para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género,
# adaptando el mensaje con 'don' o 'doña' dependiendo de este.

def mensaje_con_genero(tupla_personas):
    for nombre, genero in tupla_personas:
        if genero == "Masculino":
            titulo = "don"
        elif genero == "Femenino":
            titulo = "doña"
        else:
            titulo = "" 
        print(f"Estimado {titulo} {nombre}")


personas = (
    ("Manuel", "Masculino"),
    ("Sergio", "Masculino"),
    ("Alex", "Masculino"),
    ("María", "Femenino"),
    ("Pablo", "Masculino"),
    ("Lucía", "Femenino")
)

mensaje_con_genero(personas)
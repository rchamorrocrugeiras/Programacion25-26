# Reloj que actualiza su hora según lo que le diga el usuario

def main():
    hora = int(input("Introduce las horas: "))
    minuto = int(input("Introduce los minutos: "))
    segundo = int(input("Introduce los segundos: "))
    segundos_mas = int(input(f"Introduce los segundos que le quieres añadir a la hora ({hora}:{minuto}:{segundo}): "))

    while segundos_mas >= 60:
        minuto += 1
        segundos_mas -= 60

    while segundo + segundos_mas >= 60:
        segundo = segundo + segundos_mas - 60
        minuto += 1
        segundos_mas = 0  # ya se han sumado

    segundo += segundos_mas

    while minuto >= 60:
        minuto -= 60
        hora += 1

    print(f"La hora actual es: {hora}:{minuto}:{segundo}")

if __name__ == "__main__":
    main()

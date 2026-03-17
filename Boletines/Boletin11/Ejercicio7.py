import csv


def cargar_datos():
    ficheiro = "arquivo-euroestat.csv"
    try:
        # Usamos utf-8-sig para evitar problemas co carácter BOM
        with open(ficheiro, mode='r', encoding='utf-8-sig') as f:
            primeira_lina = f.readline()
            f.seek(0)
            delimitador = ';' if ';' in primeira_lina else ','

            reader = csv.DictReader(f, delimiter=delimitador)
            datos = []

            for row in reader:
                chaves = {str(k).strip(): v for k, v in row.items() if k is not None}

                geo = chaves.get('geo', chaves.get('GEO', ''))
                ano_str = chaves.get('TIME_PERIOD', chaves.get('time', chaves.get('TIME', '')))
                obs_str = chaves.get('OBS_VALUE', chaves.get('Value', chaves.get('OBS', '')))

                # Eliminamos a restrición de 2 letras, agora aceptamos calquera nome de país
                if geo and ano_str and obs_str:
                    try:
                        ano = int(ano_str)
                        # Ignoramos os valores que estean baleiros na columna OBS_VALUE
                        if obs_str.strip() == '':
                            continue

                        valor_limpo = obs_str.strip().replace(',', '.')
                        valor = float(valor_limpo)
                        # Gardamos o nome do país tal cal vén (ex. "Spain", "France")
                        datos.append({'geo': geo.strip(), 'ano': ano, 'valor': valor})
                    except ValueError:
                        pass

        if not datos:
            print("Aviso: O ficheiro leuse, pero non se atoparon datos válidos.")
        else:
            print(f"Datos cargados correctamente! Atopáronse {len(datos)} rexistros.\n")

        return datos

    except FileNotFoundError:
        print(f"Erro: Non se atopou o ficheiro '{ficheiro}'.")
        return []
    except Exception as e:
        print(f"Erro ao cargar os datos: {e}")
        return []


def mostrar_menu():
    print("=" * 60)
    print("   MENÚ DE ANÁLISE DE ENERXÍA RENOVABLE (EUROSTAT)")
    print("=" * 60)
    print("1. Produción total (suma da cota) de enerxía renovable por país.")
    print("2. Produción de enerxía renovable dun país nun ano.")
    print("3. País con maior crecemento porcentual (dende o primeiro ao último ano).")
    print("4. País con maior produción nun ano especificado.")
    print("5. Saír do programa.")
    print("=" * 60)


def main():
    datos = cargar_datos()
    if not datos:
        print("\nO programa vaise pechar porque non hai datos válidos para analizar.")
        return

    while True:
        mostrar_menu()
        opcion = input("Elixe unha opción (1-5): ").strip()

        match opcion:
            case '1':
                print("\n--- Produción total por país no período dispoñible ---")
                totais = {}
                for d in datos:
                    totais[d['geo']] = totais.get(d['geo'], 0) + d['valor']
                totais_ordenados = sorted(totais.items(), key=lambda x: x[1], reverse=True)
                print("País / Rexión                          | Suma Total da Cota (%)")
                print("-" * 65)
                for geo, total in totais_ordenados:
                    print(f"{geo:<38} | {total:.2f}")

            case '2':
                print("\n--- Produción dun país nun ano especificado ---")
                # Agora pedimos o nome completo, non o código
                pais = input("Introduce o nome do país (ex. Spain, France, Albania): ").strip()
                try:
                    ano = int(input("Introduce o ano (ex. 2020): "))
                    atopado = False
                    for d in datos:
                        # Comparamos ignorando maiúsculas/minúsculas para facilitar a busca
                        if d['geo'].lower() == pais.lower() and d['ano'] == ano:
                            print(f"\n=> A cota de enerxía renovable en {d['geo']} no ano {ano} foi do {d['valor']}%.")
                            atopado = True
                            break
                    if not atopado:
                        print(f"\n=> Non se atoparon datos para '{pais}' no ano {ano}.")
                except ValueError:
                    print("Erro: O ano debe ser un número enteiro.")

            case '3':
                print("\n--- País con maior crecemento porcentual ---")
                if datos:
                    ano_min = min(d['ano'] for d in datos)
                    ano_max = max(d['ano'] for d in datos)
                    print(f"Período analizado: {ano_min} - {ano_max}")
                    valores_min = {d['geo']: d['valor'] for d in datos if d['ano'] == ano_min}
                    valores_max = {d['geo']: d['valor'] for d in datos if d['ano'] == ano_max}
                    max_crecemento = -float('inf')
                    pais_max = None
                    val_inicial = 0
                    val_final = 0
                    for geo in valores_min:
                        if geo in valores_max:
                            v_min = valores_min[geo]
                            v_max = valores_max[geo]
                            if v_min > 0:
                                crecemento = ((v_max - v_min) / v_min) * 100
                                if crecemento > max_crecemento:
                                    max_crecemento = crecemento
                                    pais_max = geo
                                    val_inicial = v_min
                                    val_final = v_max
                    if pais_max:
                        print(
                            f"\n=> O país con maior crecemento foi {pais_max} cun crecemento do {max_crecemento:.2f}%")
                        print(f"   (Pasou do {val_inicial}% en {ano_min} ao {val_final}% en {ano_max}).")
                    else:
                        print("Non hai datos suficientes para comparar estes dous anos.")

            case '4':
                print("\n--- País con maior produción nun ano especificado ---")
                try:
                    ano = int(input("Introduce o ano para buscar (ex. 2021): "))
                    max_valor = -float('inf')
                    pais_max = None
                    for d in datos:
                        if d['ano'] == ano:
                            if d['valor'] > max_valor:
                                max_valor = d['valor']
                                pais_max = d['geo']
                    if pais_max:
                        print(
                            f"\n=> No ano {ano}, o país con maior cota de enerxía renovable foi {pais_max} cun {max_valor}%.")
                    else:
                        print(f"\n=> Non hai datos rexistrados para o ano {ano}.")
                except ValueError:
                    print("Erro: O ano debe ser un número enteiro.")

            case '5':
                print("\nSaíndo do programa... Ata logo!")
                break

            case _:
                print("\nErro: Opción non válida. Por favor, introduce un número do 1 ao 5.")


if __name__ == "__main__":
    main()
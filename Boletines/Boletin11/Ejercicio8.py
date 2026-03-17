import csv


def limpar_valor(valor_str):
    v = valor_str.strip()
    if not v or v == ':':
        return None
    num_str = ''.join(c for c in v if c.isdigit() or c == '.')
    try:
        return float(num_str)
    except ValueError:
        return None


def cargar_datos(ruta_ficheiro):
    datos = {}
    anos = []

    try:
        with open(ruta_ficheiro, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            headers = next(reader)
            anos = [h.strip() for h in headers[1:]]

            for row in reader:
                if not row: continue
                meta = row[0].split(',')
                if len(meta) < 3: continue

                unidade = meta[1]
                if unidade != 'PC_EMP':
                    continue

                pais = meta[2]
                if pais not in datos:
                    datos[pais] = {}

                for i, val in enumerate(row[1:]):
                    if i < len(anos):
                        ano = anos[i]
                        v = limpar_valor(val)
                        if v is not None:
                            datos[pais][ano] = v
    except FileNotFoundError:
        print(f"Erro: Non se atopou o ficheiro '{ruta_ficheiro}'.")
        exit()

    return datos, anos


def top_5_ano(datos, ano):
    ano_str = str(ano)
    valores = []

    for pais, valores_por_ano in datos.items():
        if ano_str in valores_por_ano:
            valores.append((pais, valores_por_ano[ano_str]))

    valores.sort(key=lambda x: x[1], reverse=True)

    print(f"\n--- TOP 5 PAÍSES CON MAIOR PORCENTAXE EN {ano} ---")
    if not valores:
        print("Non hai datos dispoñibles para ese ano.")
        return

    for i, (pais, valor) in enumerate(valores[:5], start=1):
        print(f"{i}. {pais}: {valor}%")


def maior_variacion(datos, ano1, ano2):
    ano1_str, ano2_str = str(ano1), str(ano2)
    maior_var = -1
    pais_maior = None
    var_real = 0

    for pais, valores_por_ano in datos.items():
        if ano1_str in valores_por_ano and ano2_str in valores_por_ano:
            val1 = valores_por_ano[ano1_str]
            val2 = valores_por_ano[ano2_str]
            var = abs(val2 - val1)

            if var > maior_var:
                maior_var = var
                pais_maior = pais
                var_real = val2 - val1

    print(f"\n--- MAIOR VARIACIÓN ENTRE {ano1} E {ano2} ---")
    if pais_maior:
        print(
            f"O país con maior variación foi {pais_maior} cunha diferencia de {var_real:+.2f}% (pasou de {datos[pais_maior][ano1_str]}% a {datos[pais_maior][ano2_str]}%)")
    else:
        print("Non hai suficientes datos cruzados para eses dous anos.")


def diferencia_con_espana(datos, pais, ano_inicio, ano_fin):
    print(f"\n--- DIFERENZA DE PORCENTAXE: {pais} vs ESPAÑA (ES) [{ano_inicio}-{ano_fin}] ---")

    atopáronse_datos = False
    for ano in range(int(ano_inicio), int(ano_fin) + 1):
        ano_str = str(ano)
        val_pais = datos.get(pais, {}).get(ano_str)
        val_es = datos.get('ES', {}).get(ano_str)

        if val_pais is not None and val_es is not None:
            diff = val_pais - val_es
            print(f"Ano {ano_str}: {pais} ({val_pais}%) | ES ({val_es}%) -> Diferenza: {diff:+.2f}%")
            atopáronse_datos = True
        else:
            print(f"Ano {ano_str}: Faltan datos para a comparativa.")

    if not atopáronse_datos:
        print("Non hai datos comúns suficientes no período solicitado.")


def grafica_periodos(datos, pais):
    if pais not in datos:
        print(f"\nErro: Non se atoparon datos para o país '{pais}'.")
        return

    periodos = [(2004, 2008), (2008, 2012), (2012, 2016), (2016, 2020), (2020, 2025)]

    print(f"\n--- GRÁFICA EVOLUTIVA POR PERÍODOS (4 ANOS) PARA {pais} ---")

    for inicio, fin in periodos:
        valores = []
        for a in range(inicio, fin):
            v = datos[pais].get(str(a))
            if v is not None:
                valores.append(v)

        if valores:
            media = sum(valores) / len(valores)
            media_redondeada = int(round(media))

            fin_etiqueta = 24 if fin == 2025 else fin
            label = f"{str(inicio)[-2:]}/{str(fin_etiqueta)[-2:]}"

            num_barras = int(media * 3)
            barras = "|" * num_barras

            print(f"{label}\t{barras}\t\t{media_redondeada}%")


if __name__ == "__main__":
    ficheiro = 'arquivo-euroestat.tsv'

    datos, anos = cargar_datos(ficheiro)

    if datos:
        top_5_ano(datos, 2023)
        maior_variacion(datos, 2010, 2023)
        diferencia_con_espana(datos, 'DE', 2015, 2020)
        grafica_periodos(datos, 'ES')
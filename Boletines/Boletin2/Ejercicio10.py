# Programa que calcula o soldo neto e bruto dunha persoa

soldo_fixo = float(input("Introduce o soldo fixo (€): "))
vendas = float(input("Introduce o importe total de vendas (€): "))
km = float(input("Introduce os km percorridos: "))
dias = int(input("Introduce os días de desprazamento: "))

comision = vendas * 0.05
quilometraxe = km * 2
dietas = dias * 30

soldo_bruto = soldo_fixo + comision + quilometraxe + dietas

irpf = soldo_bruto * 0.18
seguridade_social = 36

soldo_neto = soldo_bruto - irpf - seguridade_social

print(f"Soldo bruto: {soldo_bruto:.2f} €")
print(f"Soldo neto: {soldo_neto:.2f} €")

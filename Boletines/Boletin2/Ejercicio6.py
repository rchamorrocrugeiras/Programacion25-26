# Programa para calcular a porcentaxe de desconto dunha compra

prezo_tarifa = float(input("Introduce o prezo da tarifa (€): "))
prezo_pagado = float(input("Introduce o prezo pagado (€): "))

desconto = ((prezo_tarifa - prezo_pagado) / prezo_tarifa) * 100

print(f"A porcentaxe de desconto é do {desconto:.2f}%")

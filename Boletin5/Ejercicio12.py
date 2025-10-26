# 12. Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa e obteña o número deles
# que ganan entre 1000 e 1750 €, ámbolos dous incluídos e, a porcentaxe de traballadores que ganan menos de 1000 €.
# Tendo en conta que non se coñece con antelación o numero de traballadores da empresa e non se admiten os
# soldos negativos (utiliza como condición de fin un soldo 0).

pedir_n_trabajadores = int(input('Cuantos trabajadores tiene la empresa: '))

contador_1000_a_1750 = 0
contador_menos_de_1000 = 0
for i in range(pedir_n_trabajadores):
    saldo = int(input('Saldo: '))
    if saldo < 1000:
        contador_menos_de_1000 += 1
    if saldo >= 1000 and saldo <= 1750:
        contador_1000_a_1750 += 1
    if saldo < 0:
        print('Saldo negativo')

porcentaje_menos_de_1000 = (contador_menos_de_1000*100)/pedir_n_trabajadores
porcentaje_1000_a_1750 = (contador_1000_a_1750*100)/pedir_n_trabajadores

print('En la empresa hay ', porcentaje_menos_de_1000,
      '% empleados con un saldo inferior a 1000€')
print('En la empresa hay ', porcentaje_1000_a_1750,
      '% empleados con un saldo entre a 1000€ y 1750€')
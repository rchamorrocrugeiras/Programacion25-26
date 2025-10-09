def verificarFormatoData(data):
    verificaion = False
    data = data.strip()
    if len(data) == 10:
        if data[2] == '/' and data[5] == '/':
            dataSeparada = data.split('/')
            if len(dataSeparada[0]) == 2 and len(dataSeparada[1]) == 2 and len(dataSeparada[2]) == 4:
            # if len(data[0:2]) == 2 and len(data[3:5]) == 2 and len(data[6:10]) == 4:
                if dataSeparada[0].isdecimal() and dataSeparada[1].isdecimal() and dataSeparada[2].isdecimal():
                    verificaion = True
    return verificaion
#Verificamos se funciona
print (verificarFormatoData("02/05/2023"))
print (verificarFormatoData("22u05/2025"))
print (verificarFormatoData("22/05/20@3"))
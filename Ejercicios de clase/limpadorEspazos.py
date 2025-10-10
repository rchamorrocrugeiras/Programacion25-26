#quitar espacios ao final e ao principio de cadea

def limpadorCadeas(cadea):
    for c in cadea:
        if c ==' ':
            cadea = cadea[1:]
        else:
            break
    for i in range (len(cadea)-1, -1, -1):
        if cadea[i] ==' ':
            cadea = cadea[:i]
        else:
            break
    return cadea

limpa = limpadorCadeas('     Cadea sin espazos  ')
print ('   Cadea con espazos     ', '|')
print (limpa, '|')
# Programa que mostra por pantalla datos dunha persoa que máis pesa e a diferenza entre as dúas persoas

nome = "Paco Francisco"
nome2 = "Juan Antonio"
peso = 120
peso2 = 85

if peso > peso2:
    print (nome, "pesa", peso,"kg")
    resta = peso - peso2
    print ("A diferenza de peso entre eles é de:", resta,"kg")
elif peso < peso2:
    print (nome2, "pesa", peso2,"kg")
    resta2 = peso2 - peso
    print ("A diferenza de peso entre eles é de:", resta2,"kg")
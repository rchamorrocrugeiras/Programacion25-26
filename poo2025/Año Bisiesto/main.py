from data import Data

f1 = Data(29,2,2017)
f2 = Data(30,4,2021)
f3 = Data(29,2,2024)
f4 = Data(1,1,2000)
f5 = Data(30,2,2019)


print(f1.esValido())
print(f2.esValido())
print(f3.esValido())
print(f4.esValido())
print(f5.esValido())

f5.month = 15
print (f5.month)
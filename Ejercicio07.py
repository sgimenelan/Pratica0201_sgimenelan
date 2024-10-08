peso, estatura = -1, -1
while peso < 0 or estatura < 0:
    peso = float(input("Dime tu peso en Kg "))
    estatura = float(input("Dime tu estatura en metros "))
imc = (peso / estatura)
print ("Tu índice de masa corporal es ", round(imc, 2))
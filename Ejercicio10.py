payasos = int(input("Dime la cantidad de payasos "))
muñecas = int(input("Dime la cantidad de muñecas "))
peso_payasos = (payasos * 112)
peso_muñecas = (muñecas * 75)
peso_total = peso_muñecas + peso_payasos
n = 0
while peso_total > 1000:
    peso_total = (peso_total - 1000)
    n = n + 1
print("El peso del paquete es", n, "kg", peso_total, "g")
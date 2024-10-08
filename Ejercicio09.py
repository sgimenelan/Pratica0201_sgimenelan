a = input("¿Con que tipo de interes quieres invertir? (simple o compuesto) ")
a = a.lower()
capital = float(input("Cuanto es la capital que quieres invertir "))
interes = float(input("Cuanto es el interes anual "))
interes = (interes / 100)
años = int(input("¿Cuantos años quieres invertir? "))
if a == "simple":
    b = (capital * (1 + interes * años))
    print ("Tu capital final es ", round (b, 2),"€")
if a == "compuesto":
    b = (capital * (1 + interes)** años)
    print ("Tu capital final es ", round (b, 2),"€")
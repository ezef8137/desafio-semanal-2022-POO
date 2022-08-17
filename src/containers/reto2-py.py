sucesion= [1,1]

cantidad=int(input("Ingrese la cantidad de numeros de la serie fibonacci que desea: "))

operacion=0

for i in range(cantidad):
    operacion= sucesion[-1] + sucesion[-2]
    sucesion.append(operacion)

print(sucesion)
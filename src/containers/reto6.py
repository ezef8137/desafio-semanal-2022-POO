palabras=str(input("Ingrese una palabra: "))

lstpalabra=[]
lstnueva= list(palabras)


while len (lstnueva)> 0:
    lstpalabra.append(lstnueva[-1])
    lstnueva.pop()

palabraAlreves="".join(lstpalabra)
print(f"la palabra es: {palabraAlreves}")
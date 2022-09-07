caracter1=str(input("Ingrese una palabra: "))
caracter2=str(input("Ingrese otra palabra: "))


def palabras(caracter1,caracter2):
    listpalabra=[]
    salida1=caracter1.lower()
    salida2=caracter2.lower()
    
    
    for palabra in salida1:
        if palabra in salida2:
            listpalabra.append(palabra)

    for palabra in listpalabra:
        salida1=salida1.replace(palabra,"")
        salida2=salida2.replace(palabra,"")

    print(f"Para la expresion {caracter1} la salida es: {salida1}")
    print(f"Para la expresion {caracter2} la salida es {salida2}")



palabras(caracter1,caracter2)
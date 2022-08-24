def es_primo(numero1): 
    divisores = 0
    for i in range(1, numero1 + 1): 
        if numero1%i == 0: 
            divisores +=1
    if divisores > 2: 
        print("El número " + str(numero1) + " NO es primo")
    else: 
        print("El número " + str(numero1) + " SI es primo")


numero_usuario = int(input("Ingrese un número para saber si es primo: "))

es_primo(numero_usuario)

for i in range(2, 101): 
    es_primo(i)


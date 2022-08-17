for numero in range (1,101):
    if numero % 5==0 and numero % 3==0:
        print("fizzbuzz")
    elif numero % 5==0:
        print("buzz")
    elif numero % 3:
        print("fizz")
    else:
        print(numero)
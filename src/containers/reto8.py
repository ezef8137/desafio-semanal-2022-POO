def BinarioDec(num):
    suma=0
    i=0
    print("el binario",num)
    while (num>=1):
        div= num%10
        num= int(num/10)
        suma=suma+div*pow(2,i)
        i=i+1
    print("Le corresponde al numero",suma)

def decimal_a_binario(num):
    binario = 0
    multiplicador = 1

    while num != 0:
        binario = binario + num % 2 * multiplicador
        num = num // 2
        multiplicador = multiplicador * 10

    return binario


BinarioDec(111001)
print("El número 5 en binario es: ", decimal_a_binario(57))

function decimal_a_binario(num){
    binario = 0
    multiplicador = 1

    while (num != 0){
        binario = binario + num % 2 * multiplicador
        num = ~~(num/2)
        multiplicador = multiplicador * 10
    }
    return binario
}
console.log("El número 5 en binario es: ", decimal_a_binario(5))


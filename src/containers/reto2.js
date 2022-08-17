function fibonacci_iter(n){
    a = 1
    b = 1
    if (n == 1)
        console.log('0')
    else if(n == 2)
        console.log('0','1')
    else
        console.log('0')
        console.log(a)
        console.log(b)
        for (var n = 47; n > 0; n--) {
            total = a + b
            b = a
            a = total
            console.log(total);
         }
}
fibonacci_iter(50)
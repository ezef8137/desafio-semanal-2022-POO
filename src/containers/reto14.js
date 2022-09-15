class armstrong{
    constructor(numero){
        this.numero = numero;
    }

    separar(numero){
        this.numeros = [...this.numero+''].map(n=>+n)
        return this.numeros;
    }
    calculo(){
        this.separar()
        this.potencia = this.numeros.length;
        this.suma=0;
        this.tot=0;
        for (var valor of this.numeros){
            this.tot = Math.pow(valor, this.potencia)
            this.suma += this.tot;
            valor++;
        }
        return this.suma;
    }
    verificar(){
        this.separar()
        this.calculo()
        if (this.numero == this.suma){
            return "Es Número Armstrong"
        }
        else{
            return "No es numero Armstrong"
        }
    }

}
a = new armstrong(153)
b = new armstrong(152)
c = new armstrong(371)
d = new armstrong(13412)
console.log(a.verificar())
console.log(b.verificar())
console.log(c.verificar())
console.log(d.verificar())
let palabras = "HOLA hola que QUE tal"
palabras = palabras.toLowerCase().split(" ")
let diccionario_frecuencias = {}

cont = 0
for (palabra in palabras){
    if (palabras[palabra] in diccionario_frecuencias){
        diccionario_frecuencias[palabras[palabra]] += 1}
    else{
        diccionario_frecuencias[palabras[palabra]] = 1}
}
for (var palabra in diccionario_frecuencias){
    frecuencia = diccionario_frecuencias[palabra]
    console.log("La palabra", palabra, "se repite", frecuencia, "veces")}
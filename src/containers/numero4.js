function area(caracteristicas) {
    area_poligono=0
    if (caracteristicas[0]=="Triangulo") {
        area_poligono= caracteristicas[1] * caracteristicas[2]/2
    }

    if (caracteristicas[0]=="Rectangulo") {
        area_poligono = caracteristicas[1]*caracteristicas[2]
    }

    if (caracteristicas[0]=="Cuadrado") {
        area_poligono = caracteristicas[1]*caracteristicas[2]
    }

    return String(area_poligono)
}
console.log("El area del poligono es: "+area(["Triangulo",20,40]))
console.log("El area del poligono es: "+area(["Rectangulo",20,50]))
console.log("El area del poligono es: "+area(["Cuadrado",20,40]))
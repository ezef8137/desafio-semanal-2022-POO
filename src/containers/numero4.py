"""
triangulo = ["triangulo", base, altura]
rectangulo = ["rectangulo", lado1, lado2]
cuadrado = ["cuadrado", lado1, lado2]
"""

def area(caracteristicas): 
    area_poligono = 0
    if (caracteristicas[0] == "triangulo"): 
        area_poligono = caracteristicas[1]*caracteristicas[2]/2

    elif (caracteristicas[0]=="cuadrado"):
        area_poligono=caracteristicas[1]*caracteristicas[2]
    
    else: 
        area_poligono = caracteristicas[1]*caracteristicas[2]

    return str(area_poligono)


print("El area de este poligono es: " + area(["triangulo", 10, 20]))
print("El area del poligono es: "+area(["cuadrado",20,40]))
print("El area de este poligono es: " + area(["rectangulo", 15, 30]))
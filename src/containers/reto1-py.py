from ast import Return

palabra1=str(input("Ingrese la primera palabra: "))
palabra2=str(input("Ingrese la segunda palabra: "))

if palabra1== palabra2:
    print("Palabras igules no son anagramas")
else:
    def esAnagrama(): 
        return sorted (palabra1) == sorted(palabra2)

    print(esAnagrama())
Parentensis = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def Expresiones(Expresion: str):
    
    ListParentesis = []
    inverted_par = {value: key for key, value in Parentensis.items()}
    Equilibrada = True

    for letra in Expresion:
        
        if letra in Parentensis.keys():
            ListParentesis.append(letra)
        elif letra in Parentensis.values() and inverted_par[letra] == ListParentesis[-1]:
            ListParentesis.pop()
        elif letra in Parentensis.values():
            Equilibrada = False

    
    if len(ListParentesis) > 0:
        Equilibrada = False

    
    print(f"La expresion '{Expresion}' {'es' if Equilibrada else 'no es'} equilibrada")



Expresiones("{ [ a ( c + d ) ] - 5 }")
Expresiones("{ a ( c + d ) ] - 5 }")
Expresiones("{ [}(])")
Expresiones("{[()]}")
Expresiones("{[()]")

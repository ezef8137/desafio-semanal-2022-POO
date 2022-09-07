LetrasMorse = {
    "a": "·-",
    "b": "-···",
    "c": "-·-·",
    "d": "-··",
    "e": "·",
    "f": "··-·",
    "g": "--·",
    "h": "····",
    "i": "··",
    "j": "·---",
    "k": "-·-",
    "l": "·-··",
    "m": "--",
    "n": "-·",
    "ñ": "--·--",
    "o": "---",
    "p": "·--·",
    "q": "--·-",
    "r": "·-·",
    "s": "···",
    "t": "-",
    "u": "··-",
    "v": "···-",
    "w": "·--",
    "x": "-··-",
    "y": "-·--",
    "z": "--··",
    "0": "-----",
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
    ".": "·-·-·-",
    ",": "--··--",
    "?": "··--··",
    '"': "·-··-·",
    "/": "-··-·"
}


def Morse(natural_phrase: str):
    
    palabra_traducida = ""

    for letra in natural_phrase.lower():
        
        letra_morse = LetrasMorse.get(letra)
        
        if letra == " ":
            palabra_traducida += "  "
        
        elif letra_morse is None:
            palabra_traducida += "....--.....---..-...-.. "
        
        else:
            palabra_traducida += f"{letra_morse} "

    
    print(f"The phrase '{natural_phrase}' in morse is: '{palabra_traducida}'.")


def traduccion_textonatural(morse_phrase: str):

    palabraTraducida = ""
    latin_dict = {value: key for key, value in LetrasMorse.items()}
    
    for palabra in morse_phrase.split("   "):
        
        for letra_morse in palabra.split():
            
            latin_letter = latin_dict.get(letra_morse)
            
            if letra_morse == "....--.....---..-...-.." or latin_letter is None:
                palabraTraducida += "*"
            else:
                palabraTraducida += latin_letter

        
        palabraTraducida += " "
    print(f"El codigo morse '{morse_phrase}' en texto natural es: '{palabraTraducida}'.")


def traductor_morse(phrase: str):

    Morse = False
    
    for letter in phrase.lower().split():
        if letter in LetrasMorse.values():
            Morse = True

    if Morse:
        traduccion_textonatural(phrase)

    else:
        Morse(phrase.lower())


traductor_morse("hola mundo")
traductor_morse("programador")
traductor_morse("···· --- ·-·· ·-")
traductor_morse("-- --- ··- ·-· · -·· · ···-")

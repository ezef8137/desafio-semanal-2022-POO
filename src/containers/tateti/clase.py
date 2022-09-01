class Contador(object): 

    def __init__(self): 
        self.contador = 1

    def set_contador(self): 
        self.contador += 1

    def get_contador(self): 
        return self.contador
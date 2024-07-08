from Apartamento import Apartamento

class No:
    def __init__(self, apartamento):
        self.apartamento = apartamento
        self.proximo = None
    
    def __str__(self):
        return f"{self.apartamento}"
    
    def getNumero(self):
        return self.apartamento.getNumero()
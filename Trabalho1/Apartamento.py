from Torre import Torre

class Apartamento:
    def __init__(self, id, numero, torre) -> None:
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = None
    
    def getNumero(self):
        return self.numero
    
    def __str__(self):
        return f"ID: {self.id} - Nro do ap.: {self.numero} - Nome da torre: {self.torre.getNome()}"
    

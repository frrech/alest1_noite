from abc import ABC, abstractmethod

class Computador(ABC):

    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        if(preco > 0):
            self.preco = preco
        else:
            self.preco = 0
        
    
    @abstractmethod
    def cadastrar():
        pass

    def getInformacoes(self):
        return self.__str__()

    def __str__(self) -> str:
        return "Modelo: " + self.modelo + ", Cor: " + self.cor + ", Preço: " + str(self.preco)
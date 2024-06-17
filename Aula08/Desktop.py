from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potencia) -> None:
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potencia
        self.__id = 0

    def cadastrar(self, id):
        self.__id = id

    def getInformacoes(self):
        return self.__str__()
    
    def __str__(self) -> str:
        return "Id: " + str(self.__id) + ", " + super().__str__() + ", Potencia da fonte: " + str(self._potenciaDaFonte)
from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempodebateria) -> None:
        super().__init__(modelo, cor, preco)
        self.__tempodebateria = tempodebateria
        self.__id = 0

    def cadastrar(self, id):
        self.__id = id

    def getInformacoes(self):
        return "Id: " + str(self.__id) + ", " + super().__str__() + ", Tempo de bateria: " + str(self.__tempodebateria)
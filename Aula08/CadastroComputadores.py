class CadastroComputadores:
    def __init__(self) -> None:
        self.lista_comp = []
        self.__last_id = 0
    
    def addComputador(self, comp):
        self.lista_comp.append(comp)
        comp.cadastrar(self.__last_id)
        self.__last_id+=1
    
    def __str__(self) -> str:
        str = ""
        for x in self.lista_comp:
            str += x.getInformacoes() + "\n"
        return str
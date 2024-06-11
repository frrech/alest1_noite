from No import No

class Fila:
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho+=1
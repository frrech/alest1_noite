from Node import Node

class PilhaLivro:

    def __init__(self) -> None:
        self.topo = None
    
    def push(self, livro): #Adiciona elementos à pilha
        livro.proximo = self.topo
        self.topo = livro
        

    def pop(self): #Remove elementos à pilha
        if self.topo != None:
            self.topo = self.topo.proximo
        else:
            print("Lista vazia.")

    def peek(self):
        return self.topo

    def print(self):
        if self.topo != None:
            aux = self.topo
            while aux != None:
                print(aux)
                aux = aux.proximo
        else:
            print("Lista vazia")
    
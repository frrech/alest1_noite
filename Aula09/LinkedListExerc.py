from Node import Node

class LinkedList:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def add(self, valor):
        nodo = Node(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.proximo = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if nodo.dado < aux.dado:
                        nodo.proximo = ant.proximo
                        ant.proximo = nodo
                        break
                    else: #n achamos o espaço apropriado, indo p/ o proximo nodo
                        ant = aux
                        aux = aux.proximo
                if aux == None and nodo.dado >= ant.dado:
                    ant.proximo = nodo
        self.tamanho+=1
        self.imprimir()
    
    def remover(self, valor):
        tamInicial = self.tamanho
        if self.inicio != None:
            #Lista contém só um elemento e é igual ao valor
            if self.inicio.proximo == None and self.inicio.dado == valor:
                self.inicio == None
                self.tamanho = 0
            #Lista contém vários elementos e valor é igual o primeiro
            elif self.inicio.dado == valor:
                self.inicio = self.inicio.proximo
                self.tamanho-=1
            #Lista com vários elementos e o valor n é o primeiro
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if aux.dado == valor:
                        ant.proximo = aux.proximo
                        self.tamanho-=1
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
        if tamInicial == self.tamanho:
            print("Valor n encontrado")
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")
            aux = self.inicio

            while aux:
                print(aux.dado, "\n")
                aux = aux.proximo
            print("Tamanho da lista" + str(self.tamanho))
    

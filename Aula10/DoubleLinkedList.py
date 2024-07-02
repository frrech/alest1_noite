#Construa o algoritmo em Python de uma lista duplamente encadeada 
#que possui uma função para inserir elementos em ordem alfabética, 
#uma função para imprimir os elementos da lista e uma função para 
#imprimir os elementos na ordem inversa. 

from Node import Node

class DoubleLinkedList:
    def __init__(self):
        self.inicio = None
        self.cauda = None
        self.tamanho = 0
    
    def adicionar(self, valor):
        if valor != None:
            no = Node(valor)
            if tamanho == 0:
                self.inicio = no
                self.cauda = no
            else:
                aux = self.inicio.proximo
                ant = aux.anterior
                while aux.proximo:
                    if aux.dado > no.dado:
                        if ant != self.inicio:
                            ant.proximo = no.dado
                            no.proximo = aux
                            aux.anterior = no.dado
                            no.anterior = ant
                        else:
                            no.proximo = ant
                            ant.anterior = no
                            self.inicio = no
                    else:
                        if aux != self.cauda:
                            ant = aux
                            aux = aux.proximo
                        else:
                            no.anterior = aux
                            aux.proximo = no
                            self.cauda = no
            tamanho+=1
        else:
            print("Valor é None")
    
    def remover(self):
        pass

    def imprimir(self):
        aux = self.inicio
        while aux.proximo:
            print(aux)
            aux = aux.proximo
    
    def imprimir_reverso(self):
        aux = self.cauda
        while aux.anterior:
            print(aux)
            aux = aux.anterior
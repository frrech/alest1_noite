from No import No

class Fila_espera:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def add(self, apartamento):
        no = No(apartamento)
        if self.inicio == None:
            self.inicio = nodo
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho+=1
    
    def pop(self):
        if self.inicio:
            self.inicio = self.inicio.proximo
            if self.inicio == None:
                self.fim = None
            self.tamanho -= 1
    
    def imprimir(self):
        if self.inicio != None:
            aux = self.inicio
            i = 1
            while aux:
                print(i + " - " + aux)
                aux = aux.proximo
                i+=1
        else:
            print("Fila vazia")
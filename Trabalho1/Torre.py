class Torre:
    def __init__(self, id, nome, endereco) -> None:
        self.id = id
        self.nome = nome
        self.endereco = endereco
    
    def cadastrar(self, id):
        nome = input("Digite o nome da torre: ")
        endereco = input("Digite o endereco da torre: ")
        if id != None and nome != "" and endereco != "":
            self.id = id
            self.nome = nome
            self.endereco = endereco
        else:
            print("Campo de nome ou endereço foram deixados vazios.")

    def imprimir(self):
        print("ID da torre: ", self.id,"; Nome da torre: ", self.nome, "; Endereço:", self.endereco)

class Pessoa:

    def __init__(self, nome, idade=18):
        self.nome = nome
        self.idade = idade
        print("pessoa: ", self.nome, "construída") 

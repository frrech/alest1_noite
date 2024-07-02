class Torre:
    def __init__(self, id, nome, endereco) -> None:
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def __str__(self):
        return "ID da torre: "+ str(self.id)+" - Nome da torre: "+ self.nome+ " - Endereço: "+ self.endereco
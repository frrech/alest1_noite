from Aluno import Aluno
class AlunoEnsinoMedio:
    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(self, codigo, nome, matricula)
        self.ano = ano
    
    def toStr(self):
        return "Nome: " + self.nome + "\nAno: " + self.ano + "\nCódigo: " +\
        self.codigo + "\nMatrícula: " + self.matricula

    def imprimir(self):
        print(self.toStr())

from Aluno import Aluno
class AlunoEnsinoMedio:
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(self, codigo, nome, matricula)
        self.semestre = semestre
    
    def toStr(self):
        return "Nome: " + self.nome + "\nSemestre: " + self.semestre + "\nCódigo: " +\
        self.codigo + "\nMatrícula: " + self.matricula

    def imprimir(self):
        print(self.toStr())

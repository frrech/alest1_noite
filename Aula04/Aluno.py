class Aluno:
        def __init__(self, codigo, nome, matricula):
            self.codigo = codigo
            self.nome = nome
            self.matricula = matricula
        
        def toStr(self):
            return "Nome: " + self.nome + "\nCódigo: " +\
            self.codigo + "\nMatrícula: " + self.matricula

        def imprimir(self):
            print(self.toStr())


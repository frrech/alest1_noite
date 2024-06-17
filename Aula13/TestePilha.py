from PilhaLivro import PilhaLivro
from Node import Node
pilha = PilhaLivro()
while True:
    s = int(input("0 = push livro\n1 = pop livro\n2 = print pilha\n3 = sai"))
    if s == 0:
        #push livro
        titulo = input("Titulo do livro: ")
        autor = input("Autor do livro: ")
        paginas = input("Nro paginas do livro: ")
        pilha.push(Node(titulo, autor, paginas, pilha.peek()))
        pass
    elif s == 1:
        #pop pilha
        pilha.pop()
        pass
    elif s == 2:
        #print pilha
        pilha.print()
    elif s == 3:
        break

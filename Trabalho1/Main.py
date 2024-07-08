from Fila_espera import Fila_espera
from Apartamento import Apartamento
from Torre import Torre
def main():
    ## Fila de espera de vagas
    fila_espera = Fila_espera()
    ## Inteiro com nro de vagas
    nro_vagas = 3
    ## Lista encadeada (vagas de estacionamento)
    lista_vagas = LinkedList()
    ##MENU:
    while True:
        entrada = input("A) Add ap\nB) Remove ap\nC)Print occupied spots\nD)Print waitlist\nE)Exit")
    ## A) Cadastrar apartamento
        if entrada == "a":
            cadastarAp()
    ## B) Liberar vaga
        elif entrada == "b":
            removeAp()
    ## C) Imprimir lista de aps com vaga
        elif entrada == "c":
            print(lista_vagas)
    ## D) Imprimir lista de espera
        elif entrada == "d":
            print(fila_espera)


if __name__ == "__main__":
    main()


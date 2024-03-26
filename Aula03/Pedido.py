from Pessoa import Pessoa
from Produto import Produto


class Pedido:
    def __init__(self, id=0, end="Rua dos Bobos, 0", produtos=[], cliente=Pessoa("Fulano"), quantidades=[]) -> None:
        self.id = id
        self.end = end
        self.produtos = produtos
        self.quantidades = quantidades
        self.cliente = cliente

    def addProduto(self, p, qtd):
        p.venderProduto()
        self.produtos.append(p)
        self.quantidades.append(qtd)
        return sum(map(subtotal, self.produtos, self.quantidades))


def subtotal(m, n):
    return m.preco * n

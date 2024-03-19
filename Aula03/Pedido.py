from Pessoa import Pessoa
from Produto import Produto
class Pedido:
    def __init__(self, id = 0, end = "Rua dos Bobos, 0", produtos = [], cliente = Pessoa("Fulano")) -> None:
        self.id = id
        self.end = end
        self.produtos = produtos
        self.cliente = cliente

    def addProduto(self, p, qtd):
        p.venderProduto()
        self.produtos.append((p,qtd))
        return subtotal()

    def subtotal(self):
        pass

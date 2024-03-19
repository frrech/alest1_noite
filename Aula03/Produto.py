from Categoria import Categoria
class Produto:
    def __init__(self, nome = "Banana", preco = 6.0, qtd = 12, cat = Categoria(0, "Fruta")):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.cat = cat
    
    def venderProduto(self, qtdVendida):
        if qtdVendida > self.qtd:
            print("Quantidade maior do que a em estoque!")
        else:
            self.qtd -= qtdVendida
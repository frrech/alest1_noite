from Cidade import Cidade
from Pessoa import Pessoa

c1 = Cidade()
c2 = Cidade(nome = "Porto Alegre")
c3 = Cidade(1, "Capão da Canoa")

print(c1)
print(c2)
print(c3)

p1 = Pessoa("João")
p2 = Pessoa("Maria", 20)
p3 = Pessoa("José", 25, c1)
p4 = Pessoa("José", cid = c2)
p5 = Pessoa("Julia", idade = 30)


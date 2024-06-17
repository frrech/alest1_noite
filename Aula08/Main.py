from Desktop import Desktop
from Notebook import Notebook
from CadastroComputadores import CadastroComputadores

cc = CadastroComputadores()

d1 = Desktop("Dell", "Preto", 3000.0, 400)
d2 = Desktop("Lenovo", "Preto", 2500.0, 300)
n1 = Notebook("Dell", "Prata", 4500.0, 60)
n2 = Notebook("Apple", "Branco", 8000.0, 60)

cc.addComputador(d1)
cc.addComputador(d2)
cc.addComputador(n1)
cc.addComputador(n2)

print(cc)
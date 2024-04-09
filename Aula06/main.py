from Conta import Conta

c = Conta()
print(c.getSaldo())
c.saldo = 90
c.setSaldo(90)
print(c.getSaldo())
c.depositar(5)
print(c.getSaldo())
c.sacar(2)
print(c.getSaldo())
c.setSaldo(100)
print(c.getSaldo())
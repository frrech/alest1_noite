class Conta:
    tarifa = 1.99
    logado = True
    def __init__(self):
        self.__saldo = 0

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else:
            print("Ação não permitida")
            return None
    
    def setSaldo(self, saldo):
        if self.logado and saldo > 0:
            self.__saldo = saldo
        else:
            print("Ação não permitida")
    
    def __descontarTarifa(self):
        self.__saldo -= self.tarifa
    
    def depositar(self, valor):
        if self.__saldo + valor >= self.tarifa:
            self.__saldo += valor
            self.__descontarTarifa()
        else:
            print("Saldo insuficiente")
    
    def sacar(self, valor):
        if self.__saldo - valor >= self.tarifa:
            self.__saldo -= valor
            self.__descontarTarifa()
        else:
            print("Saldo insuficiente")
class ContaBancaria():
    def __init__(self, saldo) -> None:
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            raise Exception("Saldo insuficiente")
    
    def extrato(self):
        print(f"Saldo: R${self.saldo:.2f}")
    

conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(200)
conta.extrato()
conta.sacar(1400)
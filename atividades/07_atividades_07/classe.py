class Conta:
    def __init__(self,titular,cpf,agencia,n_conta,saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.n_conta = n_conta
        self.saldo = saldo
    
    def consultar_dados(self):
        print(f"Nome do titular da conta:{self.titular}")
        print(f"cpf do titular da conta:{self.cpf}")
        print(f"Agência da conta:{self.agencia}")
        print(f"Numero da conta:{self.n_conta}")
        print(f"saldo da conta:R${self.saldo:.2f}")


    def depositar(self,valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo 
        else:
            return"saque nao permitido."
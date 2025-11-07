class Conta:
    def __init__(self, titular,cpf,agencia,numerodaconta,saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.numerodaconta = numerodaconta
        self.saldo = saldo

    def consultar_dados(self):
        print(f"nome: {self.nome}")
        print(f"cpf:{self.cpf}")
        print(f"agencia:{self.agencia}")
        print(f"numero da conta:{self.numerodaconta}")
        print(f"saldo:{self.saldo}")
    
    def depositar_valor(self,valor):
        self.saldo += valor
        return self.saldo
    
    def sacar_valor(self,valor):
        self.saldo -= valor
        return self.saldo

def main():
    conta = Conta(titular="",cpf="",agencia="",numerodaconta="",saldo="")




# classes
Class pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone = telefone
        def exibir_dados(self)
            print(f"e-mail:{self.telefone}")
            print(f"telefone:{self.email}")



Class pessoafisica(pessoa):
    def __init__(self,nome, cpf, idade, telefone,email):
        self.email =email
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email =email, telefone=telefone)
    
    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"cpf: {self.cpf}")
        print(f"idade: {self.idade}")
        super().exibir_dados()

Class pessoauridica(pessoa):
    def __init__(self,nome_fantasia, cnpj, telefone,email):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(emaimail=email, telefone=telefone)
    
    def exibir_dados(self):
        print(f"nome da empresa: {self.nome_fantasia}")
        print(f"cnpj: {self.cnpj}")
        super().exibir_dados()


             

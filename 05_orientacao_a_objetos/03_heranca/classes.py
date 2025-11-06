# classes
class pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone = telefone
        
class pessoafisica(pessoa):
    def __init__(self,nome, cpf, idade, telefone,email):
        self.email =email
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email =email, telefone=telefone)

        class pessoauridica(pessoa):
            def __init__(self,nome_fantasia, cnpj, telefone,email):
                self.nome_fantasia = nome_fantasia
                self.cnpj = cnpj
                super().__init__(emaimail=email, telefone=telefone)
                

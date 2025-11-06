# classe
class pessoa:

    #construtor 
    def __init__(self, nome, idade, email, cpf):
        self.nome=nome
        self.cpf =cpf
        self.email =email
        self.idade =idade
        
        def exibir_dados(self):
            print(f"nome: {self.nome}")
            print(f"idade: {self.idade} anos")
            print(f"email: {self.email}")
            print(f"cpf: {self.cpf}")

# algarismo principal
if __name__ == "__main__":

    # isntacia de classe
    usuario = pessoa(nome="",cpf="",email="",idade=0)


# entrada de dados 
usuario.name = input("informe o nome:").strip().title()
usuario.cpf = input("informe o cpf:").strip()
usuario.email = input("informe o email:").strip().lower()
usuario.idade = input("informe a idade:").strip()


# saida de dados 
usuario.exibir_dados()




# classes
class pesssoa:
    

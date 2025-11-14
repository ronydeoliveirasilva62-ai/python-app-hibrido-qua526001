from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str

    def __str__(self):
        return f"Email: {self.email}\nTelefone: {self.telefone}\nEndereco: {self.endereco}"
    
@dataclass
class PessoaFisica(Pessoa):
    nome: str
    idade: str
    cpf: str
    profissao: str

    def __str__(self):
        return f"\nDados do usuario:\nNome {self.nome}\nIdade: {len(self)}\nCpf: {self.cpf}\nProfissao: {self.profissao}\n{super().__str__()}"
    
    def __len__(self):
        return self.idade
    
@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str

    def __str__(self):
        return f"\nDados da Empresa: \nNome da Empresa: {self.nome_fantasia}\ncnpj:{self.cnpj}\nWebsite: {self.website}\n{super().__str__()}"
    


from dataclasses import dataclass

@dataclass
class Pessoa:

    nome: str
    idade: int
    altura: float

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {len(self)}\nAltura: {self.altura}"
    
    def __len__(self):
        return self.idade
    
    def verificar_maioridade(self):
        return "e maior de idade" if len(self)>= 18 else "e menor de idade"
    
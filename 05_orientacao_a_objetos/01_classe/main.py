#  biblioteca
import os

# classe
class pessoa:
    # atributos
    nome = "Rony"
    idade = 50
    email = "rony@r.com"

    # metodos
    def exibir_dados(self):
        print(f"nome: {self.name}")
        print(f"idade: {self.idade}")
        print(f"email: {self.email}")

if __name__ == "__main__":
    
    #instancia a classe (cria nono objeto)
    usuario = pessoa()
    
    os.system("cls")

    # limpa console
    os.system("cls" if os.name == "nt" else "clear")

    # chama o metodo
    usuario.exibir_dados()

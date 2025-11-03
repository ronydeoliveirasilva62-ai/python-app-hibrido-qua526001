# biblioteca

import os


def boas_vindas(nome):
    print(f"seja bem vindo, {nome}😁")
   

# algaritmo principal
os.system("cls")
nome = input("informe seu nome:").strip().title()
boas_vindas(nome)

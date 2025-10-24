import os
# recebe informaçao
nome = input("digite seu nome: ").strip() .ttile() # string
email = input("digite seu e_mail: ").strip().lower() # string
cpf = input("seu cpf: ").strip() # string
telefone = input("seu telefone: ").strip() # string

os.system("cls")
# mostra a informaçao
print(f"nome: {nome}")
print(f"email: {email}")
print(f"telefone: {telefone}")
print(f"cpf: {cpf}")

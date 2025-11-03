# biblioteca
import os

# funcao
def boas_vidas(nome):
    os.system("cls")
    return f"seja bem vidos,{nome}!😜"

# algarismo principal
os.system("cls")
nome = input("informe seu nome:").strip().title()
resultado = boas_vidas(nome)
print(resultado)
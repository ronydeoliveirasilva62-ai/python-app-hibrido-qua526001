#bibliotecas
import os

# declaracao de lista

usuarios=[]

# limpa console
os.system("cls") 

while True:
    # menu
    print("1 -cadastrar usuario:")
    print("2 - listar usuarios:")
    print("3 - sair do programa:")
    opcao =input("informe a opcao desejada:").strip()
    match opcao:
        case"1":
            usuario ={}
            usuario['nome'] =input("informe o nome do usuario:").strip().title()
            usuario['idade']=int(input("informe a idade do usuario:").strip())
            usuario['email']=input("informe o e-mail do usuario:").strip().lower()
            usuarios.append(usuario)
            os.system("cls")
            print("novo usuario isnserido com sucesso")
            continue
        case"2":
            for usuarios in usuario:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario[chave]}")
                print(f"{'-'*40}")
            continue
        case "3":
            break
        case _:
            print("opcao invalida")
            continue
        



     
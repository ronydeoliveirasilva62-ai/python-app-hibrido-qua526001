# biblioteca
import os


# declaracao de lista
nomes = []
os.system("cls")
# loop
while True:
    # menu
    print("1 - insira novo nome")
    print("2 - exibir lista de nomes")
    print("3 - excluir nome da lista")
    print("4 - sair do programa")
    opcao = input("informe a opçao desejada: ").strip()
    match opcao:
        case "1":
            novo_nome = input("informe novo nome:").strip().title()
            nomes.append(novo_nome) # insire novo nome na lista
            os.system("cls")
        case "2":
            os.system("cls")
            print("lista de nomes\n")
            for i in range(len(nomes)):
                print(f"{i} - {nomes[i]}")
                print(f"\n{'_'*40}\n")
            continue
        case "3":
            os.system("cls")
            try:
                posicao = int(input("informe a posicao a ser escluida:")).strip()
                if posicao >= 0 and posicao < len(nomes):
                    del(nomes[posicao])
                    print("nome excluido com sucesso.")
                pass
            except Exception as e:
                print(f"posicao ivalida.{e}.")
                continue
        case "4":
            print("programa encerrado.")
            break
        
        case _:
            print("opçao invalida")

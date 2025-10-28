# declaracao de lista

nomes = []
try:
    while True:
        print("1 -inserir nome na lista")
        print("2 - exibir lista")
        print("3 - sair do programa")


        match opcao:
            case "1":
                novo_nome = input("informe novo nome")
            case "2":
                print("\nlista de nomes\n")
                for nome in nomes:
                    print(nome)
            case "3":
                break
            case _:
                print("opcao invalida.")
                continue
except exception as e:
    print(f"erro ao ezibir a lisata.{e}.")
# declaracao de dicionario
veiculo ={"fabricante":"chevrolet",
"modelo":"chevrolette",
"ano":1973,
"cor":"branco",
"placa": "df-1973",}

# exibe os dados
for chave in veiculo:
    print(f"{chave.capitalize()}:{veiculo[chave]}")


    #usuario escolhe o campo que deseja mudar
    while True:
        campo =input("informe o nome do campo que desejada  alterar ou digite 'sair' para encerrar o programa:").strip().lower()
        match campo:
            case "fabricante":
                veiculo['fabricante'] = input("informe o novo valor de fabricante'").strip()
                
            case "modelo":
                veiculo['modelo'] = input("informe o novo valor de modelo'")
                
            case "ano":
                veiculo['ano'] = int(input("informe o novo valor do 'ano':").strip())
            case "cor":
                [cor] = input("infome o novo valor da 'cor'").strip()

        
            case "placa":
                veiculo= ['palaca'] input("informe o novo valor da 'placa'").strip()
            case "sair":
                 break
            case _:
                print("valor invalido")
              continue
    
    #mostra na tela os novos valores
    for chave in veiculo:
        print(f"{}")

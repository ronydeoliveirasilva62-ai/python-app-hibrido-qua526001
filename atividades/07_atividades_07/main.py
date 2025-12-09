import os

from classe import Conta

def limpar():
    os.system("cls"if os.name == "nt" else "clear")
def main():
    limpar()

    cc = Conta(titular="",cpf="",agencia="1234-5",n_conta="12345-6",saldo=0)

    cc.titular = input("informe o nome do titular:").strip().title()
    cc.cpf = input("informe o cpf do titular:").strip()

    limpar()
    while True:
        print("1 - consultar dados")
        print("2 - depositar valor")
        print("3 - sacar valor")
        print("4 - sair do programa")
        opcao =input("opcao desejada:").strip()

        match opcao:
            case "1":
                cc.consultar_dados()
                continue
            case "2":
                valor = float(input("informe o valor do deposito:R$").strip().replace("," , ","))
                print(f"deposito realizado com sucesso.saldo atual:R${cc.depositar(valor):.2f}")
                continue
            case "3":
                valor = float(input("informe o valor do saque:R$").strip().replace(", "," ,"))
                print(f"valor sacado:R${cc.sacar(valor)}")
                continue     
            case "4":
                print("programa encerrado")
                break

            case _:
                print("opcao invalida")
                continue
    



if __name__ == "__main__":
    main()
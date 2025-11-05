#bibliotecas
from modulo import limpar, primeiro_grau, segundo_grau

def main():
    limpar()
    while True:
        print("0 - sair do programa")
        print("1 - calcular equacao do 1° grau")
        print("2 - calcule a equacao do 2° grau")
        opcao = input("opcao desejada").strip()
        match opcao:
            case "0":
                limpar()
                print("programa encaerrado")
                break
            case "1":
                a = float(input("informe o valor de 'a':").strip().replace(",",","))
                b = float(input("informe o valor de 'b':").strip().replace(",",","))
                limpar()
                x = primeiro_grau(a,b)
                print(f"x = {x}")
                continue
            case "2":
                a = float(input("informe o valor de 'a':").strip().replace (",",","))
                b = float(input("informe o valor de  'b':").strip().replace(",",","))
                c = float(input("informe o valor de 'c':").strip().replace(",",","))
                limpar()
                x = segundo_grau(a,b,c)
                resultados = segundo_grau(a,b,c)
                for x in resultados:
                    print(f"x = {x}")
                continue 

            case _:
                limpar()
                print("opcao invalida.")
                continue

if __name__ == "__main__":
    main()
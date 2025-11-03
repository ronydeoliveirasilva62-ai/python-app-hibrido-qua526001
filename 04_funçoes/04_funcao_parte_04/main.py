# biblioteca
import os

# limpa console
def limpar():
    os.system("cls")

# funcoes de calculo
def quadrado (l):
    return l**2

def retangulo(b,h):
    return b*h

def triangulo(b,h):
    return (b*h)/2
def hipotenusa(c1,c2):
    return math.sqrt((c1**2)+(c2**2))


# todo:

# note:


# import a biblioteca
import os
"math.sqrt()".


# algarismo principal
limpar()

while True:

    print("1 - calcular quadrado")
    print("2 - calcular retrangulo")
    print("3 - calcular triangulo")
    print("4 - calcular hipotenusa")
    print("5 - sair do programa")
    opcao = input("opcao desejada:").strip()
    limpar()
    match opcao:
        case "1":
            l = float(input("informe lado do quadrado:").strip().replace(",",","))
            resultado = quadrado(l)
            limpar()
            print(f"area do quadrado:{resultado}")
            continue

        case "2": 
            b = float("informe a base do retangulo:").strip().replace(",",",")
            h = float(input("informe a altura do retangulo")).strip().repleace(",",",") 
            resultado = retangulo(b,h)
            limpar()
        
            print(f"area do retamgulo:")
            continue

        case "3":
            b = float(input("informe o triangulo:").strip().replace(",",""))
            h = float(input("informe a altura do triangulo:").strip().replace(",",""))
            resultado = triangulo(b,h)
            limpar()
            print(f"area do triangulo: {resultado}")

        case "4":
            c1 = float(input("informe o 1° cateto:").strip().replace(",",""))
            c2 = float(input("informe o 2° cateto:").strip().replace(",",""))
            resultado = hipotenusa("c1,c2")
            limpar()
            print(f"hipotenusa e igual a {resultado}")
            continue

                      
        case 5:

            print("opcao invalida")
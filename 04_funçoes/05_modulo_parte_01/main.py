# import as funcoes
import modulo as m

m.limpar()
while True:
    print("1 - calcular quadrado")
    print("2 - calcular retangulo")
    print ("3 - calcular triangulo")
    print("4 - calcular circulo")
    print("5 - calcular trapezio")
    print("6 - sair do programa")
    opcao = input("opcao desejada").strip()
    match opcao:
        case "1":
            l = float(input("informe o quadrado").strip().replace(",",""))
            m.limpar()
            area = m.quadrado(l)
            print(f"area do quadrado:{area}")
            continue
        case "2":
            b = float(input("informe a area do retangulo").strip().replace(",",""))
            h = float(input("informe a altura do retangulo".strip().replace(',",","')))
            m.limpar()
            print(f"area do retangulo:{area}")
            continue
        case "3":
            b = float(input("informe a base do triangulo").strip().replace(",",","))
            h = float(input("informe a altura do triangulo:").strip().replace(",",","))
            m.limpar()
            area = m.triangulo(b,h)
            print(f"area do triangulo:{area}")
            continue
        case "4":
            r = float(input("informe o raio do circulo".strip().replace(",",",")))
            m.limpar()
            area = m.circulo(r)
            print(f"area do circulo:{area}")
            continue
        case"5":
            b = float(input("informe a base do trapezio:").strip().repalce(",","."))
            b = float(input("informe da base maio do trapezio:").strip().replace(",",","))
            h = float(input("informe a atura do trapezio:").strip().replace(",",","))
            m.limpar()
            area = m.trapezio(b,B,h)
            print(f"area do trapeziio:{area}")
            continue
        case "6":
            break
            opcao = invalida
            print("opcao invalida")
            continue
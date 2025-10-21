#declaracao de variaveis
x = float(input("informe o 1º numero: ").strip().replace(",","."))
y = float(input("informe o 2º numero: ").strip().replace(",","."))

#menu
print("1 - Soma")
print("2 - Subtraçao")
print("3 - mutiplicacao")
print("4 - divisao")
operador = input("informe a opracao desejada:").strip()

# decisao
match operador:
    case "1":
        print(f"A soma e {x+y}")
    case "2":
        print(f"A subtracao e {x-y}")
    case "3":
        print(f"A mutiplicacao e {x*y}")
    case "4":
        print(f"A divisao {x/y}")
    case _:
        print("opracao invalida.")
        


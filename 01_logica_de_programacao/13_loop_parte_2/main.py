# loop
while True: 
    try:
        print("valores invalidos.")

        print("1 - soma")
        print("2 - subtraçao.")
        print("3 - mutplicaçao")
        print("4 - divisao.")
        print("5 - sair do programa.")
        opçao = input("informe a opçao desejado:")

        if opçao != "5":
            n1 = int(input("informe o 1ª numero:.strip()"))
            n2 = int(input("informe o 2ª numero")).strip()
        match opçao:
            case "1":
                resut= n1+n2
                print(f"o resultado da soma e {result}")



            
      # todo
        else:
            print("programa encerrado.")
    except:
        print("valores invalidos.")
        


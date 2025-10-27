# todo: atividade

# trataemnto de dados
try: 
    nome = input("informe nome:")
    idade = int(input("informe sua idade:"))

    #lista de filmes 
    sala_1 ="a roda quadrada"
    sala_2 = "a volta dos qum nao foram"
    sala_3 ="poeira em alto mar"
    sala_4 = "as tanças do rei careca"
    sala_5 = "a vingança do frango assacino"

    # menu de filmes
    print(f"sala 1 - {sala_1} - livre")
    print (f"sala_2 -  {sala_2} - 12anos")
    print (f"sala_3 - {sala_3} -13 anos") 
    print (f"sala_4 - {sala_4} -16 anos")
    print (f"sala_5 - {sala_5} - 18 anos")
    sala = input("informe a sala desejada:").strip()

    # verifica a sala selecionada
    match sala:
        case "1":
            filme = sala_1
            idade_minima= 0
        case "2":
            filme = sala_2
            idade_minima = 12
        case "3":
            idade_minima = 14
            filme=sala_3
        case "4":
            filme = sala_4
            idade_minima = 16
        case "5":
            filme = sala_5
            
            idade_minima = 18
        case _ :
            

except Exception as e:
    print(f"erro de program.{e}")

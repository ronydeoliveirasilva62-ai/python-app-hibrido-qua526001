# entrada de dados 
aluno = input("informe o nome do aluno").strip().title()
nota = float(input("informa a nota:").strip().replece(",",","))

# verifica a nota do aluno
if nota >= 0 and nota <= 10:
    if nota>= 7:
        print(f"{aluno}esta aprovado.")
    elif nota >= 5:
        print(f"{aluno}esta recuperacao.")
    else:
        print(f"{aluno} esta reprovado.")
else:
    print(f"nota do {aluno} invalida")





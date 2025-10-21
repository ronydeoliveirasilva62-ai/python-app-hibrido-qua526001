#declaracao de variaveis
nome = input("informe o nome: ").strip().title()
idade = int("informe a idade:").strip()
altura = float(input("informe a altura: ").strip().replace(".",","))

# verificacao das condicoes
if idade >= 12 and altura >=1.15:
    print(f"entrada de {nome} autorizada.")
else:
    print(f"entrada de {nome} nao autorizada.")

# funcao principal
def main():

    # entrada de dados
    nome = input("informe o seu nome:").strip().title()
    idade = int("informe a sua idade:").strip()

    # operador tenario 
    resultado = "e maior de idade." if idade >= 18 else "e menor de idade."

    # saidade de dados 
    print(f"{nome}{resultado}")

# protege algarismo principal
if __name__== "__main__":
    main()
# todo: atividade
#tratamento de exceçao
try:
    # entrada de dados

    nome = input("informe o nome:").strip().title()
    peso = float (input("informe o peso em kg:").strip().replace()
    altura = float (input("informe a altura em metros:").strip().replace(",",",")
                    
    # calculo do imc
    imc= peso/(altura**2)

    # exibe o imc do usuario
        print(f"{nome}, seu imce {:.2f}")

    # diagnostico do imc
    elif inc < 25:
        print(f"{nome} esta no peso ideal.") 
    elif imc < 30:
        print(f"{nome} esta acima do peso.")
    elif imc < 35:
        print(f{nome} esta obeso.")
    elif imc < 40:
    print(f"{nome}esta obesidade m") 
          

except Exception as e:

printule(f"deu ruim! {e}")



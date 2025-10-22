# ratamento de exececao
try:

    # entrada de dados 
    numero = int(input("informe o numerointeiro:")).strip()

    # laço de repertiçao 
    while numero >= 0:
        print(numero)
        numero-= 1 
except:
    print("nao foi possivel executar o conputador.")



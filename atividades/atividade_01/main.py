# limpar o terminal (limpa)
import os
import time
numero = int( input("digite o numero: "))
# lasso de repertiçao para contagem regressiva
while numero >= 0:
    os.system("cls")
    print(numero)
    numero -=1
    time.sleep(1)
    
print("fim do programa")


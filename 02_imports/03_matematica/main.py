#biblioteca
import math

print(f"numero do pi:{math.pi}")


# entrada de dados
r = float(input("informe o raio do circulo:").strip().replace(",","."))

# calculos
a = math.pi*(r**2)
c = 2*math.pi*r

# saida de dados
print(f"numero do pi:{math.pi}")
print(f"area da circunferencia:{a:.2f}")
print(f"tamanho da circuferencia:{c:.2f}")

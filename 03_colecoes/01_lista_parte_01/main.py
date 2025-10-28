# declaracao de lista
nomes = ["fulano", "cicrano" , "beltrano" , "joao" , "maria" , "jose"]

# exibe toda lista
for nome in nomes:
    print(nome)

# ordena a lista em ordem alfabetica
nomes.sort()

#re-exibir a lista em ordem alfabetica
print("\nordem alfabetica:\n")
for nome in nomes:
    print(nome)

#reverte o a ordem da lista
nomes.sort(reverse=True)

print("\nordem alfabetica reversa:\n")
for nome in nomes:
    print(nome)


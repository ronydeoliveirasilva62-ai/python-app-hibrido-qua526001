# declaracoes de colecoes
usuarios=[{'nome':"fulano",'idade':20,'email':"fulano@"},{'nome':"beltrano",'idade':30,'email':'beltrano@'}]

# exibindo os dados do usuario
for usuario in usuarios:
    print(f"\n{'-'*40}\n")
    for chave in usuario:
        print(f"{chave.capitalize()}:{usuario[chave]}")
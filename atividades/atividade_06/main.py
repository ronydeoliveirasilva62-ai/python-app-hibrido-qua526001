# declaracao de  dicionario 
usuario={}

usuario['nome']=input("informe o nome:").strip().title()
usuario['email']=input("informe o email:").strip().lower()
usuario['cpf']=input("informe o cpf:").strip()
usuario['telefone']=input("informe o telefone:").strip()
usuario['genero']=input("imforme o genero:").strip()

# saida de dados
for chave in usuario:
    print(f"{chave.capitalize()}:{usuario[chave]}")


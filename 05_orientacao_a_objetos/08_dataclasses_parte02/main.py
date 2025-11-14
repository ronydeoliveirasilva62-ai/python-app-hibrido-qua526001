import os

from classes import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    usuario = PessoaFisica(
        nome="",
        idade=0,
        cpf="",
        profissao="",
        email="",
        telefone="",
        endereco=""
    )

    empresa = PessoaJuridica(
        nome_fantasia="",
        cnpj="",
        website="",
        email="",
        telefone="",
        endereco=""
    )

    print("informe os dados do usuario:\n")

    usuario.nome = input("Informe o Nome:").strip().title()
    usuario.idade = int(input("Informe a idade:").strip())
    usuario.cpf = input("Informe o cpf:").strip()
    usuario.profissao = input("Informe a profisao:").strip()
    usuario.email = input("Informe o email:").strip().lower()
    usuario.telefone = input("Informe o telefone:").strip()
    usuario.endereco = input("Informe o endereco:").strip().title()

    limpar()
    print("informe os dados da empresa:\n")

    empresa.nome_fantasia = input("Informe o nome:").strip().title()
    empresa.cnpj = input("Informe o nome:").strip()
    empresa.website = input("Informe o website:").strip().lower()
    empresa.email = input("Informe o emeil:").strip().lower()
    empresa.telefone = input("Informe o telefne:").strip()
    empresa.endereco = input("Informe o endereco:").strip().title()

    limpar()
    print(usuario)
    print(empresa)

    
        





if __name__ == "__main__":
    main()
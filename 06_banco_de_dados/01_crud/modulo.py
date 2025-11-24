import os
from datetime import datetime

def limpar():
   os.system("cls" if os.name == "nt" else "clear")
   
def cadastrar(session, Pessoa):
   try:
      nome = input("informe o nome:").strip().title()
      genero = input("imforme o genero:").strip()
      nascimento = input("informe a data de nasciento (dd/mm/aaaa):").strip()

      nascimento = datetime.strptime(nascimento,"%d/%m/%Y").date()
      email = input("informe o e_amil:").strip().lower()

      pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()

      if email in [pessoa.email for pessoa in pessoas]:
         return "E-mail ja cadastrado."

      else:
         nova_pessoa = Pessoa(nome=nome,
                              nascimento=nascimento,
                              email=email,
                              genero=genero)
         
         session.add(nova_pessoa)
         session.commit()
         return f"pessoa {nova_pessoa.nome} cadastrada com sucesso."

   except Exception as e:
      print(f"nao foi possivel cadastrar. {e}.")


def listar(session, Pessoa):
    try:
      pessoas = session.query(Pessoa).all()

      print("pessoaas cadastradas:\n")
      for pessoa in pessoas:
         print(f"ID: {pessoa.id_pessoa}")
         print(f"nome: {pessoa.nome}")
         print(f"e-mail: {pessoa.email}")
         print(f"genero: {pessoa.genero}")
         print(f"data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
         print(f"\n{'-'*40}\n")
    except Exception as e:
       print(f"nao foi possivel listar.{e}.")


def atualizar(session, Pessoa):
   id_pessoa = ""
   email = ""
   novo_nome = ""
   novo_email = ""
   novo_nascimento = ""
   novo_genero = ""

   try:
      print("esconha o campo que deseja pesquisar:")
      print("1 - ID")
      print("2 - E-mail")
      print("3 - retornar")
      opcao = input("opcao desejada:").strip()
      limpar()
      match opcao:
         case"1":
            id_pessoa = input("informe o ID:").strip()
            pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()

         case"2":
            email = input("informe o e_mail:").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).filter()
         case"3":
            return ""
         case _:
            return "opcao invalida."
         
      if pessoa:
         limpar()
         while True:
            print(f"ID{pessoa.id_pessoa}")
            print(f"gual campo deseja alterar:\n")
            print(f"1 - nome:{pessoa.nome}")
            print(f"2 - E-mail:{pessoa.email}")
            print(f"3 - data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
            print(f"4 - genero: {pessoa.genero}")
            print(f"5 -finalizar")
            campo = input("campo desejado: ").strip()
            limpar()
            match campo:
               case "1":
                  novo_nome = input("informe o novo nome: ").strip().title()
                  continue

               case "2":
                  novo_email = input("informe o novo email:").strip().lower()
                  pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                  if email in[pessoa.email for pessoa in pessoas]:
                     print("email ja cadastrado")

               case "3":
                  novo_nascimento = input("informe a nova data de nascimento (dd/mm/aaaaa): ").strip()
                  continue


               case "4":
                  novo_genero = input("informe o novo genero:").strip().lower()
                  continue

               case "5":
                  novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                  novo_email = novo_email if novo_email != "" else pessoa.email
                  novo_nascimento = datetime.strptime(novo_nascimento,"%d/%m/%Y").date() if novo_nascimento != "" else pessoa.nascimento
                  novo_genero = novo_genero if novo_genero != "" else pessoa.genero
                  break
               case _:
                  print("campo inexistente.")
                  continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero
            session.commit()
            return "dados atualizados com sucesso." 
         else:
            return "Pessoa nao encontrada"
         

              

   except Exception as e:
      print(f"nao foi possivel alterar os dados. {e}.")

def deletar(session, Pessoa):
   id_pessoa = ""
   email = ""
   pessoa = ""

   print("informe o campo que deseja pesquisar:")
   print("1 - id")
   print("2 - E-mail")
   print("3 - Retornar")
   opcao = input("informe o campo que deseja pesquisar:").strip()
   limpar()
   match opcao:
      case "1":
         id_pessoa = input("informe o ID a ser escluido:").strip()
         pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()

      case "2":
         email = input("informe o email do cadastro a ser excluido:").strip().lower()
         pessoa = session.query(Pessoa) .filter_by(email=email).first()

      case "3":
         return ""
      case _:
         return "opcao invalida."   
   if pessoa:
      limpar()
      print(f"ID:{pessoa.id_pessoa}")
      print(f"Nome:{pessoa.nome}")
      print(f"E-mail:{pessoa.email}")
      print(f"Gênero:{pessoa.genero}")
      print(f"Data de Nascimento:{pessoa.nascimento.strftime("%d/%m/%Y")}")
      print({'-'*40})
      print("1 - Sim ")
      print("2 - Nao")
      excluir = input("tem certeza de que deseja excluir o registro?").strip()
      match excluir:
         case"1":
            session.delete(pessoa)
            session.commit()
            return "pessoa excluida com sucesso."
         case "2":
            return ""
         case _:
            return "opcao invalida."


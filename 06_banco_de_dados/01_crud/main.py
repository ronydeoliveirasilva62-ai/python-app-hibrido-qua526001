from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from entidades import criar_tb_pessoa
from modulo import limpar, cadastrar,listar

def main():
    engine = create_engine("sqlite:///01_crud/database/ccrud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    while True:
        print(f"{'-'*20}😜crud da cobra😜{'-'*20}\n")
        print("0 - sair do programa")
        print("1 - cadastrar nova pessoa")
        print("2- listarpessoas")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                print("programa encerrado.")
                break
            case "1":
                print(cadastrar(session,Pessoa)) 
                continue
            case "2":  

              listar(session, Pessoa)
              continue   

            case _:
                print("opcao invalida.")
                continue
        
    


    session.close()


if __name__ == "__main__":
    main()

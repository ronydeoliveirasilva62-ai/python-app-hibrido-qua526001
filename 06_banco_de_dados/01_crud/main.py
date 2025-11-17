from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from entidades import criar_tb_pessoa
from modulo import limpar

def main():
    engine = create_engine("sqlite:///01_crud/database/ccrud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    #todo:fazer o CRUD

    session.close()


if __name__ == "__main__":
    main()

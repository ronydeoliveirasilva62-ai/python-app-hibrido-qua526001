from sqlalchemy import Column, String, Integer, Date

def criar_tb_pessoa(engine, Base):

    try:

        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            nascimento = Column(Date,nullable=False)
            email = Column(String, nullable=False, unique=True)
            genero = Column(String, nullable=True)
            
        Base.metadata.create_all(engine)
        return Pessoa
    except Exception as e:
        print(f"nao foi possivel conectar o banco de dados.{e}.")



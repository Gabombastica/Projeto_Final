from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, scoped_session

engine = create_engine("mysql+pymysql://root:senaisp@localhost:3306/projeto_final")

db_projeto_final = scoped_session (sessionmaker(bind=engine))

Base = declarative_base()

class Cadastro(Base):
    __tablename__ = "cadastros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    data_nascimento = Column(Date)
    telefone = Column(Integer)
    email = Column(String(50))
    senha = Column(String(25))

class Equipamento(Base):
    __tablename__ = "equipamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cliente = Column(String(50), nullable=False)
    quantidade = Column(Integer, default=0)
    nota_cliente = Column(String(300), nullable=False)

class Recurso(Base):
    __tablename__ = "recursos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    responsavel = Column(String(50), nullable=False)
    equipamento = Column(String(50), nullable=False)
    descricao = Column(String(300), nullable=False)

class Ordem(Base):
    __tablename__ = "ordens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(String(50), nullable=False)
    responsavel = Column(String(50), nullable=False)
    equipamento = Column(String(50), nullable=False)
    recurso = Column(String(50), nullable=False)
    prioridade = Column(String(50))
    estado = Column(String(50))
    data_abertura = Column(Date)
    data_prazo = Column(Date)
    descricao = Column(String(350), nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
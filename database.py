import os
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, scoped_session

engine = create_engine("mysql+pymysql://root:senaisp@localhost:3306/final_project")

db_sesseion = scoped_session (sessionmaker(bind=engine))

Base = declarative_base()

class Cadastro(Base):
    __tablename__ = "cadastros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    data_nascimento = Column(Date)
    email = Column(String(100))
    telefone = Column(Integer)
    senha = Column(String(50))

class Equipamento(Base):
    __tablename__ = "equipamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    quantidade = Column(Integer, default=0)
    usuario = Column(String(50), nullable=False)
    nota_solicitante = Column(String(225), nullable=False)
    data_agendada = Column(Date, default=date.today())
    atividade = Column(String(100), nullable=False)
    preco = Column(Integer, default=0)

class Ordem(Base):
    __tablename__ = "ordem_servicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_solicitante = Column(String(50), nullable=False)
    nome_responsavel = Column(String(50), nullable=False)
    descricao = Column(String(225))
    prioridade = Column(String(50))
    material = Column(String(225))
    estado = Column(String(50))
    comeco_ordem = Column(Date)
    conclusao = Column(String(225))

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
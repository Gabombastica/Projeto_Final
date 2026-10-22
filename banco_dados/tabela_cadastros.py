from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import aliased
from sqlalchemy.sql.elements import or_

from database import db_projeto_final, Cadastro

def select_todos_cadastros():
    # Buscar todos os cadastros no banco
    # 1- Montar o select
    cadastros_sql = (
        select(Cadastro, func.count(Cadastro.id).label("cadastros"))
    )
    # 2- Executar o select
    cadastros = db_projeto_final.execute(cadastros_sql).all()
    return cadastros

def salvar(nome, data_nascimento, telefone, email, senha):
    # 3- Salvar no banco
    try:
        novo_cadastro = Cadastro(nome=nome, data_nascimento=data_nascimento, telefone=telefone, email=email, senha=senha)
        db_projeto_final.add(novo_cadastro)
        db_projeto_final.commit()
        flash("Cadastro criado com sucesso", "success")
        return novo_cadastro
    except SQLAlchemyError as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"{e}")
    except Exception as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"Erro: {e}")

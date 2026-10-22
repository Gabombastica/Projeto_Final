from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import aliased
from sqlalchemy.sql.elements import or_

from database import db_projeto_final, Usuario


def select_todos_usuarios():
    # Buscar todos os equipamentos no banco
    # 1- Montar o select
    usuarios_sql = select(Usuario)
    # 2- Executar o select
    usuarios = db_projeto_final.execute(usuarios_sql).all()
    return usuarios

def salvar(nome, data_nascimento, telefone, email, senha):
    # 3- Salvar no banco
    try:
        novo_usuario = Usuario(nome=nome, data_nascimento=data_nascimento, telefone=telefone, email=email, senha=senha)
        db_projeto_final.add(novo_usuario)
        db_projeto_final.commit()
        flash("Usuário criado com sucesso", "success")
        return novo_usuario
    except SQLAlchemyError as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"{e}")
    except Exception as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"Erro: {e}")

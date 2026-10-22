from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import aliased
from sqlalchemy.sql.elements import or_

from database import db_projeto_final, Equipamento

def select_todos_equipamentos():
    # Buscar todos os equipamentos no banco
    # 1- Montar o select
    equipamentos_sql = (
        select(Equipamento, func.count(Equipamento.id).label("equipamentos"))
    )
    # 2- Executar o select
    equipamentos = db_projeto_final.execute(equipamentos_sql).all()
    return equipamentos

def salvar(nome, cliente, data_agendada, quantidade, nota_cliente):
    # 3- Salvar no banco
    try:
        novo_equipamento = Equipamento(nome=nome, cliente=cliente, data_agendada=data_agendada, quantidade=quantidade, nota_cliente=nota_cliente)
        db_projeto_final.add(novo_equipamento)
        db_projeto_final.commit()
        flash("Equipamento criado com sucesso", "success")
        return novo_equipamento
    except SQLAlchemyError as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"{e}")
    except Exception as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"Erro: {e}")

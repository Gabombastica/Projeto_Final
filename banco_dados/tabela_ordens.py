from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import aliased
from sqlalchemy.sql.elements import or_

from database import db_projeto_final, Ordem

def select_todas_ordens():
    # Buscar todos as OS no banco
    # 1- Montar o select
    ordens_sql = (
        select(Ordem, func.count(Ordem.id).label("ordens"))
    )
    # 2- Executar o select
    ordens = db_projeto_final.execute(ordens_sql).all()
    return ordens

def salvar(cliente, responsavel, equipamento, recurso, prioridade, estado, data_abertura, data_prazo, descricao):
    # 3- Salvar no banco
    try:
        nova_ordem = Ordem(cliente=cliente, responsavel=responsavel, equipamento=equipamento, recurso=recurso, prioridade=prioridade, estado=estado, data_abertura=data_abertura, data_prazo=data_prazo, descricao=descricao)
        db_projeto_final.add(nova_ordem)
        db_projeto_final.commit()
        flash("Ordem de Serviço criada com sucesso", "success")
        return nova_ordem
    except SQLAlchemyError as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"{e}")
    except Exception as e:
        db_projeto_final.rollback()
        flash("Ocorreu um erro, tente novamente", "error")
        print(f"Erro: {e}")

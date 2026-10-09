from os import times

import request
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from banco_dados import tabela_cadastro, tabela_equipamentos, tabela_servico
from database import *

app = Flask(__name__)
app.secret_key = "chave-secreta-projeto-2026"

@app.route("/equipamentos", methods=["GET", "POST"])
def listar_equipamentos():
    # 1- Pegar os valores digitados no formulário
    equipamentos_sql = select(Equipamento)
    # 2- Executar o select
    equipamentos = db_session.execute(equipamentos_sql).scalars().all()
    return render_template("equipamentos.html", equipamentos=equipamentos)

@app.route("/ordem_servicos", methods=["GET", "POST"])
def listar_ordem_servicos():
    # 1- Pegar os valores digitados no formulário
    ordem_servicos_sql = select(Ordem)
    # 2- Executar o select
    ordem_servicos = db_session.execute(ordem_servicos_sql).scalars().all()
    return render_template("ordem_servicos.html", ordem_servicos=ordem_servicos)

@app.route("/cadastros", methods=["GET", "POST"])
def listar_cadastros():
    # 1- Pegar os valores digitados no formulário
    cadastros_sql = select(Cadastro)
    # 2- Executar o select
    cadastros = db_session.execute(cadastros_sql).scalars().all()
    return render_template("cadastros.html", cadastros=cadastros)

@app.route("/cadastro/novo", methods=["GET", "POST"])
def novo_cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        data_nascimento = request.form.get("data_nascimento", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        senha = request.form.get("senha", "").strip()

        if not nome:
            flash('Por favor, insira o nome', 'error')
            return redirect(url_for("novo_cadastro"))
        if not data_nascimento:
            flash('Por favor, insira a data de nascimento', 'error')
            return redirect(url_for("novo_cadastro"))
        if not email:
            flash('Por favor, insira o email', 'error')
            return redirect(url_for("novo_cadastro"))
        if not telefone:
            flash('Por favor, insira o telefone', 'error')
            return redirect(url_for("novo_cadastro"))
        if not senha:
            flash('Por favor, insira a senha', 'error')
            return redirect(url_for("novo_cadastro"))

@app.route("/equipamento/novo", methods=["GET", "POST"])
def novo_equipamento():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        usuario = request.form.get("usuario", "").strip()
        nota_solicitante = request.form.get("nota_solicitante", "").strip()
        data_agendada = request.form.get("data_agendada", "").strip()
        atividade = request.form.get("atividade", "").strip()
        preco = request.form.get("preco", "").strip()
        quantidade = request.form.get("quantidade", "").strip()

        if not nome:
            flash('Por favor, insira o nome', 'error')
            return redirect(url_for("novo_equipamento"))
        if not usuario:
            flash('Por favor, insira o usuário', 'error')
            return redirect(url_for("novo_equipamento"))
        if not nota_solicitante:
            flash('Por favor, insira a nota do solicitante', 'error')
            return redirect(url_for("novo_equipamento"))
        if not data_agendada:
            flash('Por favor, insira a data agendada', 'error')
            return redirect(url_for("novo_equipamento"))
        if not atividade:
            flash('Por favor, insira a atividade', 'error')
            return redirect(url_for("novo_equipamento"))
        if not preco:
            flash('Por favor, insira o preço', 'error')
            return redirect(url_for("novo_equipamento"))
        if not quantidade:
            flash('Por favor, insira a quantidade', 'error')
            return redirect(url_for("novo_equipamento"))

@app.route("/ordem_servico/nova", methods=["GET", "POST"])
def nova_ordem_servico():
    if request.method == "POST":
        nome_solicitante = request.form.get("nome_solicitante", "").strip()
        nome_responsavel = request.form.get("nome_responsavel", "").strip()
        descricao = request.form.get("descricao", "").strip()
        prioridade = request.form.get("prioridade", "").strip()
        material = request.form.get("material", "").strip()
        estado = request.form.get("estado", "").strip()
        comeco_ordem = request.form.get("comeco_ordem", "").strip()
        conclusao = request.form.get("conclusao", "").strip()

        if not nome_solicitante:
            flash('Por favor, insira o nome do solicitante', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not nome_responsavel:
            flash('Por favor, insira o nome do responsável', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not descricao:
            flash('Por favor,insira a descrição da ordem de serviço', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not prioridade:
            flash('Por favor, selecione a prioridade', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not material:
            flash('Por favor, insira o material', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not estado:
            flash('Por favor, selecione o estado da OS', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not comeco_ordem:
            flash('Por favor, insira a data do começo', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not conclusao:
            flash('Digite a conclusão', 'error')
            return redirect(url_for("nova_ordem_servico"))

            # salvar no banco
            # tabela_jogador.salvar_jogadores(nome=nome, posicao=posicao, time_id=time_id, numero_camisa=numero_camisa)

        # jogador = tabela_jogador.select_todos()
        # times = tabela_cadastro.select_todos()
        # return render_template("jogadores.html", jogador=jogador, times=times)

    # @app.route("/times")
    # def listar_ordem_servicos():
    #     times = tabela_cadastro.select_todos()
    #     print(times)
    #     return render_template("times.html", times=times)

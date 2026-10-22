from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from banco_dados import tabela_cadastro, tabela_equipamentos, tabela_ordens, tabela_recursos
from database import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = "chave-secreta-projeto-2026"

@app.route("/")
def home():
    return render_template("inicio.html")

@app.route("/equipamentos", methods=["GET", "POST"])
def listar_equipamentos():
    equipamentos = tabela_equipamentos.select_todos()
    return render_template("equipamentos.html", equipamentos=equipamentos)

@app.route("/ordem_servicos", methods=["GET", "POST"])
def listar_ordem_servicos():
    ordem_servicos = tabela_ordens.select_todos()
    return render_template("ordem_servicos.html", ordem_servicos=ordem_servicos)

@app.route("/cadastros", methods=["GET", "POST"])
def listar_cadastros():
    cadastros = tabela_cadastro.select_todos_cadastros()
    return render_template("cadastros.html", cadastros=cadastros)

@app.route("/cadastro/novo", methods=["GET", "POST"])
def novo_cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        data_nascimento = request.form.get("data_nascimento", "").strip()
        telefone = request.form.get("telefone", "").strip()
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "").strip()

        if not nome:
            flash('Por favor, insira o seu nome', 'error')
            return redirect(url_for("novo_cadastro"))
        if not data_nascimento:
            flash('Por favor, insira a sua data de nascimento', 'error')
            return redirect(url_for("novo_cadastro"))
        if not email:
            flash('Por favor, insira o seu email', 'error')
            return redirect(url_for("novo_cadastro"))
        if not telefone:
            flash('Por favor, insira o seu telefone', 'error')
            return redirect(url_for("novo_cadastro"))
        if not senha:
            flash('Por favor, insira a sua senha', 'error')
            return redirect(url_for("novo_cadastro"))

        tabela_cadastro.salvar(nome=nome, data_nascimento=data_nascimento, email=email, telefone=telefone, senha=senha)
        return redirect(url_for("listar_cadastros"))

    cadastros = tabela_cadastro.select_todos_cadastros()
    print(cadastros)
    return render_template("cadastro_principal.html", cadastros=cadastros)

@app.route("/equipamento/novo", methods=["GET", "POST"])
def novo_equipamento():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        cliente = request.form.get("cliente", "").strip()
        data_agendada = request.form.get("data_agendada", "").strip()
        quantidade = request.form.get("quantidade", "").strip()
        nota_cliente = request.form.get("nota_cliente", "").strip()

        if not nome:
            flash('Por favor, insira o nome do equipamento', 'error')
            return redirect(url_for("novo_equipamento"))
        if not cliente:
            flash('Por favor, insira o seu nome', 'error')
            return redirect(url_for("novo_equipamento"))
        if not data_agendada:
            flash('Por favor, selecione uma data para agendar', 'error')
            return redirect(url_for("novo_equipamento"))
        if not quantidade:
            flash('Por favor, insira a quantidade', 'error')
            return redirect(url_for("novo_equipamento"))
        if not nota_cliente:
            flash('Deixe uma nota de descrição (Não obrigatório)', 'error')
            return redirect(url_for("novo_equipamento"))

        tabela_equipamentos.salvar(nome=nome, cliente=cliente, data_agendada=data_agendada, quantidade=quantidade, nota_cliente=nota_cliente)
        return redirect(url_for("listar_equipamentos"))

    equipamentos = tabela_equipamentos.select_todos()
    print(equipamentos)
    return render_template("equipamentos_principal.html", equipamentos=equipamentos)

@app.route("/recurso/novo", methods=["GET", "POST"])
def novo_recurso():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        responsavel = request.form.get("responsavel", "").strip()
        equipamento = request.form.get("equipamento", "").strip()
        descricao = request.form.get("descricao", "").strip()

        if not nome:
            flash('Por favor, insira o nome do recurso', 'error')
            return redirect(url_for("novo_recurso"))
        if not responsavel:
            flash('Por favor, insira o responsável pelo recurso', 'error')
            return redirect(url_for("novo_recurso"))
        if not equipamento:
            flash('Por favor, insira o equipamento que será concertado', 'error')
            return redirect(url_for("novo_recurso"))
        if not descricao:
            flash('Deixe uma nota de descrição (Não obrigatório)', 'error')
            return redirect(url_for("novo_recurso"))

        tabela_recursos.salvar(nome=nome, responsavel=responsavel, equipamento=equipamento, descricao=descricao)
        return redirect(url_for("listar_equipamentos"))

    recursos = tabela_recursos.select_todos()
    print(recursos)
    return render_template("equipamentos_principal.html", equipamentos=equipamentos)

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
            flash('Por favor, insira a descrição da ordem de serviço', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not prioridade:
            flash('Por favor, selecione a prioridade', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not material:
            flash('Por favor, insira o material', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not estado:
            flash('Por favor, selecione o status da OS', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not comeco_ordem:
            flash('Por favor, insira a data do começo', 'error')
            return redirect(url_for("nova_ordem_servico"))
        if not conclusao:
            flash('Digite a conclusão', 'error')
            return redirect(url_for("nova_ordem_servico"))

        tabela_ordens.salvar(nome_solicitante=nome_solicitante, nome_responsavel=nome_responsavel, descricao=descricao, prioridade=prioridade, material=material, estado=estado, comeco_ordem=comeco_ordem, conclusao=conclusao)
        return redirect(url_for("listar_ordem_servicos"))

    ordem_servicos = tabela_ordens.select_todos()
    print(ordem_servicos)
    return render_template("ordem_servico_principal.html", ordem_servicos=ordem_servicos)

if __name__ == "__main__":
    app.run(debug=True)
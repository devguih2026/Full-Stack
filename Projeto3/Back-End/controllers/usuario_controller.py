from flask import Blueprint, request, jsonify
from services.usuario_service import cadastrar_usuario, autenticar_usuario

projeto_bp = Blueprint("projeto", __name__)

# ---------- CADASTRO ----------
@projeto_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json
    nome = dados["nome"]
    cpf = dados["cpf"]
    senha = dados["senha"]

    usuario = cadastrar_usuario(nome, cpf, senha)

    return jsonify({"mensagem": "Usuário criado com sucesso"})


# ---------- LOGIN ----------
@projeto_bp.route("/login", methods=["POST"])
def login():
    dados = request.json
    cpf = dados["cpf"]
    senha = dados["senha"]

    usuario = autenticar_usuario(cpf, senha)

    if not usuario:
        return jsonify({"mensagem": "CPF ou senha inválidos"}), 401

    return jsonify({
        "mensagem": "Login realizado com sucesso",
        "nome": usuario.nome
    })




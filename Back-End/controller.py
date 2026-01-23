
from flask import Blueprint, request, jsonify
from crud import NovoUsuario, MostrarUsuarios, RemoverUsuarios, AtualizarUsuarios, ValidarLogin

projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/cadastro", methods=["POST"])
def NovoDado():
    dados = request.json

    nome = dados["nome"]
    email = dados["email"]

    chamar = NovoUsuario(nome, email)

    return jsonify(chamar), 201

@projeto_bp.route("/login", methods=["POST"])
def VerDados():
    chamar = MostrarUsuarios()
    return jsonify(chamar), 200

@projeto_bp.route("/cadastro/usuario/<id>", methods=["DELETE"])
def ApagarDados(id):
    chamar = RemoverUsuarios(id) 
    return jsonify(chamar)

@projeto_bp.route("/cadastro/usuario/<id>", methods=["PUT"])
def Atualizacao(id):
    dados = request.json
    nome = dados["nome"]
    chamar = AtualizarUsuarios(nome, id)
    return jsonify(chamar)

@projeto_bp.route("/Logar", methods=["POST"])
def Login():
    dados = request.get_json()
  
    nome = dados.get("nome")
    email = dados.get("email")

    print("Nome:", nome)
    print("Email:", email)

    entrar = ValidarLogin(nome, email)

    if not entrar:
        return jsonify({"erro": "nome ou email incorreto"}), 401

    return jsonify({"mensagem": "Login realizado com sucesso"}), 200
""
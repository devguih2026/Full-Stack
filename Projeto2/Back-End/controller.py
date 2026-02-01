from flask import Blueprint, request, jsonify
from crud import buscar_cep, cadastrar_cep

projeto_bp = Blueprint("projeto_bp", __name__)

@projeto_bp.route("/cep", methods=["POST"])
def consultar_cep():
    dados = request.get_json()
    cep = dados.get("cep")

    resultado = buscar_cep(cep)

    if resultado:
        return jsonify({
            "encontrado": True,
            "cidade": resultado.cidade,
            "estado": resultado.estado
        }), 200

    return jsonify({
        "encontrado": False,
        "mensagem": "CEP não encontrado"
    }), 404

@projeto_bp.route("/Atualizar", methods=["POST"])
def novo_cep():
    dados = request.get_json()
    cep = dados.get("cep")
    cidade = dados.get("cidade")
    estado = dados.get("estado")

    resultado = cadastrar_cep(cep, cidade, estado)
    return jsonify(resultado)
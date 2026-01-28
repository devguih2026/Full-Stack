from flask import Blueprint, request, jsonify
from crud import buscar_cep, cadastrar_cep

cep_bp = Blueprint("cep", __name__)

@cep_bp.route("/cep", methods=["POST"])
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

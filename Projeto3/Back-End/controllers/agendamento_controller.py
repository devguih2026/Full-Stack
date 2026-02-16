from flask import Blueprint, request, jsonify
from services.agendamento_service import agendar

agendamento_bp = Blueprint("agendamento", __name__)

@agendamento_bp.route("/agendamentos", methods=["POST"])
def criar_agendamento():
    dados = request.json
    usuario_id = dados["usuario_id"]
    data = dados["data"]

    agendamento = agendar(usuario_id, data)

    return jsonify({"mensagem": "Agendamento criado com sucesso"})


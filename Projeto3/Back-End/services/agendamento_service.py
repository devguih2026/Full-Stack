from repositories.agendamento_repo import criar_agendamento

def agendar(usuario_id, data):
    # aqui depois pode validar horário disponível
    return criar_agendamento(usuario_id, data)

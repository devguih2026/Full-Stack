from App.db import SessionLocal
from models.agendamento import Agendamento

def criar_agendamento(usuario_id, data, hora):
    db = SessionLocal()

    agendamento = Agendamento(
        usuario_id=usuario_id,
        data=data,
        hora=hora
    )

    db.add(agendamento)
    db.commit()
    db.refresh(agendamento)
    db.close()

    return agendamento


def listar_agendamentos():
    db = SessionLocal()
    agendamentos = db.query(Agendamento).all()
    db.close()
    return agendamentos

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from App.db import Base


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True)
    agendamento_id = Column(Integer, ForeignKey("agendamentos.id"), nullable=False)
    data_realizacao = Column(DateTime)

    agendamento = relationship("Agendamento")

# Importa os tipos de colunas: 
# Column: define uma coluna da tabela
# Integer: tipo inteiro
# String: tipo texto (VARCHAR no MySQL)
from sqlalchemy import Column, Integer, String
from db import Base

# Define a classe Cep, essa classe representa a tabela "cep" no banco de dados
class Cep(Base):

    # Nome da tabela no banco de dados
    # O SQLAlchemy vai mapear essa classe para a tabela "cep"
    __tablename__ = "cep"

    id = Column(Integer, primary_key=True)
    cep_codigo = Column(Integer, unique=True, nullable=False)
    cidade = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)

# Esse model representa a tabela "cep" do banco de dados
from models.cep import Cep

# Importa a fábrica de sessões criada no db.py para conversar com o banco
from db import SessionLocal

# Função responsável por BUSCAR um CEP no banco (READ)
def buscar_cep(cep):

    # Cria uma nova sessão, cada sessão é uma "conversa" com o banco
    session = SessionLocal()

    # Monta a query:
    # session.query(Cep) → SELECT * FROM cep
    # filter(Cep.cep_codigo == cep) → WHERE cep = valor_recebido
    # first() → pega apenas o primeiro resultado (ou None)
    resultado = session.query(Cep).filter(Cep.cep_codigo == cep).first()

    # Fecha a sessão para liberar recursos
    session.close()

    # Retorna o objeto Cep encontrado ou None se não existir
    return resultado

# Função responsável por CADASTRAR um novo CEP no banco (CREATE)
def cadastrar_cep(cep, cidade, estado):
    session = SessionLocal()

    # Cria um novo objeto Cep, esse objeto ainda não está no banco
    novo = Cep(cep=cep, # valor do CEP
               cidade=cidade, # valor da cidade
               estado=estado) # valor do estado
    
    # Adiciona o objeto à sessão, isso prepara o INSERT, mas ainda não executa
    session.add(novo)

    # Confirma a transação, aqui o INSERT é realmente executado no banco
    session.commit()
    session.close()

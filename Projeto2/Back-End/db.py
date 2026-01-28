# Importa a função create_engine, responsável por criar a conexão com o banco de dados
from sqlalchemy import create_engine

# - sessionmaker: cria sessões para conversar com o banco
# - declarative_base: base para criar os models (classes que viram tabelas)
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:Guilherme!@localhost/localizacao"

# Cria o "engine", que é o objeto responsável pela conexão real com o banco
engine = create_engine(DATABASE_URL, echo=True)

# Cada vez que você chamar SessionLocal(), você cria uma nova sessão
# A sessão é quem executa: SELECT, INSERT, UPDATE, DELETE
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


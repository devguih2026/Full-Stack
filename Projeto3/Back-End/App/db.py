from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:Guilherme!@localhost/agendamentos"

engine = create_engine (DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

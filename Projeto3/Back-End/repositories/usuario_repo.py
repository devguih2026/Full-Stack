from App.db import SessionLocal
from models.usuario import Usuario


# ---------- CRIAR USUÁRIO ----------
def criar_usuario(nome, cpf, senha):
    db = SessionLocal()

    novo_usuario = Usuario(
        nome=nome,
        cpf=cpf,
        senha=senha
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    db.close()

    return novo_usuario


# ---------- BUSCAR POR CPF ----------
def buscar_usuario_por_cpf(cpf):
    db = SessionLocal()

    usuario = db.query(Usuario).filter(Usuario.cpf == cpf).first()

    db.close()

    return usuario





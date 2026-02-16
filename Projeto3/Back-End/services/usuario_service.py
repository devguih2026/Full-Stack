from repositories.usuario_repo import criar_usuario, buscar_usuario_por_cpf


def cadastrar_usuario(nome, cpf, senha):
    
    return criar_usuario(nome, cpf, senha)


def autenticar_usuario(cpf, senha):
    usuario = buscar_usuario_por_cpf(cpf)

    if usuario is None:
        return None

    if usuario.senha != senha:
        return None

    return usuario

from db import Conectar

def NovoUsuario(nome,email):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO usuario (nome, email) VALUES (%s, %s)"
    cursor.execute(query, (nome, email))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Query executada"
    
def MostrarUsuarios():
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    print("Query executada")
    return resultado

def RemoverUsuarios(id):
    conexao = Conectar()
    cursor = conexao.cursor(dictionary=True)
    query = "DELETE FROM usuario WHERE id = %s"
    cursor.execute(query, (id, ))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Query executada"

def AtualizarUsuarios(nome, id):
    conexao = Conectar()
    cursor = conexao.cursor()
    query = "UPDATE usuario SET nome = %s WHERE id= %s"
    cursor.execute(query, (nome, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Dados atualizados"
    

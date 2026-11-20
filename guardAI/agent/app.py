import sqlite3


def fazer_login(usuario, senha):
    query = """
        SELECT 1
        FROM usuarios
        WHERE username = ? AND password = ?
        LIMIT 1
    """

    conexao = sqlite3.connect("banco_de_dados.db")
    try:
        cursor = conexao.execute(query, (usuario, senha))
        resultado = cursor.fetchone()
    finally:
        conexao.close()

    if resultado:
        return "Acesso Permitido!"
    return "Acesso Negado."
import sqlite3 as conector


class TipoCurso:
    def __init__(self, descricao):
        self.descricao = descricao


class Titulo:
    def __init__(self, descricao):
        self.descricao = descricao


class Instituicao:
    def __init__(self, sigla, descricao):
        self.sigla = sigla
        self.descricao = descricao


class TipoDisciplina:
    def __init__(self, descricao):
        self.descricao


def create_tables():

    # tipo_curso, titulo, instituicao, tipo_disciplina
    try:
        conexao = conector.connect('escola.db')
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        # crição da tabela tipo_curso
        cursor.execute('''CREATE TABLE IF NOT EXISTS tipo_curso (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT)''')

        # crição da tabela titulo
        cursor.execute('''CREATE TABLE IF NOT EXISTS titulo (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT)''')

        # crição da tabela instituicao
        cursor.execute('''CREATE TABLE IF NOT EXISTS instituicao (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sigla TEXT,
                        descricao TEXT)''')

        # crição da tabela tipo_disciplina
        cursor.execute('''CREATE TABLE IF NOT EXISTS tipo_disciplina(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT)''')

        conexao.commit()
    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


if __name__ == "__init__":
    create_tables()

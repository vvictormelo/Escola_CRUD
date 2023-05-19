import sqlite3 as conector
# tipo_curso, titulo, instituicao, tipo_disciplina


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
        self.descricao = descricao


def create_tables():

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


def insert_tipo_curso():

    descricao_tipo_curso = input("Digite a descrição do curso: ")

    curso = TipoCurso(descricao_tipo_curso)

    try:
        conexao = conector.connect('escola.db')
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO tipo_curso (descricao) VALUES (?)", (curso.descricao,))
        conexao.commit()
    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def insert_titulo():

    descricao_titulo = input("Digite a descrição do titulo do professor: ")

    titulo = Titulo(descricao_titulo)

    try:
        conexao = conector.connect('escola.db')
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO titulo (descricao) VALUES (?)", (titulo.descricao,))

        conexao.commit()

    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def insert_instituicao():

    sigla_instituicao = input("Digite a sigla da instituição: ")
    descricao_instituicao = input("Digite a descrição da instituicao: ")

    instituicao = Instituicao(sigla_instituicao, descricao_instituicao)

    try:
        conexao = conector.connect('escola.db')
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO instituicao (sigla, descricao) VALUES (?, ?)", (instituicao.sigla, instituicao.descricao,))

        conexao.commit()

    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def insert_tipo_disciplina():

    descricao_tipo_disciplina = input("Digite o tipo de disciplina: ")

    tipo_disciplina = TipoDisciplina(descricao_tipo_disciplina)

    try:
        conexao = conector.connect('escola.db')
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO tipo_disciplina (descricao) VALUES (?)", (tipo_disciplina.descricao,))

        conexao.commit()

    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


insert_tipo_disciplina()

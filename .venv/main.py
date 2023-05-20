import sqlite3 as conector
from entities import TipoCurso, Titulo, Instituicao, TipoDisciplina


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

        print("\033[1;36m\nTabelas criadas com êxito.\033[m")
    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def insert_tipo_curso():

    print("\n-=-=-=-=-=-=Cadastro de Tipo de curso-=-=-=-=-=-=")

    descricao_tipo_curso = input("\nDigite a descrição do tipo de curso: ")

    curso = TipoCurso(descricao_tipo_curso)

    try:
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO tipo_curso (descricao) VALUES (?)", (curso.descricao,))
        conexao.commit()

        print("\033[1;36m\nTipo de curso cadastrado com êxito.\033[m")
    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def insert_titulo():

    print("\n-=-=-=-=-=-=Cadastro de Título-=-=-=-=-=-=")

    descricao_titulo = input("\nDigite a descrição do titulo do professor: ")

    titulo = Titulo(descricao_titulo)

    try:
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO titulo (descricao) VALUES (?)", (titulo.descricao,))

        conexao.commit()

        print("\033[1;36m\nTítulo cadastrado com êxito.\033[m")
    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def insert_instituicao():

    print("\n-=-=-=-=-=-=Cadastro de Instituição-=-=-=-=-=-=")

    sigla_instituicao = input("\nDigite a sigla da instituição: ")
    descricao_instituicao = input("\nDigite a descrição da instituicao: ")

    instituicao = Instituicao(sigla_instituicao, descricao_instituicao)

    try:
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO instituicao (sigla, descricao) VALUES (?, ?)", (instituicao.sigla, instituicao.descricao,))

        conexao.commit()

        print("\033[1;36m\ninstituição cadastrada com êxito.\033[m")
    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def insert_tipo_disciplina():

    print("\n-=-=-=-=-=-=Cadastro de Disciplina-=-=-=-=-=-=")

    descricao_tipo_disciplina = input("\nDigite o tipo de disciplina: ")

    tipo_disciplina = TipoDisciplina(descricao_tipo_disciplina)

    try:
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO tipo_disciplina (descricao) VALUES (?)", (tipo_disciplina.descricao,))

        conexao.commit()

        print("\033[1;36m\nDisciplina cadastrada com êxito.\033[m")
    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close


def menu():

    print("\n")
    print("-=" * 15)
    print(f'\033[1;36m{"MENU - CADASTRO ACADÊMICO":>27}\033[m')
    print("-=" * 15)
    print("\n1 - Criar tabelas")
    print(
        """2 - Crud entidades: 
    2.1 - Criar Tipo de curso
    2.2 - Criar Titulo 
    2.3 - Criar Instituição
    2.4 - Criar Tipo de Disciplina"""
    )
    print("3 - Sair")


def program():

    print("\033[1;36m\nSEJA BEM VINDO...\033[m")

    acao = 0
    try:
        while acao != 3:

            menu()
            acao = float(input("\nInsira a ação desejada: "))

            match acao:
                case 1:
                    create_tables()
                case 2.1:
                    insert_tipo_curso()
                case 2.2:
                    insert_titulo()
                case 2.3:
                    insert_instituicao()
                case 2.4:
                    insert_tipo_disciplina()
                case 3:
                    acao = 3
                    print("Saindo... Até logo!")
            if (acao > 4.0) or (acao < 1.0):
                print(
                    "\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")

    except ValueError:
        print("\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")


if __name__ == "__main__":
    program()

import sqlite3 as conector

def database_create():

    try:
        conexao = conector.connect('escola.db')
        cursor = conexao.cursor()

    except ConnectionError as e:
        print("Erro no banco", e)

    finally:
        cursor.close()
        conexao.close

if (__name__ == '__main__'):
    database_create()

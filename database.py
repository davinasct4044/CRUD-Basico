import sqlite3 as sql
#importa a biblioteca do sqlite3(nativa)


def get_connection(): #cria uma função para se conectar com o banco de dados
    connection = sql.connect("usuarios.db") #usa o metodo do sqlite para se conectar
    return connection

def create_table():
    # cria uma tabela com os usuarios e com as colunas dos tipos dos dados
    connection = get_connection()
    # coloca a função dentro da váriavel, assim retornando a conexão
    cursor = connection.cursor()
    #pega o cursor da função de conexao, me permite executar comandos sql
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            senha TEXT
        )""") #executa meus comandos sql, para criar a tabela.
    connection.commit() #salva essa tabela criada no banco de dados
    connection.close() #fecha a conexao com o banco de dados

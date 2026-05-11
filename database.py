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

def register_user(nome, email, senha): #essa função registra os dados(params) do usuario no banco de dados
    connection = get_connection() #inicia a conexão
    cursor = connection.cursor()#da conexão ele pega o método cursor
    cursor.execute("""
    INSERT INTO usuarios (
        nome, 
        email, 
        senha
    ) VALUES (?, ?, ?)""", (nome, email, senha))
    #Executa os comandos SQL para cadastrar usuario
    # Os ? são placeholders que o SQLite substitui pelos valores da tupla,
    # evitando SQL Injection
    connection.commit() #salva as alterações no banco de dados
    connection.close() #fecha a conexão com o banco de dados

def get_users(): #estrutura da função que lê os dados e os retorna
    connection = get_connection() #inicia a conexão
    cursor = connection.cursor() # da conexão ele pega o método cursor
    cursor.execute("""
    SELECT id, nome, email FROM usuarios""")
    #executa o comando sql para ler os dados do banco de dados
    #aqui não precisa de connection.commit() pq não modifica o banco de dados, apenas lê
    users = cursor.fetchall()#atribui todos os dados buscados no cursor dentro da variavel
    connection.close()#fecha a conexão
    return users #retorna os usuarios do banco de dados

def get_users_by_id(id):#só recebe o id como parâmetro
    connection = get_connection()#inicia a conexao
    cursor = connection.cursor()#pega o cursor da conexao
    cursor.execute("""SELECT * FROM usuarios WHERE id = ?""", (id, ))
    """executa o comando sql, usando o WHERE para filtrar o usuario pelo id, nos paramente tem q colocar a virgula
    após o parametro, assim o SQlite entende que é uma tupla."""
    user = cursor.fetchone()#pega só um resultado o outro fetch retorna uma lista
    connection.close()#fecha a conexão
    return user#retorna os valores desse usuario
        
def update_user(id, nome, email, senha):#atualiza todos os dados do usuario, por isso pega todos os params
    connection = get_connection()#inicia a conexão
    cursor = connection.cursor()#pega o cursor da conexão
    cursor.execute(""" UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?""", (nome, email, senha, id))
    #executa os comandos sql, para atualizar os dados,coloca ? que depois vira o valor que tá no params, questão de segurança.
    connection.commit()#salva a alteração
    connection.close()#fecha a conexão

def delete_user(id)#recebe o id da função erase_user
    connection = get_connection()#inicia a conexão
    cursor = connection.cursor()#pega o cursor da conexão
    cursor.execute("""DELETE FROM usuarios WHERE id = ?""", (id, )) #tem q ter a virgula no (id,)
    connection.commit()#salva as alerações
    connection.close() #fecha a conexão

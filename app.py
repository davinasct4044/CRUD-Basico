from flask import Flask
#importa o modulo Flask
from database import get_connection, create_table
#importa as funções para criar o banco de dados
app = Flask(__name__)
create_table() #usa a função que conecta o banco de dados e cria a tabela

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

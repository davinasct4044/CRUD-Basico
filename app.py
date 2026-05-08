from flask import Flask, render_template

#importa o modulo Flask
from database import get_connection, create_table
#importa as funções para criar o banco de dados
app = Flask(__name__)
create_table() #usa a função que conecta o banco de dados e cria a tabela

@app.route('/')
def renderizarformulario():
    return render_template("create.html")
@app.route('/usuarios')    
def renderizarindex():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

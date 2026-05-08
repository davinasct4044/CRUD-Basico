from flask import Flask, render_template, request, redirect, url_for
#importa o modulo Flask
from database import get_connection, create_table, register_user
#importa as funções para criar o banco de dados
app = Flask(__name__)
create_table() #usa a função que conecta o banco de dados e cria a tabela

@app.route('/')
def render_form():
    return render_template("create.html")
@app.route('/users')
def render_index():
    return render_template("index.html")
@app.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    register_user(nome, email, senha)
    return redirect(url_for("render_index"))
if __name__ == '__main__':
    app.run()

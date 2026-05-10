from flask import Flask, render_template, request, redirect, url_for
#importa métodos do Flask:
#render_template para renderizar templates.
#request para pegar dados do request
#redirect para redirecionar o usuario para outra rota
#url_for, é uma sintaxe do jinja2, para misturar python com html e o html com python

from database import get_connection, create_table, register_user, get_users
#importa as funções para criar o banco de dados:
#create_table é para criar o banco de dados inicial
#register_user é pra cadastrar o usuario no banco de dados
#get_users é para ler os usuarios do banco de dados
app = Flask(__name__)
create_table() #usa a função que conecta o banco de dados e cria a tabela

@app.route('/') #rota principal
def render_form(): #estrutura de função para colocar o método que renderiza o template
    return render_template("create.html") # retorno que retorna o método do flask para renderizar o template

@app.route('/users') #rota que fica os usuários cadastrados no banco de dados
def render_index(): #estrutura de função para colocar o método que renderiza o template
    users = get_users() #guarda os usuarios cadastrados da função get_users do banco de dados, e atribui na variavel
    return render_template("index.html", usuarios=users)
# retorno que retorna o método do flask para renderizar o template, e envia os usuarios cadastrados para o html.

@app.route('/register', methods=['POST'])
#rota com o método POST, só é usada para cadastrar o usuario no banco de dados
def register():#estrutura de função
    nome = request.form['nome'] #método do flask para pegar dados do request. Nesse caso do action="" do <form>
    email = request.form['email'] #método do flask para pegar dados do request. Nesse caso do action="" do <form>
    senha = request.form['senha'] #método do flask para pegar dados do request. Nesse caso do action="" do <form>
    register_user(nome, email, senha) #executa a função do database.py para cadastrar o usuario no banco de dados.
    return redirect(url_for("render_index")) #método do flask para redirecionar um usuario para uma página.

if __name__ == '__main__':
    app.run()

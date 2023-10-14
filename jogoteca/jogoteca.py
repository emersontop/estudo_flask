from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo(object):

    def __init__(self, nome, categoria, console):
        self.__nome = nome
        self.__categoria = categoria
        self.__console  = console

    @property
    def nome(self):
        return self.__nome
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def console(self):
        return self.__console


jogo1 = Jogo('Tetris','Puzzle','Atari')
jogo2 = Jogo('God of war','Rack in Slash','PS2')
jogo3 = Jogo('Mortal combat','Luta','PS2')

lista_de_jogos = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Bruno Divino", "BD", "alohomora")
usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake", "Python_eh_vida")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3 }

# instancia a aplicação
app = Flask(__name__)
app.secret_key ='alura'

# Rota
@app.route('/')
def index():
    # instanciando jogos:

    return render_template('lista.html', titulo = 'Jogos', jogos = lista_de_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima = url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    #captura as informações do forms
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login',proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        # grava em um dicionario o nome do usuário
        session['usuario_logado'] = request.form['usuario'] 
        flash('logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

# Roda a a plicação
app.run(debug = True)
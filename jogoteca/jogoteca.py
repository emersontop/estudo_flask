from flask import Flask, render_template, request, redirect, session, flash

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
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    #captura as informações do forms
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo='Login')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario'] 
        flash(session['usuario_logado'] + 'logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('login')

# Roda a a plicação
app.run(debug = True)
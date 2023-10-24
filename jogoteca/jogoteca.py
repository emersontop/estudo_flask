from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# instancia a aplicação
app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app) 
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views_game import *
from views_users import *

# Roda a a plicação

if __name__ == '__main__':
    app.run(debug = True)
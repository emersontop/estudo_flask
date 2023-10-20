from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

# instancia a aplicação
app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app) 

from views import *

# Roda a a plicação

if __name__ == '__main__':
    app.run(debug = True)
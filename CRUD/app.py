import os
from functools import wraps
from flask import Flask, render_template, redirect, request, flash, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

############# CRIANDO BANCO DE DADOS ###############
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


############### CRIANDO TABELAS ##############
class Post(db.Model):
    __tablename__="posts"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text)
    descricao = db.Column(db.Text)
    tema_cor = db.Column(db.String)



################ DEFININDO ROTAS #################


@app.route("/<string:tema>")
@app.route("/", defaults = {'tema':None})
def index(tema):
    if tema== "grey" or tema== None:
        posts =  Post.query.all()
    else:
        posts =  Post.query.filter_by(tema_cor = tema)
    return render_template('dashboard.html', posts=posts)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    categ = request.form['categoria']

    novoPost = Post()
    novoPost.descricao = descricao
    novoPost.titulo  = titulo
    novoPost.tema_cor = categ

    db.session.add(novoPost)
    db.session.commit()

    return redirect(url_for('index'))
    

@app.route("/deletar/<int:id>")
def deletar(id):

    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/editar/<int:id>", methods=['POST'])
def editar(id):

    
    post = Post.query.get(id)
    post.titulo = request.form['titulo']
    post.descricao = request.form['descricao']

    db.session.commit()

    return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(debug=True)

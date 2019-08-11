from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text)
    descricao = db.Column(db.Text)

@app.route("/")
def index():

    posts =  Post.query.all()
    return render_template('dashboard.html', posts=posts)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form['titulo']
    descricao = request.form['descricao']

    novoPost = Post()
    novoPost.descricao = descricao
    novoPost.titulo  = titulo

    db.session.add(novoPost)
    db.session.commit()

    return redirect(url_for("index"))
    

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

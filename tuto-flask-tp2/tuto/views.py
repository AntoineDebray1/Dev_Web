from .app import app,db
from flask import render_template,url_for , redirect
from .models import get_author, get_sample,Author
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms.validators import DataRequired

class AuthorForm ( FlaskForm ):
    id = HiddenField("id")
    name = StringField("Nom", validators=[DataRequired()])

@app.route("/edit/author/<int:id>")
def edit_author (id):
    a = get_author(id)
    f = AuthorForm(id=a.id , name=a.name)
    return render_template("edit-author.html",author =a, form=f)

@app.route("/")
def home():
    return render_template(
        "booksBS.html", 
        title="My Books !",
        books=get_sample())


@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    return render_template(
        "detail.html",
        book=book)

@app.route("/save/author/", methods =("POST" ,))
def save_author():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('one_author',id=a.id))
    a = get_author(int(f.id.data ))
    return render_template("edit-author.html",author =a, form=f)

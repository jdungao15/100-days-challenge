from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# Create the extension
db = SQLAlchemy()

# APP CONFIG
WTF_CSRF_SECRET_KEY = 'snoopy'
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db.init_app(app)


# Books Data
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create Database
with app.app_context():
    db.create_all()


# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Forms
class book_form(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


class edit_rating(FlaskForm):
    rating = StringField('Change Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    books = Book.query.all()
    print(books)
    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = book_form()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(book)
        db.session.commit()
        return render_template('index.html', books=Book.query.all())

    return render_template('add.html', form=form)


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book_to_update = Book.query.get(book_id)
    form = edit_rating()

    if form.validate_on_submit():
        book_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_to_update, form=form)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

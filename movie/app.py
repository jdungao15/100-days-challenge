from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import pprint as pp

API_KEY = '97e0004539d7957771e44c003ea457e7'
API_URL = 'https://api.themoviedb.org/3/search/movie'



# Create Extension
db = SQLAlchemy()

# App Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
db.init_app(app)


# Edit Form
class EditForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    movie = StringField("Movie Name", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# Movie Model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    for movie in all_movies:
        print(movie.title)
    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditForm()
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    #
    # # title = movie_data['results']['title']
    # # year= movie_data['results']['release_date']
    # # description = movie_data['results']['overview']
    # # rating = movie_data['results']['vote_average']

    form = AddForm()
    if form.validate_on_submit():
        title = form.movie.data
        res = requests.get(url=API_URL, params={
            'api_key': API_KEY,
            'query': title
        })
        res.raise_for_status()
        movie_data = res.json()

        return render_template('select.html', movie_data=movie_data)
    return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_id = request.args.get('movie_id')
    print(movie_id)
    movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    if movie_id:
        res = requests.get(url=movie_api_url, params={
            'api_key': API_KEY,
            "languange": "en-US"
        })
        movie_data = res.json()
        pp.pprint(movie_data)
        image_path = f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
        movie = Movie(
            title=movie_data['title'],
            year=movie_data['release_date'].split('-')[0],
            description=movie_data['overview'],
            img_url=image_path)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('edit', movie_id=movie.id))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

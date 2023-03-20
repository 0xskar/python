import os
from flask import Flask, render_template, redirect, url_for, request, session, flash, Markup
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, HiddenField, TextAreaField
from wtforms.fields.html5 import DateField, IntegerField, URLField
from wtforms.validators import DataRequired, NumberRange, URL, Length
import requests
from movies import Movies

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Strapi API & Populate
api_endpoint = "http://192.168.0.35:1337/api/favourite-movies"
api_headers = {
    "Authorization": f"Bearer {os.environ['STRAPI_API_KEY']}",
    "accept": "application/json",
    "Content-Type": "application/json"
}


# Forms
class EditMovieForm(FlaskForm):
    rating = FloatField('Rating 1-10', validators=[DataRequired(), NumberRange(min=0, max=10, message="Number must be between 0 and 10. You can use decimal.")])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit Edit')


class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Release Year', validators=[DataRequired(), NumberRange(min=1900, max=2025, message="Must be a valid year.")])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10, message="Must be between 1-10.")])
    review = StringField('Review', validators=[DataRequired()])
    img_url = URLField('Movie URL Image', validators=[DataRequired(), URL(message="Must be a Valid URL")])


@app.route("/")
def home():
    r = requests.get(url=api_endpoint, headers=api_headers)
    data = r.json()['data']

    # assign all movies in the db
    all_movies = []
    for entry in data:
        movie = Movies(
            movie_id=entry['id'],
            title=entry['attributes']['title'],
            year=entry['attributes']['year'],
            description=entry['attributes']['description'],
            rating=entry['attributes']['rating'],
            ranking=None,
            review=entry['attributes']['review'],
            img_url=entry['attributes']['img_url']
        )
        all_movies.append(movie)

    # sort the movies by rating and assign rankings based on sorted order
    sorted_movies = sorted(all_movies, key=lambda m: m.rating, reverse=True)

    for i, movie in enumerate(sorted_movies):
        movie.ranking = i + 1

    return render_template("index.html", movies=sorted_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    # edit movie with new rating and new review
    form = EditMovieForm()
    # only assign session on GET and recieve on POST to ensure correct ID value used
    if request.method == "GET":
        session["movie_id"] = request.args.get('id')
    movie_id = session.get("movie_id")
    if form.validate_on_submit():
        if movie_id is None:
            flash(Markup("Invalid movie id. Select a new movie, from <a href='{}'>the homepage</a>.".format(url_for("home"))))
            return redirect(url_for('edit'))
        rating = form.rating.data
        review = form.review.data
        # add edited data to db
        json = {
          "data": {
            "rating": rating,
            "review": review,
          }
        }
        r = requests.put(url=f"{api_endpoint}/{movie_id}", headers=api_headers, json=json)
        movie = r.json()['data']
        movie_title = movie['attributes']['title']
        session.pop("movie_id", None)
        flash(Markup("Movie '{}' edited successfully. Return to <a href='{}'>the homepage</a>.".format(movie_title, url_for("home"))))
        return redirect(url_for('edit'))
    return render_template('edit.html', form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    r = requests.delete(url=f"{api_endpoint}/{movie_id}", headers=api_headers)
    flash(f"Movie successfully deleted.")
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        schema = {
          "data": {
            "title": form.title.data,
            "description": form.description.data,
            "rating": form.rating.data,
            "review": form.review.data,
            "img_url": form.img_url.data,
            "year": form.year.data
          }
        }
        r = requests.post(url=api_endpoint, headers=api_headers, json=schema)
        flash(Markup('Movie {} Successfully added!, return <a href="{}">home</a>, or add another.').format(form.title.data, url_for('home')))
        return redirect(url_for('add'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)

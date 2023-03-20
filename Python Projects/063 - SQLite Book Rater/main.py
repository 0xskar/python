import os
import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets.html5 import NumberInput


# Flask Stuff
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Strapi
strapi_headers = {
    "Authorization": f"Bearer {os.environ['STRAPI_API_KEY']}"
}
strapi_endpoint = "http://192.168.0.35:1337/api/books"


# Forms
class AddBook(FlaskForm):
    rating_choices = []
    for _ in range(1, 11):
        choice = (_, f"{_}")
        rating_choices.append(choice)
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    book_rating = SelectField('Book Rating', choices=rating_choices)
    submit = SubmitField('Submit')


# Get all books from Strapi
def get_books():
    params = {
        "sort": "id:desc"
    }
    r = requests.get(url=strapi_endpoint, headers=strapi_headers, params=params)
    data = r.json()
    return data['data']


# Post new book to strapi
def post_book(book_data):
    data = {
        "data": book_data
    }
    r = requests.post(url=strapi_endpoint, headers=strapi_headers, json=data)
    print(r.text)


@app.route('/')
def home():
    all_books = get_books()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():

    form = AddBook()
    if form.validate_on_submit():
        book_data = {
            "title": form.book_name.data,
            "author": form.book_author.data,
            "rating": form.book_rating.data
        }
        post_book(book_data)


    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)


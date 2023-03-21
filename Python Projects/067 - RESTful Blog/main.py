import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from collections.abc import MutableMapping
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# connect to db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine("sqlite:///posts.db", echo=True)
Session = scoped_session(sessionmaker(bind=engine))
db = SQLAlchemy(app)


# configure table
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# Post form
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Edit form
class EditPostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField("Submit Post")

@app.route('/')
def get_all_posts():
    session = Session()
    posts = session.query(BlogPost).all()
    session.close()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    session = Session()
    posts = session.query(BlogPost).all()
    session.close()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.date.today().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        session = Session()
        session.add(new_post)
        session.commit()
        session.close()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


@app.route("/edit-post", methods=["GET", "POST"])
def edit_post():
    form = EditPostForm()

    # get the post_id from url
    post_id = request.args.get('post_id')

    # submit the edited post if submitted.
    session = Session()
    if form.validate_on_submit():
        post_edit = BlogPost(
            id=post_id,
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.date.today().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        session.merge(post_edit)
        session.commit()
        session.close()
        return redirect(url_for('get_all_posts'))

    # get all posts
    posts = session.query(BlogPost).all()
    session.close()

    post_to_edit = None
    # find the post
    for post in posts:
        if post.id == int(post_id):
            post_to_edit = post

    # pass post information to edit form
    form.title.data = post_to_edit.title
    form.subtitle.data = post_to_edit.subtitle
    form.author.data = post_to_edit.author
    form.img_url.data = post_to_edit.img_url
    form.body.data = post_to_edit.body

    return render_template("edit-post.html", form=form)


@app.route("/delete/<int:index>")
def delete_post(index):
    # create session and get the post
    session = Session()
    post = session.query(BlogPost).filter_by(id=index).first()
    session.delete(post)
    session.commit()
    session.close()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

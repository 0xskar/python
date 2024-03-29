import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

# configuration stuff
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# login manager
login_manager = LoginManager()
login_manager.init_app(app)


# user_loader callback - reloads the user object from the userID stored in the session,
# This uses the str ID of a user and returns the corresponding user object.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # hash the password using pbkdf2:sha256 with salt length of 8

        password = werkzeug.security.generate_password_hash(
            password=request.form.get('password'),
            method="pbkdf2:sha256", salt_length=8)

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # check if user exists
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()

        # check users credentials
        if user is not None and check_password_hash(pwhash=user.password, password=request.form.get('password')):

            # log in user
            login_user(user)

            return redirect(url_for('secrets'))

        flash('Incorrect username/password.')
        return render_template('login.html')

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

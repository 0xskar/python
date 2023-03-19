from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, InputRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "sup3rm3g4s3cr4tk3y"
WTF_CSRF_SECRET_KEY = "sup3rm3g4s3cr4tk3y"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    # Login Validator
    def length_check(min=0, max=-1):
        message = 'Must be between %d and %d characters long.' % (min, max)

        def _length(form, field):
            l = field.data and len(field.data) or 0
            if l < min or max != -1 and l > max:
                raise ValidationError(message)

        return _length

    # Login Form
    class LoginForm(FlaskForm):
        email = StringField(label='Email', validators=[Email(message="Invalid email address.")])
        password = PasswordField(label='Password', validators=[InputRequired(message="Password required."), length_check(max=8)])
        submit = SubmitField(label='Log In')

    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


# TODO-1 create validation for login


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
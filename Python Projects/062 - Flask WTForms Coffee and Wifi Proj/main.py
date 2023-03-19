from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField, TimeField, IntegerField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url_location = URLField('Google Maps URL', validators=[DataRequired(), URL(message="Must be valid URL")])
    open_time = TimeField('Opening Time', validators=[DataRequired()])
    close_time = TimeField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', validators=[DataRequired()], choices=[('✘', '✘'), ('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')])
    wifi_rating = SelectField('WIFI Rating', validators=[DataRequired()], choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')])
    power_rating = SelectField('Power Rating', validators=[DataRequired()], choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    success = False
    form = CafeForm()
    if form.validate_on_submit():
        open_time = f"{form.open_time.data.strftime('%I:%M %p')}"
        close_time = form.close_time.data.strftime('%I:%M %p')
        success = True
        cafe_data = [form.cafe.data, form.url_location.data, open_time, close_time, form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
        with open(file="cafe-data.csv", mode="a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(cafe_data)
    return render_template('add.html', form=form, success=success)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

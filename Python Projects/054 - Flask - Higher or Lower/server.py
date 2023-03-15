from flask import Flask
import random

# Random Number Website?

# Generate a number between 0-9
random_num = random.randint(0, 9)


app = Flask(__name__)


@app.route("/")
def main_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           f'<br>' \
           '<iframe src="https://giphy.com/embed/42wQXwITfQbDGKqUP7" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/detectivepikachumovie-pikachu-detective-detectivepikachu-42wQXwITfQbDGKqUP7">via GIPHY</a></p>'


@app.route("/guess/<int:guess>")
def guess(guess):
    if guess > random_num:
        return f'{guess} is too high, guess again.'
    if guess < random_num:
        return f'{guess} is too low, guess again.'
    else:
        return f'{random_num} was the correct guess, good job!'

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

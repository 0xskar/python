from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
    return render_template("login.html", username=username, password=password)
    #do something cool



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

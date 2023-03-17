import os
from flask import Flask, render_template
import markdown
import datetime
import requests
from posts import Post

# strapi
STRAPI_ENDPOINT = "http://192.168.0.35:1337/api/articles"
STRAPI_API_KEY = os.environ['STRAPI_API_KEY']
STRAPI_HEADER = {
    "Authorization": f"Bearer {STRAPI_API_KEY}",
    "Content-Type": f"application/json"
}

# define app
app = Flask(__name__)

# get year for footer copyright
current_year = datetime.datetime.now().year
footer_copyright = f"Copyright © {current_year} Errol Vogt. Some rights reserved."

# post container
all_posts = []

@app.route('/')
def home():
    return render_template("index.html", footer_copyright=footer_copyright)


@app.route('/guess-age/<name>')
def guess(name):
    # api request for agify
    AGIFY_ENDPOINT = "https://api.agify.io/"
    request = requests.get(url=AGIFY_ENDPOINT)
    agify_response = request.json()
    agify_age = agify_response['age']
    return render_template("guess_age.html", name=name, age=agify_age)


@app.route('/blog')
def list_posts():
    params = {
        "publicationState": "live",
        "fields[0]": "title,description,content"
    }
    r = requests.get(url=STRAPI_ENDPOINT, headers=STRAPI_HEADER, params=params)
    posts = r.json()['data']
    for post in posts:
        post = Post(id_num=post['id'], title=post['attributes']['title'], description=post['attributes']['description'], content=markdown.markdown(post['attributes']['content']))
        all_posts.append(post)
    return render_template('list_posts.html', posts=all_posts)


@app.route('/blog/<int:index>')
def show_post(index):
    page = False
    for post in all_posts:
        if post.id == index:
            page = post
    return render_template('post.html', post=page)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

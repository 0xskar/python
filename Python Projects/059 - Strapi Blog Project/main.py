import os

import requests
from flask import Flask, render_template
from strapistuff import Posts

app = Flask(__name__)

# strapi CMS
api_key = os.environ['STRAPI_API_KEY']
url_endpoint = "http://192.168.0.35:1337/api/articles"
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Get the recent 25 posts from strapi
params = {
    "sort": "id:desc"
}
r = requests.get(url=url_endpoint, headers=headers, params=params)
print(r.status_code)
data = r.json()['data']
blog_posts = []
for post in data:
    title = post['attributes']['title']
    tags = post['attributes']['tags']
    categories = post['attributes']['categories']
    content = post['attributes']['content']
    blog_posts.append(Posts(title, tags, categories, content))


@app.route("/")
def index():
    print(blog_posts)
    return render_template("index.html", posts=blog_posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/post.html")
def post():
    return render_template("post.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
